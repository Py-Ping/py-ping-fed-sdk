import os
import logging
from requests import Session
from requests.exceptions import HTTPError


class _certificates_revocation():
    def __init__(self, endpoint:str, session:Session) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._certificates_revocation')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getRevocationSettings(self):
        """ Get certificate revocation settings.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/certificates/revocation/settings"),
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

    def updateRevocationSettings(self, body):
        """ Update certificate revocation settings.
        """

        payload = {
            "body": body

        }

        try:
            response = self.session.put(
                data=payload,
                url=self._build_uri("/certificates/revocation/settings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Certificate revocation settings updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getOcspCertificates(self):
        """ Get the list of available OCSP responder signature verification certificates.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/certificates/revocation/ocspCertificates"),
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

    def importOcspCertificate(self, body):
        """ Import an OCSP responder signature verification certificate.
        """

        payload = {
            "body": body

        }

        try:
            response = self.session.post(
                data=payload,
                url=self._build_uri("/certificates/revocation/ocspCertificates"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info('OCSP responder signature verification certificate imported.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getOcspCertificateById(self, var_id):
        """ Get an OCSP responder signature verification certificate by ID.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/certificates/revocation/ocspCertificates/{id}"),
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

    def deleteOcspCertificateById(self, var_id):
        """ Delete an OCSP responder signature verification certificate by ID.
        """

        try:
            response = self.session.delete(

                url=self._build_uri("/certificates/revocation/ocspCertificates/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info('OCSP responder signature verification certificate deleted.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Resource is in use and cannot be deleted.')
        finally:
            return response

