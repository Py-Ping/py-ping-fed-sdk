import logging
import requests
import os
from requests.exceptions import HTTPError


class _idp_connectors():
    def __init__(self, endpoint: str) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._idp_connectors')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getIdpConnectorDescriptors(self):
        """ Get the list of available IdP connector descriptors.
        """

        try:
            response = requests.get(

                url=self._build_uri("/idp/connectors/descriptors"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its IdP role enabled. Operation not available.')
        finally:
            return response

    def getIdpConnectorDescriptorById(self, var_id):
        """ Get the list of available connector descriptors.
        """

        try:
            response = requests.get(

                url=self._build_uri("/idp/connectors/descriptors/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its IdP role enabled. Operation not available.')
        finally:
            return response

