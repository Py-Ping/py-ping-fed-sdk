import os
import logging
from requests import Session
from requests.exceptions import HTTPError


class _oauth_tokenExchange_tokenGeneratorMappings():
    def __init__(self, endpoint:str, session:Session) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._oauth_tokenExchange_tokenGeneratorMappings')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getTokenGeneratorMappings(self):
        """ Get the list of Token Exchange Processor policy to Token Generator Mappings.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/oauth/tokenExchange/tokenGeneratorMappings"),
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
                self.logger.info('PingFederate does not have the IdP, SP and OAuth roles enabled. Operation not available.')
        finally:
            return response

    def createTokenGeneratorMapping(self, body, X-BypassExternalValidation):
        """ Create a new Token Exchange Processor policy to Token Generator Mapping.
        """

        payload = {
            "body": body,
            "X-BypassExternalValidation": X-BypassExternalValidation

        }

        try:
            response = self.session.post(
                data=payload,
                url=self._build_uri("/oauth/tokenExchange/tokenGeneratorMappings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info('Token Exchange Processor policy to Token Generator mapping created.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the IdP, SP and OAuth roles enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getTokenGeneratorMappingById(self, var_id):
        """ Get a Token Exchange Processor policy to Token Generator Mapping.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/oauth/tokenExchange/tokenGeneratorMappings/{id}"),
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
                self.logger.info('PingFederate does not have the IdP, SP and OAuth roles enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def updateTokenGeneratorMappingById(self, var_id, body, X-BypassExternalValidation):
        """ Update a Token Exchange Processor policy to Token Generator Mapping.
        """

        payload = {
            "var_id": var_id,
            "body": body,
            "X-BypassExternalValidation": X-BypassExternalValidation

        }

        try:
            response = self.session.put(
                data=payload,
                url=self._build_uri("/oauth/tokenExchange/tokenGeneratorMappings/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Token Exchange Processor policy to Token Generator mapping updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the IdP, SP and OAuth roles enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def deleteTokenGeneratorMappingById(self, var_id):
        """ Delete a Token Exchange Processor policy to Token Generator Mapping.
        """

        try:
            response = self.session.delete(

                url=self._build_uri("/oauth/tokenExchange/tokenGeneratorMappings/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info('Token Exchange Processor policy to Token Generator mapping deleted.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the IdP, SP and OAuth roles enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

