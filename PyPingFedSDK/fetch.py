import json
import os
import sys
import requests
import logging

ping_swagger_url = "https://sso.anycompany.org:9999/pf-admin-api/v1/api-docs"

class Fetch():
    def __init__(self, api_schema_key='apis'):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL.Fetch')
        self.logger.setLevel(int(os.environ.get('Logging', logging.INFO)))
        self.api_schema_key = api_schema_key
        self.ping_data = {}
        self.models = {}
        self.apis = {}

    def get_source(self, ping_swagger_url=ping_swagger_url, verify=False):
        content_type = "application/json"
        request_headers = {'Content-Type': content_type}

        try:
            response = requests.get(ping_swagger_url, verify=verify)
        except Exception as err:
            self.logger.error(f'Failed to download swagger from: {ping_swagger_url} with error {err}')
            raise URLError(f'Failed to download swagger from: {ping_swagger_url} with error {err}')
        else:
            self.logger.info(f'Successfully downloaded Ping Swagger document: {ping_swagger_url}')
            self.ping_data = response.json()
            self.write_json(data=response.json(), name="pf-admin-api", dir="./source/" )
        finally:
            self.logger.debug(json.dumps(self.ping_data, default=str, sort_keys=True, indent=4, separators=(',', ': ')))

    def write_json(self, data, name, file_type="json", dir=None):
        filedirectory = os.path.dirname(os.path.realpath(__file__))
        if dir:
            targetdirectory = os.path.join(
                filedirectory, dir)
        else:
            targetdirectory = os.path.join(
                filedirectory, './templates/resources/')

        if not os.path.exists(targetdirectory):
            os.makedirs(targetdirectory)

        path = f'{targetdirectory}/{name}.{file_type}'
        if file_type == "json":
            with open(os.path.join(filedirectory, path), "w") as fh:
                fh.write(json.dumps(data, default=str, sort_keys=True, indent=4, separators=(',', ': ')))
        else:
            with open(os.path.join(filedirectory, path), "w") as fh:
                fh.write(data)

    def read_json(self, file):

        filedirectory = os.path.dirname(os.path.realpath(__file__))
        try:
            with open(os.path.join(filedirectory, file), 'r') as file:
                content = file.read()
        except IOError as err:
            return False

        return json.loads(content)

    def get_api_schema(self, api_schema_key='apis', verify=False):
        for api in self.ping_data.get(api_schema_key, {}):
            if os.path.exists(f"{os.path.dirname(os.path.realpath(__file__))}/source/apis/{self.safe_name(api.get('path'))}.json"):
                response = self.read_json(file=f"./source/apis/{self.safe_name(api.get('path'))}.json")
                self.apis[self.safe_name(response.get('resourcePath', self.safe_name(api.get('path'))))] = (response.get('apis', []))
                self.models.update(response.get('models', {}))
            else:
                try:
                    self.logger.info(f'Attempting to retrieve {ping_swagger_url}{api.get("path")}')
                    response = requests.get(f"{ping_swagger_url}{api.get('path')}", verify=verify)
                except Exception as err:
                    self.logger.error(f'Failed to download swagger from: {ping_swagger_url}{api.get("path")} with error {err}')
                else:
                    self.apis[response.json().get('resourcePath', self.safe_name(api.get('path')))] = (response.json().get('apis', []))
                    self.models.update(response.json().get('models', {}))
                    self.logger.debug(f'Successfully downloaded Ping Swagger document: {ping_swagger_url}{api.get("path")}')
                    self.write_json(data=response.json(), name=self.safe_name(api.get("path")), dir="./source/apis/" )

    def fetch(self):
        self.get_source()
        self.get_api_schema()

        return {
            "models": self.models,
            "apis": self.apis
        }

    def safe_name(self, unsafe_string, unsafe_char='/', sub_char='_'):
        safe_string_list = [x if x not in unsafe_char else sub_char for x in unsafe_string]

        return str(''.join(safe_string_list))

if __name__ == '__main__':
    Fetch().fetch()
