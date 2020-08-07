import logging
import requests
import os
from requests.exceptions import HTTPError


class _oauth_authServerSettings():
    def __init__(self, endpoint: str) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._oauth_authServerSettings')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getAuthorizationServerSettings(self):
        """ Get the Authorization Server Settings.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/authServerSettings"),
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

    def updateAuthorizationServerSettings(self, body):
        """ Update the Authorization Server Settings.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/oauth/authServerSettings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Authorization Server Settings updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def addCommonScope(self, body):
        """ Add a new common scope.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/oauth/authServerSettings/scopes/commonScopes"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info("Common Scope added.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getCommonScope(self, name):
        """ Get an existing common scope.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/authServerSettings/scopes/commonScopes/{name}"),
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

    def updateCommonScope(self, name, body):
        """ Update an existing common scope.
        """

        payload = {
            "name": name,
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/oauth/authServerSettings/scopes/commonScopes/{name}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Common Scope updated.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def removeCommonScope(self, name):
        """ Remove an existing common scope.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/oauth/authServerSettings/scopes/commonScopes/{name}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info("Common Scope deleted.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def addCommonScopeGroup(self, body):
        """ Create a new common scope group.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/oauth/authServerSettings/scopes/commonScopeGroups"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info("Common Scope Group created.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getCommonScopeGroup(self, name):
        """ Get an existing common scope group.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/authServerSettings/scopes/commonScopeGroups/{name}"),
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

    def updateCommonScopeGroup(self, name, body):
        """ Update an existing common scope group.
        """

        payload = {
            "name": name,
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/oauth/authServerSettings/scopes/commonScopeGroups/{name}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Common Scope Group updated.")
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

    def removeCommonScopeGroup(self, name):
        """ Remove an existing common scope group.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/oauth/authServerSettings/scopes/commonScopeGroups/{name}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info("Common Scope Group deleted.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def addExclusiveScope(self, body):
        """ Add a new exclusive scope.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/oauth/authServerSettings/scopes/exclusiveScopes"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info("Exclusive Scope added.")
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

    def getExclusiveScope(self, name):
        """ Get an existing exclusive scope.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/authServerSettings/scopes/exclusiveScopes/{name}"),
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

    def updateExclusiveScope(self, name, body):
        """ Update an existing exclusive scope.
        """

        payload = {
            "name": name,
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/oauth/authServerSettings/scopes/exclusiveScopes/{name}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Exclusive Scope updated.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def removeExclusiveScope(self, name):
        """ Remove an existing exclusive scope.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/oauth/authServerSettings/scopes/exclusiveScopes/{name}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info("Exclusive Scope deleted.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def addExclusiveScopeGroup(self, body):
        """ Create a new exclusive scope group.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/oauth/authServerSettings/scopes/exclusiveScopeGroups"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info("Exclusive Scope Group created.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getExclusiveScopeGroup(self, name):
        """ Get an existing exclusive scope group.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/authServerSettings/scopes/exclusiveScopeGroups/{name}"),
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

    def updateExclusiveScopeGroups(self, name, body):
        """ Update an existing exclusive scope group.
        """

        payload = {
            "name": name,
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/oauth/authServerSettings/scopes/exclusiveScopeGroups/{name}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Exclusive Scope Group updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def removeExclusiveScopeGroup(self, name):
        """ Remove an existing exclusive scope group.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/oauth/authServerSettings/scopes/exclusiveScopeGroups/{name}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info("Exclusive Scope Group deleted.")
            if response.status_code == 403:
                self.logger.info("PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

