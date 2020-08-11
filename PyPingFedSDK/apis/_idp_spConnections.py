import logging
import requests
import os
from requests.exceptions import HTTPError


class _idp_spConnections():
    def __init__(self, endpoint: str) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._idp_spConnections')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getConnections(self, entityId, page, numberPerPage, filter):
        """ Get list of SP connections.
        """

        try:
            response = requests.get(

                url=self._build_uri("/idp/spConnections"),
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
                self.logger.info("PingFederate does not have its IdP role enabled. Operation not available.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def createConnection(self, body, XBypassExternalValidation):
        """ Create a new SP connection.
        """

        payload = {
            "body": body,
            "XBypassExternalValidation": XBypassExternalValidation

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/idp/spConnections"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info("Connection created.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its IdP role enabled. Operation not available.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getConnection(self, var_id):
        """ Find SP connection by ID.
        """

        try:
            response = requests.get(

                url=self._build_uri("/idp/spConnections/{id}"),
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
                self.logger.info("PingFederate does not have its IdP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def updateConnection(self, var_id, body, XBypassExternalValidation):
        """ Update an SP connection.
        """

        payload = {
            "var_id": var_id,
            "body": body,
            "XBypassExternalValidation": XBypassExternalValidation

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/idp/spConnections/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Connection updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its IdP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def deleteConnection(self, var_id):
        """ Delete an SP connection.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/idp/spConnections/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info("Connection deleted.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its IdP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Resource is in use and cannot be deleted.")
        finally:
            return response.json()

    def getSigningSettings(self, var_id):
        """ Get the SP connection's signature settings.
        """

        try:
            response = requests.get(

                url=self._build_uri("/idp/spConnections/{id}/credentials/signingSettings"),
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
                self.logger.info("PingFederate does not have its IdP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def updateSigningSettings(self, var_id, body):
        """ Update the SP connection's signature settings.
        """

        payload = {
            "var_id": var_id,
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/idp/spConnections/{id}/credentials/signingSettings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Connection updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its IdP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def addConnectionCert(self, var_id, body):
        """ Add a new SP connection certificate.
        """

        payload = {
            "var_id": var_id,
            "body": body

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/idp/spConnections/{id}/credentials/certs"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info("Connection Certificate added.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its IdP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getConnectionCerts(self, var_id):
        """ Get the SP connection's certificates.
        """

        try:
            response = requests.get(

                url=self._build_uri("/idp/spConnections/{id}/credentials/certs"),
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
                self.logger.info("PingFederate does not have its IdP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def updateConnectionCerts(self, var_id, body):
        """ Update the SP connection's certificates.
        """

        payload = {
            "var_id": var_id,
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/idp/spConnections/{id}/credentials/certs"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Connection updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its IdP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getDecryptionKeys(self, var_id):
        """ Get the decryption keys of an SP connection.
        """

        try:
            response = requests.get(

                url=self._build_uri("/idp/spConnections/{id}/credentials/decryptionKeys"),
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
                self.logger.info("PingFederate does not have its IdP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def updateDecryptionKeys(self, var_id, body):
        """ Updating the SP connection's decryption keys.
        """

        payload = {
            "var_id": var_id,
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/idp/spConnections/{id}/credentials/decryptionKeys"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Connection updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its IdP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

