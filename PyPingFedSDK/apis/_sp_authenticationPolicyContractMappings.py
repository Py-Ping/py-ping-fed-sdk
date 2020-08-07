import logging
import requests
import os
from requests.exceptions import HTTPError


class _sp_authenticationPolicyContractMappings():
    def __init__(self, endpoint: str) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._sp_authenticationPolicyContractMappings')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getApcToSpAdapterMappings(self):
        """ Get the list of APC-to-SP Adapter Mappings.
        """

        try:
            response = requests.get(

                url=self._build_uri("/sp/authenticationPolicyContractMappings"),
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
                self.logger.info("PingFederate does not have its SP role enabled. Operation not available.")
        finally:
            return response.json()

    def createApcToSpAdapterMapping(self, body, XBypassExternalValidation):
        """ Create a new APC-to-SP Adapter Mapping.
        """

        payload = {
            "body": body,
            "X-BypassExternalValidation": X-BypassExternalValidation

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/sp/authenticationPolicyContractMappings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info("Authentication policy contract-to-SP adapter mapping created.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its SP role enabled. Operation not available.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getApcToSpAdapterMappingById(self, var_id):
        """ Get an APC-to-SP Adapter Mapping.
        """

        try:
            response = requests.get(

                url=self._build_uri("/sp/authenticationPolicyContractMappings/{id}"),
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
                self.logger.info("PingFederate does not have its SP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

<<<<<<< HEAD
    def updateApcToSpAdapterMappingById(self, var_id, body, X-BypassExternalValidation):
=======
    def updateApcToSpAdapterMappingById(self, id, body, XBypassExternalValidation):
>>>>>>> Baseline Sphinx generation
        """ Update an APC-to-SP Adapter Mapping.
        """

        payload = {
            "var_id": var_id,
            "body": body,
            "X-BypassExternalValidation": X-BypassExternalValidation

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/sp/authenticationPolicyContractMappings/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Authentication policy contract-to-SP adapter mapping updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its SP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def deleteApcToSpAdapterMappingById(self, var_id):
        """ Delete an APC-to-SP Adapter Mapping.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/sp/authenticationPolicyContractMappings/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info("Authentication policy contract-to-SP adapter mapping deleted.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its SP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

