import logging
import requests
import os
from requests.exceptions import HTTPError


class _idpToSpAdapterMapping():
    def __init__(self, endpoint: str) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._idpToSpAdapterMapping')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getIdpToSpAdapterMappings(self):
        """ Get list of IdP-to-SP Adapter Mappings.
        """

        try:
            response = requests.get(

                url=self._build_uri("/idpToSpAdapterMapping"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have the appropriate IdP/SP role enabled. Operation not available.")
        finally:
            return response.json()

    def createIdpToSpAdapterMapping(self, body, XBypassExternalValidation):
        """ Create a new IdP-to-SP Adapter mapping.
        """

        payload = {
            "body": body,
            "XBypassExternalValidation": XBypassExternalValidation

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/idpToSpAdapterMapping"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info("IdP-to-SP adapter mapping created.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getIdpToSpAdapterMappingsById(self, var_id):
        """ Get an IdP-to-SP Adapter Mapping.
        """

        try:
            response = requests.get(

                url=self._build_uri("/idpToSpAdapterMapping/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def updateIdpToSpAdapterMapping(self, var_id, body, XBypassExternalValidation):
        """ Update the specified IdP-to-SP Adapter mapping.
        """

        payload = {
            "var_id": var_id,
            "body": body,
            "XBypassExternalValidation": XBypassExternalValidation

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/idpToSpAdapterMapping/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("IdP-to-SP adapter mapping updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def deleteIdpToSpAdapterMappingsById(self, var_id):
        """ Delete an Adapter to Adapter Mapping.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/idpToSpAdapterMapping/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info("IdP-to-SP adapter mapping deleted.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

