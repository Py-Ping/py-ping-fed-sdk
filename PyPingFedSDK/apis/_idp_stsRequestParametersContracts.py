import logging
import requests
import os
from requests.exceptions import HTTPError


class _idp_stsRequestParametersContracts():
    def __init__(self, endpoint):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._idp_stsRequestParametersContracts')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path):
        return f"{self.endpoint}{path}"

    def getStsRequestParamContracts(self):
        """ Get the list of STS Request Parameters Contracts.
        """

        try:
            response = requests.get(

                url=self._build_uri("/idp/stsRequestParametersContracts"),
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
                self.logger.info("PingFederate does not have its IdP role enabled. Operation not available.")
        finally:
            return response.json()

    def createStsRequestParamContract(self, body):
        """ Create a new STS Request Parameters Contract.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/idp/stsRequestParametersContracts"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info("STS Request Parameters Contract created.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its IdP role enabled. Operation not available.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getStsRequestParamContractById(self, id):
        """ Get a STS Request Parameters Contract.
        """

        try:
            response = requests.get(

                url=self._build_uri("/idp/stsRequestParametersContracts/{id}"),
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
                self.logger.info("PingFederate does not have its IdP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def updateStsRequestParamContractById(self, id, body):
        """ Update a STS Request Parameters Contract.
        """

        payload = {
            "id": id,
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/idp/stsRequestParametersContracts/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("STS Request Parameters Contract updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its IdP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def deleteStsRequestParamContractById(self, id):
        """ Delete a STS Request Parameters Contract.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/idp/stsRequestParametersContracts/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info("STS Request Parameters Contract deleted.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its IdP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

