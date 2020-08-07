import logging
import requests
import os
from requests.exceptions import HTTPError


class _oauth_openIdConnect():
    def __init__(self, endpoint):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._oauth_openIdConnect')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path):
        return f"{self.endpoint}{path}"

    def getSettings(self):
        """ Get the OpenID Connect Settings.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/openIdConnect/settings"),
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
                self.logger.info("PingFederate does not have its OpenID connect protocol enabled. Operation not available.")
        finally:
            return response.json()

    def updateSettings(self, body):
        """ Set the OpenID Connect Settings.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/oauth/openIdConnect/settings"),
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
                self.logger.info("PingFederate does not have its OpenID connect protocol enabled. Operation not available.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getPolicies(self):
        """ Get list of OpenID Connect Policies.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/openIdConnect/policies"),
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
                self.logger.info("PingFederate does not have its OpenID connect protocol enabled. Operation not available.")
        finally:
            return response.json()

    def createPolicy(self, body, XBypassExternalValidation):
        """ Create a new OpenID Connect Policy.
        """

        payload = {
            "body": body,
            "X-BypassExternalValidation": X-BypassExternalValidation

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/oauth/openIdConnect/policies"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info("Policy created.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OpenID connect protocol enabled. Operation not available.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getPolicy(self, id):
        """ Find OpenID Connect Policy by ID.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/openIdConnect/policies/{id}"),
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
                self.logger.info("PingFederate does not have its OpenID connect protocol enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def updatePolicy(self, id, body, XBypassExternalValidation):
        """ Update an OpenID Connect Policy.
        """

        payload = {
            "id": id,
            "body": body,
            "X-BypassExternalValidation": X-BypassExternalValidation

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/oauth/openIdConnect/policies/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Policy updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OpenID connect protocol enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def deletePolicy(self, id):
        """ Delete an OpenID Connect Policy.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/oauth/openIdConnect/policies/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info("Policy deleted.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OpenID connect protocol enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

