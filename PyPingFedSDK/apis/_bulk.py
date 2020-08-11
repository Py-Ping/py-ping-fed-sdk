import logging
import requests
import os
from requests.exceptions import HTTPError


class _bulk():
    def __init__(self, endpoint: str) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._bulk')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def exportConfiguration(self, includeExternalResources):
        """ Export all API resources to a JSON file.
        """

        try:
            response = requests.get(

                url=self._build_uri("/bulk/export"),
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
                self.logger.info("The current configuration cannot be bulk exported.")
        finally:
            return response.json()

    def importConfiguration(self, failFast, body, XBypassExternalValidation):
        """ Import configuration for a PingFederate deployment from a JSON file.
        """

        payload = {
            "failFast": failFast,
            "body": body,
            "XBypassExternalValidation": XBypassExternalValidation

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/bulk/import"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

