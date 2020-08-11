import os
import logging
from requests import Session
from requests.exceptions import HTTPError


class _oauth_openIdConnect():
    def __init__(self, endpoint:str, session:Session) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._oauth_openIdConnect')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getSettings(self):
        """ Get the OpenID Connect Settings.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/oauth/openIdConnect/settings"),
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
                self.logger.info('PingFederate does not have its OpenID connect protocol enabled. Operation not available.')
        finally:
            return response

    def updateSettings(self, body):
        """ Set the OpenID Connect Settings.
        """

        payload = {
            "body": body

        }

        try:
            response = self.session.put(
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
                self.logger.info('Settings updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its OpenID connect protocol enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getPolicies(self):
        """ Get list of OpenID Connect Policies.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/oauth/openIdConnect/policies"),
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
                self.logger.info('PingFederate does not have its OpenID connect protocol enabled. Operation not available.')
        finally:
            return response

    def createPolicy(self, body, X-BypassExternalValidation):
        """ Create a new OpenID Connect Policy.
        """

        payload = {
            "body": body,
            "X-BypassExternalValidation": X-BypassExternalValidation

        }

        try:
            response = self.session.post(
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
                self.logger.info('Policy created.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its OpenID connect protocol enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getPolicy(self, var_id):
        """ Find OpenID Connect Policy by ID.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/oauth/openIdConnect/policies/{id}"),
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
                self.logger.info('PingFederate does not have its OpenID connect protocol enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def updatePolicy(self, var_id, body, X-BypassExternalValidation):
        """ Update an OpenID Connect Policy.
        """

        payload = {
            "var_id": var_id,
            "body": body,
            "X-BypassExternalValidation": X-BypassExternalValidation

        }

        try:
            response = self.session.put(
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
                self.logger.info('Policy updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its OpenID connect protocol enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def deletePolicy(self, var_id):
        """ Delete an OpenID Connect Policy.
        """

        try:
            response = self.session.delete(

                url=self._build_uri("/oauth/openIdConnect/policies/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info('Policy deleted.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its OpenID connect protocol enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

