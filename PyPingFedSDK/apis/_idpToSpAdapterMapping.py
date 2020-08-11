import os
import logging
from requests import Session
from requests.exceptions import HTTPError


class _idpToSpAdapterMapping():
    def __init__(self, endpoint:str, session:Session) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._idpToSpAdapterMapping')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getIdpToSpAdapterMappings(self):
        """ Get list of IdP-to-SP Adapter Mappings.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/idpToSpAdapterMapping"),
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
                self.logger.info('PingFederate does not have the appropriate IdP/SP role enabled. Operation not available.')
        finally:
            return response

    def createIdpToSpAdapterMapping(self, body, X-BypassExternalValidation):
        """ Create a new IdP-to-SP Adapter mapping.
        """

        payload = {
            "body": body,
            "X-BypassExternalValidation": X-BypassExternalValidation

        }

        try:
            response = self.session.post(
                data=payload,
                url=self._build_uri("/idpToSpAdapterMapping"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info('IdP-to-SP adapter mapping created.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getIdpToSpAdapterMappingsById(self, var_id):
        """ Get an IdP-to-SP Adapter Mapping.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/idpToSpAdapterMapping/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def updateIdpToSpAdapterMapping(self, var_id, body, X-BypassExternalValidation):
        """ Update the specified IdP-to-SP Adapter mapping.
        """

        payload = {
            "var_id": var_id,
            "body": body,
            "X-BypassExternalValidation": X-BypassExternalValidation

        }

        try:
            response = self.session.put(
                data=payload,
                url=self._build_uri("/idpToSpAdapterMapping/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('IdP-to-SP adapter mapping updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def deleteIdpToSpAdapterMappingsById(self, var_id):
        """ Delete an Adapter to Adapter Mapping.
        """

        try:
            response = self.session.delete(

                url=self._build_uri("/idpToSpAdapterMapping/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info('IdP-to-SP adapter mapping deleted.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

