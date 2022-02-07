import json
import os
import requests
import logging
import glob
from copy import deepcopy
from helpers import safe_name, get_auth_session, strip_ref
from property import Property
from api import ApiEndpoint
from overrides import Override


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

    def get_source(self):
        """
        Pull the API JSON from the remote swagger url
        """

        try:
            response = self.session.get(self.swagger_url)
        except Exception as err:
            err_str = f"Failed to download swagger from: {self.swagger_url} with error {err}"
            self.logger.error(err_str)
            raise ConnectionError(err_str)
        self.logger.info(f"Successfully downloaded Ping Swagger document: {self.swagger_url}")
        self.ping_data = response.json()
        self.base_path = self.ping_data.get('basePath', self.swagger_url)
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

    def get_v11_plus_schemas(self):
        """
        Versions of Ping Federate greater than v11 use Swagger 2.0 and a cleaner
        implementation exists.
        """
        for api in self.ping_data.get("paths", {}):
            safe_api_name = safe_name(api, rem_leading_char=True)
            self.apis[safe_api_name] = ApiEndpoint(api, self.ping_data["paths"][api], v11=True)
        self.models = self.ping_data.get("definitions", {})

        for model_name, model_data in self.models.items():
            model_ref = None
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

    def get_enums_and_imports(self):
        for model_name, details in self.models.items():
            imports = {"models": set(), "enums": set()}
            model_props = {}
            for prop_name, prop in details.get("properties", {}).items():
                if type(prop) == dict:
                    model_property = Property(prop, model_name, prop_name)
                    model_import = model_property.get_model_import()
                    enum_import = model_property.get_enum_import()
                    if model_property.type == "DataStore" or \
                       model_property.type == "list" and \
                       model_property.sub_type == "DataStore":
                        imports["models"].add("JdbcDataStore")
                        imports["models"].add("CustomDataStore")
                        imports["models"].add("LdapDataStore")
                        imports["models"].add("DataStore")
                    if model_import and model_import not in imports["models"]:
                        imports["models"].add(model_import)
                    if enum_import and enum_import not in imports["enums"]:
                        imports["enums"].add(enum_import)

                    enums = model_property.get_enums()
                    if enums:
                        enum_name, enum_domain = enums
                        self.enums[enum_name] = enum_domain

                model_props[prop_name] = model_property

            details["properties"] = model_props
            details["imports"] = imports

            self.models[model_name] = details

    def fetch(self):
        self.get_source()
        if self.swagger_version == "1.2":
            self.get_api_schemas()
        elif self.swagger_version == "2.0":
            self.get_v11_plus_schemas()
        self.get_enums_and_imports()

        return {
            "models": self.models,
            "apis": self.apis,
            "enums": self.enums
        }


if __name__ == "__main__":
    Fetch("https://localhost:9999/pf-admin-api/v1/api-docs").fetch()
