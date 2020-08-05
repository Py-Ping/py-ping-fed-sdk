import logging
import requests
import os
from requests.exceptions import HTTPError


class _oauth_clientRegistrationPolicies():
    def __init__(self, endpoint):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._oauth_clientRegistrationPolicies')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path):
        return f"{self.endpoint}{path}"

    def getDynamicClientRegistrationDescriptors(self):
        """ Get the list of available client registration policy plugin descriptors.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/clientRegistrationPolicies/descriptors"),
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
                self.logger.info('PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.')
        finally:
            return response

    def getDynamicClientRegistrationDescriptor(self, id):
        """ Get the description of a client registration policy plugin descriptor.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/clientRegistrationPolicies/descriptors/{id}"),
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
                self.logger.info('PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def getDynamicClientRegistrationPolicies(self):
        """ Get a list of client registration policy plugin instances.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/clientRegistrationPolicies"),
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
                self.logger.info('PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.')
        finally:
            return response

    def createDynamicClientRegistrationPolicy(self, body):
        """ Create a client registration policy plugin instance.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/oauth/clientRegistrationPolicies"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info('Client Registration Policy plugin created.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getDynamicClientRegistrationPolicy(self, id):
        """ Get a specific client registration policy plugin instance.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/clientRegistrationPolicies/{id}"),
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
                self.logger.info('PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def updateDynamicClientRegistrationPolicy(self, id, body):
        """ Update a client registration policy plugin instance.
        """

        payload = {
            "id": id,
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/oauth/clientRegistrationPolicies/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Client Registration Policy plugin updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def deleteDynamicClientRegistrationPolicy(self, id):
        """ Delete a client registration policy plugin instance.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/oauth/clientRegistrationPolicies/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info('Client Registration Policy plugin deleted.')
            if response.status_code == 403:
                self.logger.info('The operation is not permitted, based on the current configuration of the server.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

