import logging
import requests
import os
from requests.exceptions import HTTPError


class _oauth_resourceOwnerCredentialsMappings():
    def __init__(self, endpoint: str) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._oauth_resourceOwnerCredentialsMappings')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getResourceOwnerCredentialsMappings(self):
        """ Get the list of Resource Owner Credentials Grant Mapping.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/resourceOwnerCredentialsMappings"),
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
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
        finally:
            return response.json()

    def createResourceOwnerCredentialsMapping(self, body, XBypassExternalValidation):
        """ Create a new Resource Owner Credentials mapping.
        """

        payload = {
            "body": body,
            "XBypassExternalValidation": XBypassExternalValidation

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/oauth/resourceOwnerCredentialsMappings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info("Resource owner credentials mapping created.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getResourceOwnerCredentialsMapping(self, var_id):
        """ Find the Resource Owner Credentials mapping by the ID.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/resourceOwnerCredentialsMappings/{id}"),
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
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def updateResourceOwnerCredentialsMapping(self, var_id, body, XBypassExternalValidation):
        """ Update a Resource Owner Credentials mapping.
        """

        payload = {
            "var_id": var_id,
            "body": body,
            "XBypassExternalValidation": XBypassExternalValidation

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/oauth/resourceOwnerCredentialsMappings/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Resource owner credentials mapping updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def deleteResourceOwnerCredentialsMapping(self, var_id):
        """ Delete a Resource Owner Credentials mapping.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/oauth/resourceOwnerCredentialsMappings/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info("Resource owner credentials mapping deleted.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

