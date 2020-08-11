import logging
import requests
import os
from requests.exceptions import HTTPError


class _oauth_cibaServerPolicy():
    def __init__(self, endpoint: str) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._oauth_cibaServerPolicy')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getSettings(self):
        """ Get general ciba server request policy settings.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/cibaServerPolicy/settings"),
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
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
        finally:
            return response.json()

    def updateSettings(self, body, XBypassExternalValidation):
        """ Update general ciba server request policy settings.
        """

        payload = {
            "body": body,
            "XBypassExternalValidation": XBypassExternalValidation

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/oauth/cibaServerPolicy/settings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Settings updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getPolicies(self):
        """ Get list of request policies.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/cibaServerPolicy/requestPolicies"),
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
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
        finally:
            return response.json()

    def createPolicy(self, body, XBypassExternalValidation):
        """ Create a new request policy.
        """

        payload = {
            "body": body,
            "XBypassExternalValidation": XBypassExternalValidation

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/oauth/cibaServerPolicy/requestPolicies"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info("Request Handling Policy created.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getPolicy(self, var_id):
        """ Find request policy by ID.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/cibaServerPolicy/requestPolicies/{id}"),
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
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def updatePolicy(self, var_id, body, XBypassExternalValidation):
        """ Update a request policy.
        """

        payload = {
            "var_id": var_id,
            "body": body,
            "XBypassExternalValidation": XBypassExternalValidation

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/oauth/cibaServerPolicy/requestPolicies/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Request Handling Policy updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def deletePolicy(self, var_id):
        """ Delete a request policy.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/oauth/cibaServerPolicy/requestPolicies/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info("Request Handling Policy deleted.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

