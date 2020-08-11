import os
import logging
from requests import Session
from requests.exceptions import HTTPError


class _oauth_authenticationPolicyContractMappings():
    def __init__(self, endpoint:str, session:Session) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._oauth_authenticationPolicyContractMappings')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getApcMappings(self):
        """ Get the list of authentication policy contract to persistent grant mappings.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/oauth/authenticationPolicyContractMappings"),
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

    def createApcMapping(self, body, X-BypassExternalValidation):
        """ Create a new authentication policy contract to persistent grant mapping.
        """

        payload = {
            "body": body,
            "X-BypassExternalValidation": X-BypassExternalValidation

        }

        try:
            response = self.session.post(
                data=payload,
                url=self._build_uri("/oauth/authenticationPolicyContractMappings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info('Authentication policy contract to persistent grant mapping created.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the IdP and OAuth roles enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getApcMapping(self, var_id):
        """ Find the authentication policy contract to persistent grant mapping by ID.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/oauth/authenticationPolicyContractMappings/{id}"),
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

    def updateApcMapping(self, var_id, body, X-BypassExternalValidation):
        """ Update an authentication policy contract to persistent grant mapping.
        """

        payload = {
            "var_id": var_id,
            "body": body,
            "X-BypassExternalValidation": X-BypassExternalValidation

        }

        try:
            response = self.session.put(
                data=payload,
                url=self._build_uri("/oauth/authenticationPolicyContractMappings/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Authentication policy contract to persistent grant mapping updated.')
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

    def deleteApcMapping(self, var_id):
        """ Delete an authentication policy contract to persistent grant mapping.
        """

        try:
            response = self.session.delete(

                url=self._build_uri("/oauth/authenticationPolicyContractMappings/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info('Authentication policy contract to persistent grant mapping deleted.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the IdP and OAuth roles enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

