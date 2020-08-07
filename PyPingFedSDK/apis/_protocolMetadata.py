import logging
import requests
import os
from requests.exceptions import HTTPError


class _protocolMetadata():
<<<<<<< HEAD
    def __init__(self, endpoint: str) -> None:
=======
    def __init__(self, endpoint):
>>>>>>> Baseline Sphinx generation
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._protocolMetadata')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

<<<<<<< HEAD
    def _build_uri(self, path: str):
=======
    def _build_uri(self, path):
>>>>>>> Baseline Sphinx generation
        return f"{self.endpoint}{path}"

    def getLifetimeSettings(self):
        """ Get metadata cache duration and reload delay for automated reloading.
        """

        try:
            response = requests.get(

                url=self._build_uri("/protocolMetadata/lifetimeSettings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
<<<<<<< HEAD
                self.logger.info('Success.')
        finally:
            return response
=======
                self.logger.info("Success.")
        finally:
            return response.json()
>>>>>>> Baseline Sphinx generation

    def updateLifetimeSettings(self, body):
        """ Update metadata cache duration and reload delay for automated reloading.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/protocolMetadata/lifetimeSettings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
<<<<<<< HEAD
                self.logger.info('Metadata lifetime settings updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response
=======
                self.logger.info("Metadata lifetime settings updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()
>>>>>>> Baseline Sphinx generation

    def getSigningSettings(self):
        """ Get the certificate ID and algorithm used for metadata signing.
        """

        try:
            response = requests.get(

                url=self._build_uri("/protocolMetadata/signingSettings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
<<<<<<< HEAD
                self.logger.info('Success.')
        finally:
            return response
=======
                self.logger.info("Success.")
        finally:
            return response.json()
>>>>>>> Baseline Sphinx generation

    def updateSigningSettings(self, body):
        """ Update the certificate and algorithm for metadata signing.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/protocolMetadata/signingSettings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
<<<<<<< HEAD
                self.logger.info('Metadata signing settings updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response
=======
                self.logger.info("Metadata signing settings updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()
>>>>>>> Baseline Sphinx generation

