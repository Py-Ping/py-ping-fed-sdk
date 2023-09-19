from json import dumps
import logging
import os
import traceback

from requests import Session
from requests.exceptions import HTTPError

from pingfedsdk.models.saas_plugin_descriptor import SaasPluginDescriptor as ModelSaasPluginDescriptor
from pingfedsdk.models.saas_plugin_descriptors import SaasPluginDescriptors as ModelSaasPluginDescriptors


class IdpConnectors:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.IdpConnectors")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getIdpConnectorDescriptors(self):
        """ Get the list of available IdP connector descriptors.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/idp/connectors/descriptors"),
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
                return ModelSaasPluginDescriptors.from_dict(response.json())

    def getIdpConnectorDescriptorById(self, id: str):
        """ Get the list of available connector descriptors.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/idp/connectors/descriptors/{id}"),
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
                return ModelSaasPluginDescriptor.from_dict(response.json())
