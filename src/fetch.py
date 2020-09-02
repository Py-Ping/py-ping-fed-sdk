import json
import os
import requests
import logging
from helpers import json_type_convert, safe_name
from property import Property


class ApiEndpoint:
    def __init__(self, api_path, api_data):
        self.api_data = api_data
        self.safe_api_path = safe_name(api_path)
        self.path = api_path
        self.response_codes = []
        self.imports = set()
        self.operations = []
        self._process()

    def _process(self):
        for data in self.api_data:
            for op in data["operations"]:
                params = []
                for param in op["parameters"]:
                    param_obj = Parameter(param)
                    params.append(param_obj)
                    if not param_obj.is_primitive_type and param_obj.type not in self.imports:
                        self.imports.add(param_obj.type)

                op_response_codes = []
                for response_code in op["responseMessages"]:
                    op_code = {"code": response_code["code"], "message": response_code["code"]}
                    op_response_codes.append(op_code)
                    if response_code["code"] not in self.response_codes:
                        self.response_codes.append(response_code["code"])

                if not json_type_convert(op["type"]) and op["type"] not in self.imports:
                    self.imports.add(op["type"])
                self.operations.append(
                    Operation(
                        params, op_response_codes, op["type"],
                        op["nickname"], op["summary"], op["method"], data["path"])
                )


class Operation:
    def __init__(self, parameters=[], response_codes=[], op_type=None, nickname='', summary='', method='', api_path=''):
        self.parameters = parameters
        self.response_codes = response_codes
        self.json_type = op_type
        self.type = op_type
        if json_type_convert(op_type):
            self.type = json_type_convert(op_type)
        self.is_primitive_type = bool(json_type_convert(op_type))
        self.nickname = nickname
        self.summary = summary
        self.method = method
        self.api_path = api_path

    def get_response_str(self):
        if json_type_convert(self.json_type) not in ("", "None") and self.is_primitive_type:
            return f"{self.type}(response)"
        elif json_type_convert(self.json_type) == "None":
            return "response"
        else:
            return f"Model{self.type}.from_dict(response.json())"

    def get_return_type_str(self):
        if self.type not in ("", "None") and self.is_primitive_type:
            return self.type
        elif self.type == "None":
            return "dict"
        return f"Model{self.json_type}"


class Parameter:
    def __init__(self, param):
        self._raw_param = param
        self.json_type = self._raw_param["type"]
        self.type = self._raw_param["type"]
        if json_type_convert(self._raw_param["type"]):
            self.type = json_type_convert(self._raw_param["type"])
        self.name = self._raw_param["name"]
        self.safe_name = safe_name(self._raw_param["name"])
        self.is_primitive_type = bool(json_type_convert(self._raw_param["type"]))

    def get_parameter_str(self):
        if self.is_primitive_type:
            return self.type
        return f"Model{self.json_type}"


class Fetch():
    def __init__(self, swagger_url, api_schema_key="apis"):
        logging.basicConfig(
            format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p"
        )
        self.project_path = os.path.dirname(os.path.realpath(__file__))
        self.logger = logging.getLogger("PingSDK.Fetch")
        self.logger.setLevel(
            int(os.environ.get("Logging", logging.INFO))
        )
        self.api_schema_key = api_schema_key
        self.swagger_url = swagger_url
        self.ping_data = {}
        self.models = {}
        self.apis = {}
        self.enums = {}

    def get_source(self, verify=False):
        """
            Pull the API JSON from the remote swagger url
        """

        try:
            response = requests.get(self.swagger_url, verify=verify)
        except Exception as err:
            err_str = f"Failed to download swagger from: {self.swagger_url} with error {err}"
            self.logger.error(err_str)
            raise ConnectionError(err_str)
        self.logger.info(f"Successfully downloaded Ping Swagger document: {self.swagger_url}")
        self.ping_data = response.json()
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

    def get_api_schema(self, api_schema_key="apis", verify=False):
        """
            Iterate over each API in the schema file pf-admin-api and pull
            down each paths content. Store in the api and model dictionaries
            and write to the repository
        """
        for api in self.ping_data.get(api_schema_key, {}):
            safe_api_path = safe_name(api.get("path"))
            api_path = api.get("path")
            abs_path = f"{self.project_path}/pingfedsdk/source/apis/{safe_api_path}.json"
            if os.path.exists(abs_path):
                response = self.read_json(file=abs_path)
                self.apis[safe_name(response.get("resourcePath", safe_api_path))] = ApiEndpoint(
                    api_path, response.get("apis", [])
                )
                self.models.update(response.get("models", {}))
            else:
                try:
                    self.logger.info(f"Attempting to retrieve {self.swagger_url}{api_path}")
                    response = requests.get(f"{self.swagger_url}{api.get('path')}", verify=verify)
                except Exception as err:
                    self.logger.error(f"Failed to download swagger from: {self.swagger_url}{api_path} with error {err}")
                else:
                    r_json = response.json()

                    self.apis[r_json.get("resourcePath", safe_api_path)] = ApiEndpoint(api_path, r_json.get("apis", []))
                    self.models.update(r_json.get("models", {}))
                    self.logger.debug(f"Successfully downloaded Ping Swagger document: {self.swagger_url}{api_path}")
                    if safe_api_path.startswith('_'):
                        safe_api_path = safe_api_path[1:]
                    self.write_json(data=r_json, name=safe_api_path, directory="../pingfedsdk/source/apis/")

        self.processed_model = {}
        for model, details in self.models.items():
            imports = {"models": set(), "enums": set()}
            for prop_name, prop in details.get("properties", {}).items():
                model_property = Property(prop, model, prop_name)
                model_import = model_property.get_model_import()
                enum_import = model_property.get_enum_import()
                if model_import and model_import not in imports["models"]:
                    imports["models"].add(model_import)
                if enum_import and enum_import not in imports["enums"]:
                    imports["enums"].add(enum_import)

                enums = model_property.get_enums()
                if enums:
                    enum_name, enum_domain = enums
                    self.enums[enum_name] = enum_domain

                details["properties"][prop_name] = model_property
            details["imports"] = imports

            self.models[model] = details

    def fetch(self):
        self.get_source()
        self.get_api_schema()

        return {
            "models": self.models,
            "apis": self.apis,
            "enums": self.enums
        }


if __name__ == "__main__":
    Fetch("https://localhost:9999/pf-admin-api/v1/api-docs").fetch()
