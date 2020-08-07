import logging
import requests
import os
from requests.exceptions import HTTPError


class _keyPairs_signing():
    def __init__(self, endpoint):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._keyPairs_signing')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path):
        return f"{self.endpoint}{path}"

    def getKeyPairs(self):
        """ Get list of key pairs.
        """

        try:
            response = requests.get(

                url=self._build_uri("/keyPairs/signing"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
        finally:
            return response.json()

    def importKeyPair(self, body):
        """ Import a new key pair.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/keyPairs/signing/import"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info("Key Pair imported.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("The operation is not permitted, based on the current configuration of the server.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def createKeyPair(self, body):
        """ Generate a new key pair.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/keyPairs/signing/generate"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info("Key Pair created.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getKeyPair(self, id):
        """ Retrieve details of a key pair.
        """

        try:
            response = requests.get(

                url=self._build_uri("/keyPairs/signing/{id}"),
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

    def deleteKeyPair(self, id):
        """ Delete a key pair.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/keyPairs/signing/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info("Key Pair deleted.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Resource is in use and cannot be deleted.")
        finally:
            return response.json()

    def exportCsr(self, id):
        """ Generate a new certificate signing request (CSR) for this key pair.
        """

        try:
            response = requests.get(

                url=self._build_uri("/keyPairs/signing/{id}/csr"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
        finally:
            return response.json()

    def importCsrResponse(self, id, body):
        """ Import a CSR response for this key pair.
        """

        payload = {
            "id": id,
            "body": body

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/keyPairs/signing/{id}/csr"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("CSR Response imported.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def exportPKCS12File(self, id, body):
        """ Download the key pair in PKCS12 format.
        """

        payload = {
            "id": id,
            "body": body

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/keyPairs/signing/{id}/pkcs12"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Key Pair downloaded.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def exportCertificateFile(self, id):
        """ Download the certificate from a given key pair.
        """

        try:
            response = requests.get(

                url=self._build_uri("/keyPairs/signing/{id}/certificate"),
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

    def getRotationSettings(self, id):
        """ Retrieve details of rotation settings for a key pair.
        """

        try:
            response = requests.get(

                url=self._build_uri("/keyPairs/signing/{id}/rotationSettings"),
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

    def updateRotationSettings(self, id, body):
        """ Add rotation settings to a key pair
        """

        payload = {
            "id": id,
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/keyPairs/signing/{id}/rotationSettings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Key Pair updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def deleteKeyPairRotationSettings(self, id):
        """ Delete rotation settings for a signing key pair.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/keyPairs/signing/{id}/rotationSettings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info("Rotation Settings deleted.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

