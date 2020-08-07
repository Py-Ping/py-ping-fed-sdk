import logging
import requests
import os
from requests.exceptions import HTTPError


class _authenticationSelectors():
    def __init__(self, endpoint):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._authenticationSelectors')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path):
        return f"{self.endpoint}{path}"

    def getAuthenticationSelectorDescriptors(self):
        """ Get the list of available Authentication Selector descriptors.
        """

        try:
            response = requests.get(

                url=self._build_uri("/authenticationSelectors/descriptors"),
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
                self.logger.info("PingFederate does not have the appropriate IdP/SP role enabled. Operation not available.")
        finally:
            return response.json()

    def getAuthenticationSelectorDescriptorsById(self, id):
        """ Get the description of an Authentication Selector plugin by ID.
        """

        try:
            response = requests.get(

                url=self._build_uri("/authenticationSelectors/descriptors/{id}"),
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
                self.logger.info("PingFederate does not have the appropriate IdP/SP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def getAuthenticationSelectors(self, page, numberPerPage, filter):
        """ Get the list of configured Authentication Selector instances.
        """

        try:
            response = requests.get(

                url=self._build_uri("/authenticationSelectors"),
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
                self.logger.info("PingFederate does not have the appropriate IdP/SP role enabled. Operation not available.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def createAuthenticationSelector(self, body):
        """ Create a new authentication selector instance.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/authenticationSelectors"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info("Authentication selector created.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have the appropriate IdP/SP role enabled. Operation not available.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getAuthenticationSelector(self, id):
        """ Get an Authentication Selector instance by ID.
        """

        try:
            response = requests.get(

                url=self._build_uri("/authenticationSelectors/{id}"),
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
                self.logger.info("PingFederate does not have the appropriate IdP/SP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def updateAuthenticationSelector(self, id, body):
        """ Update an authentication selector instance.
        """

        payload = {
            "id": id,
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/authenticationSelectors/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Authentication selector updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have the appropriate IdP/SP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def deleteAuthenticationSelector(self, id):
        """ Delete an Authentication Selector instance.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/authenticationSelectors/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info("Authentication selector deleted.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its IdP role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Resource is in use and cannot be deleted.")
        finally:
            return response.json()

