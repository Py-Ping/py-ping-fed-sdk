import json
import os
import sys
import requests
import logging
from urllib3.exceptions import ConnectionError


class Fetch():
    def __init__(self, swagger_url, api_schema_key="apis"):
        logging.basicConfig(
            format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p"
        )
        self.project_path = os.path.dirname(os.path.realpath(__file__))
        self.logger = logging.getLogger("PingDSL.Fetch")
        self.logger.setLevel(
            int(os.environ.get("Logging", logging.INFO))
        )
        self.api_schema_key = api_schema_key
        self.swagger_url = swagger_url
        self.ping_data = {}
        self.models = {}
        self.apis = {}

    def get_source(self, verify=False):
        """
            Pull the API JSON from the remote swagger url
        """
        content_type = "application/json"
        request_headers = {"Content-Type": content_type}

        try:
            response = requests.get(self.swagger_url, verify=verify)
        except Exception as err:
            err_str = f"Failed to download swagger from: {self.swagger_url} with error {err}"
            self.logger.error(err_str)
            raise ConnectionError(err_str)
        self.logger.info(f"Successfully downloaded Ping Swagger document: {self.swagger_url}")
        self.ping_data = response.json()
        self.write_json(data=self.ping_data, name="pf-admin-api", directory="./source/")
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
        except IOError as err:
            return False

    def get_api_schema(self, api_schema_key="apis", verify=False):
        """
            Iterate over each API in the schema file pf-admin-api and pull
            down each paths content. Store in the api and model dictionaries
            and write to the repository
        """

        for api in self.ping_data.get(api_schema_key, {}):

            safe_api_path = self.safe_name(api.get("path"))
            api_path = api.get("path")
            abs_path = f"{self.project_path}/source/apis/{safe_api_path}.json"
            if os.path.exists(abs_path):
                response = self.read_json(file=abs_path)
                self.apis[self.safe_name(response.get("resourcePath", safe_api_path))] = (response.get("apis", []))
                self.models.update(response.get("models", {}))
            else:
                try:
                    self.logger.info(f"Attempting to retrieve {self.swagger_url}{api_path}")
                    response = requests.get(f"{self.swagger_url}{api.get('path')}", verify=verify)
                except Exception as err:
                    self.logger.error(f"Failed to download swagger from: {self.swagger_url}{api_path} with error {err}")
                else:
                    r_json = response.json()
                    self.apis[r_json.get("resourcePath", safe_api_path)] = (r_json.get("apis", []))
                    self.models.update(r_json.get("models", {}))
                    self.logger.debug(f"Successfully downloaded Ping Swagger document: {self.swagger_url}{api_path}")
                    self.write_json(data=r_json, name=safe_api_path, directory="./source/apis/")

    def fetch(self):
        self.get_source()
        self.get_api_schema()

        return {
            "models": self.models,
            "apis": self.apis
        }

    def safe_name(self, unsafe_string, unsafe_char="/", sub_char="_"):
        """
            replace all instances of unsafe_char with sub_char and return the string
        """
        safe_string_list = [x if x not in unsafe_char else sub_char for x in unsafe_string]
        return "".join(safe_string_list)

if __name__ == "__main__":
    Fetch("https://localhost:9999/pf-admin-api/v1/api-docs").fetch()
