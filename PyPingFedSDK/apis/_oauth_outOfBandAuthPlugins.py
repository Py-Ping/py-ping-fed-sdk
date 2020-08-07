import logging
import requests
import os
from requests.exceptions import HTTPError


class _oauth_outOfBandAuthPlugins():
    def __init__(self, endpoint: str) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._oauth_outOfBandAuthPlugins')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getOOBAuthPluginDescriptors(self):
        """ Get the list of available Out of Band authenticator plugin descriptors.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/outOfBandAuthPlugins/descriptors"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
        finally:
            return response.json()

    def getOOBAuthPluginDescriptor(self, var_id):
        """ Get the descriptor of an Out of Band authenticator plugin.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/outOfBandAuthPlugins/descriptors/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def getOOBAuthenticators(self):
        """ Get a list of Out of Band authenticator plugin instances.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/outOfBandAuthPlugins"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
        finally:
            return response.json()

    def createOOBAuthenticator(self, body):
        """ Create an Out of Band authenticator plugin instance.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/oauth/outOfBandAuthPlugins"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info("Out of Band Authenticator created.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getOOBAuthenticator(self, var_id):
        """ Get a specific Out of Band authenticator plugin instance.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/outOfBandAuthPlugins/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def updateOOBAuthenticator(self, var_id, body):
        """ Update an Out of Band authenticator plugin instance.
        """

        payload = {
            "var_id": var_id,
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/oauth/outOfBandAuthPlugins/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Out of Band Authenticator updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def deleteOOBAuthenticator(self, var_id):
        """ Delete an Out of Band authenticator plugin instance.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/oauth/outOfBandAuthPlugins/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info("Out of Band Authenticator deleted.")
            if response.status_code == 403:
                self.logger.info("The operation is not permitted, based on the current configuration of the server.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def getActions(self, var_id):
        """ List of actions for an Out of Band authenticator plugin instance.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/outOfBandAuthPlugins/{id}/actions"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def getAction(self, var_id, actionId):
        """ Find an Out of Band authenticator plugin instance's action by ID.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/outOfBandAuthPlugins/{id}/actions/{actionId}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def invokeAction(self, var_id, actionId):
        """ Invokes an action for Out of Band authenticator plugin instance.
        """

        payload = {
            "var_id": var_id,
            "actionId": actionId

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/oauth/outOfBandAuthPlugins/{id}/actions/{actionId}/invokeAction"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Action invoked on Out of Band authenticator.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

