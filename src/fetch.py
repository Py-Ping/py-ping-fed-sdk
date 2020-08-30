import json
import os
import requests
import logging
from helpers import json_type_convert, safe_name


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
                self.apis[safe_name(response.get("resourcePath", safe_api_path))] = self.preprocess_api(
                    response.get("apis", [])
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
                    self.apis[r_json.get("resourcePath", safe_api_path)] = self.preprocess_api(r_json.get("apis", []))
                    self.models.update(r_json.get("models", {}))
                    self.logger.debug(f"Successfully downloaded Ping Swagger document: {self.swagger_url}{api_path}")
                    if safe_api_path.startswith('_'):
                        safe_api_path = safe_api_path[1:]
                    self.write_json(data=r_json, name=safe_api_path, directory="../pingfedsdk/source/apis/")

        for model, details in self.models.items():
            details["imports"] = self.get_model_imports(details)
            self.models[model] = details

    def preprocess_api(self, api_data):
        """
        Pre-process the API document and determine what needs to be imported
        to dynamically generate return objects
        """
        imports = set()
        response_codes = set()
        for data in api_data:
            for op in data["operations"]:
                for param in op["parameters"]:
                    if not json_type_convert(param["type"]) and param["type"] not in imports:
                        imports.add(param["type"])
                for response_code in op["responseMessages"]:
                    if response_code["code"] not in response_codes:
                        response_codes.add(response_code["code"])
                if not json_type_convert(op["type"]) and op["type"] not in imports:
                    imports.add(op["type"])
        return {"imports": imports, "codes": response_codes, "details": api_data}

    def get_model_imports(self, model_data):
        """
        For a given model, determine it's other model dependencies, enum dependencies
        and cache discovered
        """
        imports = {"models": set(), "enums": set()}
        for prop in model_data.get("properties").values():
            class_name = prop.get("$ref", "")
            # check for a model import and add it to the set
            if class_name and "enum" not in prop and not class_name.startswith("File"):
                if class_name.startswith("Map"):
                    key_label, value_label = class_name.replace("Map[", "").replace("]", "").split(",")
                    if not json_type_convert(key_label):
                        imports["models"].add(key_label)
                    if not json_type_convert(value_label):
                        imports["models"].add(value_label)
                elif class_name == "Set" and "items" in prop:
                    if "enum" in prop["items"]:
                        imports["enums"].add(prop["items"]["$ref"])
                        if prop["items"]["$ref"] in self.enums and self.enums[prop["items"]["$ref"]] != prop["items"]["enum"]:
                            self.logger.warn(
                                f"Found redefined enum type: {class_name}"
                                f" original -> {self.enums[class_name]}, new -> {prop['enum']}..."
                            )
                        self.enums[prop["items"]["$ref"]] = prop["items"]["enum"]
                    elif "$ref" in prop["items"] and not json_type_convert(prop["items"]["$ref"]):
                        imports["models"].add(prop["items"]["$ref"])
                else:
                    imports["models"].add(class_name)
            elif "type" in prop and prop["type"] == "array":
                if "$ref" in prop["items"] and not json_type_convert(prop["items"]["$ref"]):
                    imports["models"].add(prop["items"]["$ref"])
            elif class_name and "enum" in prop:
                if class_name in self.enums and self.enums[class_name] != prop["enum"]:
                    self.logger.warn(
                        f"Found redefined enum type: {class_name}"
                        f" original -> {self.enums[class_name]}, new -> {prop['enum']}..."
                    )
                self.enums[class_name] = prop["enum"]
                imports["enums"].add(class_name)
        return imports

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
