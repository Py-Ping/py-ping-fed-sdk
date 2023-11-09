import importlib.util
import json
import os
from pathlib import Path
import requests
import logging
import glob
import urllib3
import pkgutil
from urllib.parse import urljoin

from copy import deepcopy
from helpers import safe_name, get_auth_session, strip_ref
from property import Property
from api import ApiEndpoint
from overrides import Override
import patches


class PatchesNotFound(Exception):
    """No patches found for a particular PingFed version"""


class Fetch():
    def __init__(self, swagger_url, api_schema_key="apis", verify=False, session=None, swagger_version="1.2"):
        logging.basicConfig(
            format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p"
        )
        self.swagger_version = swagger_version
        self.project_path = os.path.dirname(os.path.realpath(__file__))
        self.logger = logging.getLogger("PingSDK.Fetch")
        self.logger.setLevel(
            int(os.environ.get("Logging", logging.INFO))
        )
        self.base_path = None
        self.session = session
        if session is None and self.swagger_version == "2.0":
            self.session = get_auth_session()
        elif session is None:
            self.session = requests.Session()
        self.session.verify = verify
        self.api_schema_key = api_schema_key
        self.swagger_url = swagger_url
        self.ping_data = {}
        self.models = {}
        self.apis = {}
        self.enums = {}
        self.server_version = None

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def get_source(self):
        """
        Pull the API JSON from the remote swagger url
        """

        try:
            response = self.session.get(self.swagger_url)
            if response.status_code == 401 or response.status_code == 404:
                raise Exception("Invalid swagger url or credentials, this can be as set as an environment variable, "
                                "see documentation.")
        except Exception as err:
            err_str = f"Failed to download swagger from: {self.swagger_url} with error {err}"
            self.logger.error(err_str)
            raise ConnectionError(err_str)
        self.logger.info(f"Successfully downloaded Ping Swagger document: {self.swagger_url}")
        self.ping_data = response.json()
        self.base_path = self.ping_data.get('basePath', self.swagger_url)
        self.logger.info("Writing source data to pingfedsdk/source/pf-admin-api.json")
        self.write_json(data=self.ping_data, name="pf-admin-api", directory="../pingfedsdk/source/")
        self.logger.debug(
            json.dumps(self.ping_data, default=str, sort_keys=True, indent=4, separators=(",", ": "))
        )

    def write_json(self, data, name, directory=None):
        """
        given string data write it to file name in folder directory
        """
        if not directory:
            directory = "./templates/resources/"
        targetdirectory = os.path.join(self.project_path, directory)

        if not os.path.exists(targetdirectory):
            os.makedirs(targetdirectory)

        path = f"{targetdirectory}/{name}.json"

        with open(os.path.join(self.project_path, path), "w") as fh:
            fh.write(json.dumps(data, default=str, sort_keys=True, indent=4, separators=(",", ": ")))

    def read_json(self, file):
        """
        extract a JSON document from the project path
        and load into a dict type
        """
        try:
            with open(os.path.join(self.project_path, file), "r") as file:
                return json.loads(file.read())
        except IOError:
            return False

    def get_server_version(self):
        """Get version of server which is being processed

        Note that the path to the version is the same across Ping Federate
        versions."""
        api_path = f'{self.ping_data["basePath"]}/version'
        response = self.session.get(urljoin(self.swagger_url, api_path))
        response.raise_for_status()
        response = response.json()
        return response['version']

    def apply_20_patches(self, patch_root: Path):
        self.logger.debug('Searching for patches in:%s', patch_root)
        if not patch_root.exists():
            raise PatchesNotFound(f'{patch_root} does not exist')
        modules = pkgutil.iter_modules([str(patch_root)])
        patch_modules = sorted([p for p in modules if not p.ispkg],
                               key=lambda mi: mi.name)
        self.logger.debug('%s patch_modules:%s', patch_root, patch_modules)
        for patch_mod in patch_modules:
            self.logger.debug('Applying patch:%s in:%s',
                              patch_mod.name, patch_mod.module_finder.path)
            mod_spec = patch_mod.module_finder.find_spec(patch_mod.name)
            module = importlib.util.module_from_spec(mod_spec)
            mod_spec.loader.exec_module(module)
            patch_callable = vars(module).get('patch', None)
            if patch_callable:
                patch_callable(self.swagger_version, self.ping_data)
            else:
                self.logger.warning('No callable found for:%s, skipping',
                                    patch_mod.name)

    def patch_20_source(self):
        """
        Patch the parsed swagger 2.0 json by running (python) hooks.

        Note that swagger 2.0 presents its info in a totally different
        structure than swagger 1.0. which makes the v1.0 patching mechanism
        unusable for v2.0.

        Patch modules must define a "patch" callable which must conform to
        the following signature:

          def patch(swagger_version: str, input_swagger: dict) -> None:

        i.e. the callable takes a swagger version and an input dictionary which
        is the Python representation of the swagger definition (i.e. the
        original swagger has already been parsed into Python) in the patch
        chain. The callable should examine the input dictionary and modify it
        as necessary. The modified result of the swagger definition will be
        then passed as input to the next patch and so on until all patches have
        been applied.

        Patches reside in the "patches" submodule of this module and are
        applied in the following order:
            - the "patches" directory is scanned for all patch modules (i.e.
              *.py). These should be version agnostic patches.
            - The patch modules are imported in alphabetical order and their
              "patch" callable called with the output of a "patch" call being
              fed to the next "patch" call as its input.

        Next the patches in the subdirectory corresponding to the PingFederate
        server's major version are loaded and processed in the same manner as
        above. To make it easy to import the version specific patches the
        subdirectories take the format "v_$majorversion", e.g.
        "v_11" holds all patches across PingFederate 11.y.z.

        Following that the subdirectories in the major version specific
        directory (which would represent the minor version) are processed in
        the same manner. The subdirectories must be named with the full version
        upto the minor version (e.g. "v_11_3" represents patches for
        PingFederate 11.3).

        Patch levels can be arbitrarily deep - the patch engine traverses the
        directory tree for each patch component and (if it exists) it applies
        all the patches found in that directory.
        """
        curr_path = Path(patches.__path__[0])
        patch_paths = [curr_path]
        curr_prefix = 'v'
        for vpart in self.server_version:
            curr_prefix = f'{curr_prefix}_{vpart}'
            curr_path = curr_path / curr_prefix
            patch_paths.append(curr_path)

        for patch_path in patch_paths:
            try:
                self.apply_20_patches(patch_path)
            except PatchesNotFound:
                break

    def apply_override_patch(self, api_name, api_version, api_data):
        override_path = f"src/overrides/{api_name}"
        if api_version and os.path.exists(f"{override_path}.{api_version}.delta"):
            override_path = f"{override_path}.{api_version}.delta"
            override = Override(override_path, api_version)
            return override.apply_patch(api_data)
        elif os.path.exists(f"{override_path}.all.delta"):
            override = Override(f"{override_path}.all.delta", api_version)
            return override.apply_patch(api_data)
        return api_data

    def get_api_schema(self, api_path, api_name):
        safe_api_name = safe_name(api_name)
        print(api_path)
        if os.path.exists(api_path):
            response = self.read_json(file=api_path)
            response = self.apply_override_patch(safe_api_name[1:], response["apiVersion"], response)
            if api_name != "/overrides":
                self.apis[response.get("resourcePath", safe_api_name)] = ApiEndpoint(
                    api_name, response.get("apis", [])
                )
            self.models.update(response.get("models", {}))
        else:
            try:
                self.logger.info(f"Attempting to retrieve {self.base_path}{api_name}")
                response = self.session.get(f"{self.base_path}{api_name}")
            except Exception as err:
                self.logger.error(f"Failed to download swagger from: {self.base_path}{api_name} with error {err}")
            else:
                r_json = response.json()
                r_json = self.apply_override_patch(safe_api_name[1:], r_json["apiVersion"], r_json)

                self.apis[r_json.get("resourcePath", safe_api_name)] = ApiEndpoint(api_name, r_json.get("apis", []))
                self.models.update(r_json.get("models", {}))
                self.logger.debug(f"Successfully downloaded Ping Swagger document: {self.base_path}{api_name}")
                if safe_api_name.startswith("_"):
                    safe_api_name = safe_api_name[1:]
                self.write_json(data=r_json, name=safe_api_name, directory="../pingfedsdk/source/apis/")

    def get_api_schemas(self, api_schema_key="apis"):
        """
        Iterate over each API in the schema file pf-admin-api and pull
        down each paths content. Store in the api and model dictionaries
        and write to the repository
        """

        for api in self.ping_data.get(api_schema_key, {}):
            safe_api_name = safe_name(api.get("path"))
            if safe_api_name.startswith("_"):
                safe_api_name = safe_api_name[1:]
            api_path = f"{self.project_path}/../pingfedsdk/source/apis/{safe_api_name}.json"
            self.get_api_schema(api_path, api.get("path"))

        api_path = f"{self.project_path}/overrides/*.json"
        for file_path in glob.glob(api_path):
            file_name = file_path.split("/")[-1].split(".")[0]
            # set the overridden definitions
            self.get_api_schema(file_path, f'/{file_name}')

    def update_v11_schema(self):
        self.ping_data_v11 = {}
        for api in self.ping_data.get("paths", {}):
            action = list(self.ping_data["paths"][api].keys())[0]
            action_tag = self.ping_data["paths"][api][action]["tags"][0]
            if action_tag not in self.ping_data_v11:
                self.ping_data_v11[action_tag] = {}
            for action in self.ping_data["paths"][api]:
                self.ping_data_v11[action_tag].update({f'{api}-{action}': self.ping_data["paths"][api][action]})

    def get_v11_plus_schemas(self):
        """
        Versions of Ping Federate greater than v11 use Swagger 2.0 and a cleaner
        implementation exists.
        """
        for api, api_data in self.ping_data_v11.items():
            safe_api_name = safe_name(api, rem_leading_char=True)
            self.apis[safe_api_name] = ApiEndpoint(api, api_data, v11=True)
        self.models = self.ping_data.get("definitions", {})

        for model_name, model_data in self.models.items():
            if "allOf" in model_data:
                inherit_model = None
                special_details = None
                for inherit_data in model_data["allOf"]:
                    if "$ref" in inherit_data:
                        inherit_model = strip_ref(inherit_data["$ref"])
                    if "type" in inherit_data:
                        special_details = inherit_data
                ground_model_data = deepcopy(self.models[inherit_model])
                for attr, attr_value in special_details.items():
                    if attr == "properties":
                        continue
                    ground_model_data[attr] = special_details[attr]

                for prop, prop_data in special_details["properties"].items():
                    ground_model_data["properties"][prop] = prop_data

                self.models[model_name] = ground_model_data

    @staticmethod
    def sort_properties(property_list):
        # First sort by position
        by_position = sorted(property_list, key=lambda p: p.position)
        # Sort properties with same position values alphabetically
        sorted_props = []
        curr_group = []
        curr_position = None
        for prop in by_position:
            if prop.position != curr_position:
                # New group of properties - sort the previous batch
                sorted_props.extend(sorted(curr_group, key=lambda p: p.name))
                curr_group = [prop]
            else:
                curr_group.append(prop)
        else:
            sorted_props.extend(sorted(curr_group, key=lambda p: p.name))
        return sorted_props

    def get_enums_and_imports(self):
        for model_name, details in self.models.items():
            import_models = set()
            import_enums = set()
            model_props = {}
            required_props = []
            optional_props = []
            required = details.get('required', [])
            for prop_name, prop in details.get("properties", {}).items():
                if isinstance(prop, dict):
                    model_property = Property(prop, model_name, prop_name)
                    model_import = model_property.get_model_import()
                    enum_import = model_property.get_enum_import()
                    if enum_import == model_name:
                        import_suffix = f' as {enum_import}Enum'
                    else:
                        import_suffix = ''
                    if model_property.type == "DataStore" or \
                       model_property.type == "list" and \
                       model_property.sub_type == "DataStore":
                        import_models.add("JdbcDataStore")
                        import_models.add("CustomDataStore")
                        import_models.add("LdapDataStore")
                        import_models.add("DataStore")
                    if model_import:
                        import_models.add(model_import)
                    if enum_import:
                        import_enums.add((enum_import, import_suffix))

                    enums = model_property.get_enums()
                    if enums:
                        enum_name, enum_domain = enums
                        self.enums[enum_name] = enum_domain

                    model_props[prop_name] = model_property
                else:
                    # TODO: Should define custom exceptions!
                    raise Exception(f"Invalid property definition "
                                    f"for:{prop_name}: {prop}")
                if prop_name in required:
                    required_props.append(model_property)
                else:
                    optional_props.append(model_property)
            details["properties"] = model_props
            details["imports"] = {
                # keep keys in sorted order so that the imports are generated
                # in alphabetical order
                "enums": sorted(list(import_enums)),
                "model": ["Model"],  # always import the pingfed.model.Model
                "models": sorted(list(import_models)),
            }
            details["conflict_suffix"] = Property.CONFLICT_SUFFIX
            details["sorted_required"] = self.sort_properties(required_props)
            details["sorted_optional"] = self.sort_properties(optional_props)

            self.models[model_name] = details

    def fetch(self):
        self.get_source()
        if self.swagger_version == "1.2":
            self.logger.info("Getting API schemas for swagger version 1.2")
            self.get_api_schemas()
        elif self.swagger_version == "2.0":
            self.server_version = self.get_server_version().split('.')
            self.patch_20_source()
            self.write_json(
                data=self.ping_data, name='pf-admin-api-patched',
                directory="../pingfedsdk/source/"
            )
            self.logger.info("Getting API schemas for swagger version 2.0")
            self.update_v11_schema()
            self.get_v11_plus_schemas()
        self.logger.info("Getting Enums and Imports")
        self.get_enums_and_imports()

        return {
            "models": self.models,
            "apis": self.apis,
            "enums": self.enums
        }


if __name__ == "__main__":
    Fetch("https://localhost:9999/pf-admin-api/v1/swagger.json", swagger_version='2.0').fetch()
