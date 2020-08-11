import os
import logging
from requests import Session
from requests.exceptions import HTTPError


class _keyPairs_sslServer():
    def __init__(self, endpoint:str, session:Session) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._keyPairs_sslServer')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getKeyPairs(self):
        """ Get list of key pairs.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/keyPairs/sslServer"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
        finally:
            return response

    def importKeyPair(self, body):
        """ Import a new key pair.
        """

        payload = {
            "body": body

        }

        try:
            response = self.session.post(
                data=payload,
                url=self._build_uri("/keyPairs/sslServer/import"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info('Key Pair imported.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('The operation is not permitted, based on the current configuration of the server.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def createKeyPair(self, body):
        """ Generate a new key pair.
        """

        payload = {
            "body": body

        }

        try:
            response = self.session.post(
                data=payload,
                url=self._build_uri("/keyPairs/sslServer/generate"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info('Key Pair created.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getKeyPair(self, var_id):
        """ Retrieve details of a key pair.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/keyPairs/sslServer/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def deleteKeyPair(self, var_id):
        """ Delete a key pair.
        """

        try:
            response = self.session.delete(

                url=self._build_uri("/keyPairs/sslServer/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info('Key Pair deleted.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Resource is in use and cannot be deleted.')
        finally:
            return response

    def exportCsr(self, var_id):
        """ Generate a new certificate signing request (CSR) for this key pair.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/keyPairs/sslServer/{id}/csr"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
        finally:
            return response

    def importCsrResponse(self, var_id, body):
        """ Import a CSR response for this key pair.
        """

        payload = {
            "var_id": var_id,
            "body": body

        }

        try:
            response = self.session.post(
                data=payload,
                url=self._build_uri("/keyPairs/sslServer/{id}/csr"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('CSR Response imported.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def exportPKCS12File(self, var_id, body):
        """ Download the key pair in PKCS12 format.
        """

        payload = {
            "var_id": var_id,
            "body": body

        }

        try:
            response = self.session.post(
                data=payload,
                url=self._build_uri("/keyPairs/sslServer/{id}/pkcs12"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Key Pair downloaded.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def exportCertificateFile(self, var_id):
        """ Download the certificate from a given key pair.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/keyPairs/sslServer/{id}/certificate"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def getSettings(self):
        """ Get the SSL Server Certificate Settings.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/keyPairs/sslServer/settings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
        finally:
            return response

    def updateSettings(self, body):
        """ Update the SSL Server Certificate Settings.
        """

        payload = {
            "body": body

        }

        try:
            response = self.session.put(
                data=payload,
                url=self._build_uri("/keyPairs/sslServer/settings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('SSL Certificate Settings updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

