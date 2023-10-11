from json import dumps
import logging
import os
import traceback

from requests import Session
from requests.exceptions import HTTPError

from pingfedsdk.models.configuration_encryption_keys import ConfigurationEncryptionKeys as ModelConfigurationEncryptionKeys


class ConfigurationEncryptionKeys:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.ConfigurationEncryptionKeys")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getConfigurationEncryptionKeys(self):
        """ Get the list of Configuration Encryption Keys.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/configurationEncryptionKeys"),
                headers={"Content-Type": "application/json"}
            )
        except HTTPError as http_err:
            print(traceback.format_exc())
            self.logger.error(f"HTTP error occurred: {http_err}")
            raise http_err
        except Exception as err:
            print(traceback.format_exc())
            self.logger.error(f"Error occurred: {err}")
            raise err
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelConfigurationEncryptionKeys.from_dict(response_dict)
            else:
                return ModelConfigurationEncryptionKeys.from_dict(response.json())

    def rotateConfigurationEncryptionKey(self):
        """ Rotate the current Configuration Encryption Key.
        """

        try:
            response = self.session.post(
                url=self._build_uri("/configurationEncryptionKeys/rotate"),
                headers={"Content-Type": "application/json"}
            )
        except HTTPError as http_err:
            print(traceback.format_exc())
            self.logger.error(f"HTTP error occurred: {http_err}")
            raise http_err
        except Exception as err:
            print(traceback.format_exc())
            self.logger.error(f"Error occurred: {err}")
            raise err
        else:
            if response.status_code == 201:
                self.logger.info("Configuration encryption key rotated.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelConfigurationEncryptionKeys.from_dict(response_dict)
            else:
                return ModelConfigurationEncryptionKeys.from_dict(response.json())
