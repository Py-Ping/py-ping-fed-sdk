import logging
import requests
import os
from requests.exceptions import HTTPError


class _configStore():
    def __init__(self, endpoint):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._configStore')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path):
        return f"{self.endpoint}{path}"

    def getSetting(self, bundle, id):
        """ Get a single setting from a bundle.
        """

        try:
            response = requests.get(

                url=self._build_uri("/configStore/{bundle}/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
            if response.status_code == 403:
                self.logger.info('The specified configuration bundle is unavailable.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def updateSetting(self, bundle, id, body):
        """ Update a setting.
        """

        payload = {
            "bundle": bundle,
            "id": id,
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/configStore/{bundle}/{id}"),
                headers={'Accept': '['application/json']'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Configuration setting updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('The specified configuration bundle is unavailable.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def deleteSetting(self, bundle, id):
        """ Delete a setting.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/configStore/{bundle}/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info('Configuration setting deleted.')
            if response.status_code == 403:
                self.logger.info('The specified configuration bundle is unavailable.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def getSettings(self, bundle):
        """ Get all settings from a bundle.
        """

        try:
            response = requests.get(

                url=self._build_uri("/configStore/{bundle}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
            if response.status_code == 403:
                self.logger.info('The specified configuration bundle is unavailable.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

