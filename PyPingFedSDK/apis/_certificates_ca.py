import os
import logging
from requests import Session
from requests.exceptions import HTTPError


class _certificates_ca():
    def __init__(self, endpoint:str, session:Session) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._certificates_ca')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getTrustedCAs(self):
        """ Get list of trusted certificate authorities.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/certificates/ca"),
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

    def getTrustedCert(self, var_id):
        """ Retrieve details of a trusted certificate authority.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/certificates/ca/{id}"),
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

    def deleteTrustedCA(self, var_id):
        """ Delete a trusted certificate authority.
        """

        try:
            response = self.session.delete(

                url=self._build_uri("/certificates/ca/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info('Certitifcate Authority deleted.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def importTrustedCA(self, body):
        """ Import a new trusted certificate authority.
        """

        payload = {
            "body": body

        }

        try:
            response = self.session.post(
                data=payload,
                url=self._build_uri("/certificates/ca/import"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info('Certificate Authority imported.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def exportCertificateFile(self, var_id):
        """ Download the certificate from a given trusted certificate authority.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/certificates/ca/{id}/file"),
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

