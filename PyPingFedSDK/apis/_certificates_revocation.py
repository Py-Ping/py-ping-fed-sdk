import logging
import requests
import os
from requests.exceptions import HTTPError


class _certificates_revocation():
    def __init__(self, endpoint):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._certificates_revocation')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path):
        return f"{self.endpoint}{path}"

    def getRevocationSettings(self):
        """ Get certificate revocation settings.
        """

        try:
            response = requests.get(

                url=self._build_uri("/certificates/revocation/settings"),
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

    def updateRevocationSettings(self, body):
        """ Update certificate revocation settings.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.put(
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
                self.logger.info("Certificate revocation settings updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getOcspCertificates(self):
        """ Get the list of available OCSP responder signature verification certificates.
        """

        try:
            response = requests.get(

                url=self._build_uri("/certificates/revocation/ocspCertificates"),
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

    def importOcspCertificate(self, body):
        """ Import an OCSP responder signature verification certificate.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.post(
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
                self.logger.info("OCSP responder signature verification certificate imported.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getOcspCertificateById(self, id):
        """ Get an OCSP responder signature verification certificate by ID.
        """

        try:
            response = requests.get(

                url=self._build_uri("/certificates/revocation/ocspCertificates/{id}"),
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

    def deleteOcspCertificateById(self, id):
        """ Delete an OCSP responder signature verification certificate by ID.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/certificates/revocation/ocspCertificates/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info("OCSP responder signature verification certificate deleted.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Resource is in use and cannot be deleted.")
        finally:
            return response.json()

