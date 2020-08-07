import logging
import requests
import os
from requests.exceptions import HTTPError


class _incomingProxySettings():
<<<<<<< HEAD
    def __init__(self, endpoint: str) -> None:
=======
    def __init__(self, endpoint):
>>>>>>> Baseline Sphinx generation
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._incomingProxySettings')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

<<<<<<< HEAD
    def _build_uri(self, path: str):
=======
    def _build_uri(self, path):
>>>>>>> Baseline Sphinx generation
        return f"{self.endpoint}{path}"

    def getIncomingProxySettings(self):
        """ Get incoming proxy settings.
        """

        try:
            response = requests.get(

                url=self._build_uri("/incomingProxySettings"),
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

    def updateIncomingProxySettings(self, body):
        """ Update incoming proxy settings.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/incomingProxySettings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
<<<<<<< HEAD
                self.logger.info('Incoming proxy settings updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response
=======
                self.logger.info("Incoming proxy settings updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()
>>>>>>> Baseline Sphinx generation

