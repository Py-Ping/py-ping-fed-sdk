import logging
import requests
import os
from requests.exceptions import HTTPError


class _oauth_tokenExchange_processor():
    def __init__(self, endpoint):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._oauth_tokenExchange_processor')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path):
        return f"{self.endpoint}{path}"

    def getSettings(self):
        """ Get general OAuth 2.0 Token Exchange Processor settings.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/tokenExchange/processor/settings"),
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
                self.logger.info('PingFederate does not have the IdP and OAuth roles enabled. Operation not available.')
        finally:
            return response

    def updateSettings(self, body, bypassExternalValidation):
        """ Update general OAuth 2.0 Token Exchange Processor settings.
        """

        payload = {
            "body": body,
            "bypassExternalValidation": bypassExternalValidation

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/oauth/tokenExchange/processor/settings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Settings updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the IdP and OAuth roles enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getPolicies(self):
        """ Get list of OAuth 2.0 Token Exchange Processor policies.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/tokenExchange/processor/policies"),
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
                self.logger.info('PingFederate does not have the IdP and OAuth roles enabled. Operation not available.')
        finally:
            return response

    def createPolicy(self, body, bypassExternalValidation):
        """ Create a new OAuth 2.0 Token Exchange Processor policy.
        """

        payload = {
            "body": body,
            "bypassExternalValidation": bypassExternalValidation

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/oauth/tokenExchange/processor/policies"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info('Token Exchange Processor Policy created.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the IdP and OAuth roles enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getPolicy(self, id):
        """ Find an OAuth 2.0 Token Exchange Processor policy by ID.
        """

        try:
            response = requests.get(

                url=self._build_uri("/oauth/tokenExchange/processor/policies/{id}"),
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
                self.logger.info('PingFederate does not have the IdP and OAuth roles enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def updatePolicy(self, id, body, bypassExternalValidation):
        """ Update an OAuth 2.0 Token Exchange Processor policy.
        """

        payload = {
            "id": id,
            "body": body,
            "bypassExternalValidation": bypassExternalValidation

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/oauth/tokenExchange/processor/policies/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Token Exchange Processor Policy updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the IdP and OAuth roles enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def deletePolicy(self, id):
        """ Delete an OAuth 2.0 Token Exchange Processor policy.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/oauth/tokenExchange/processor/policies/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info('Token Exchange Processor Policy deleted.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the IdP and OAuth roles enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

