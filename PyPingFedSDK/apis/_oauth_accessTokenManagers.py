import logging
import requests

class _oauth_accessTokenManagers():
    def __init__(self, endpoint):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._oauth_accessTokenManagers')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path):
        return f"{self.endpoint}{path}"

    def getSettings(self):
        """ Get general access token management settings.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/oauth/accessTokenManagers/settings"),
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

    def updateSettings(self, body):
        """ Update general access token management settings.
        """
        
        payload = {
            "body": body
        }
        
        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/oauth/accessTokenManagers/settings"),
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
                self.logger.info('PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getTokenManagerDescriptors(self):
        """ Get the list of available token management plugin descriptors.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/oauth/accessTokenManagers/descriptors"),
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

    def getTokenManagerDescriptor(self, id):
        """ Get the description of a token management plugin descriptor.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/oauth/accessTokenManagers/descriptors/{id}"),
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

    def getTokenManagers(self):
        """ Get a list of all token management plugin instances.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/oauth/accessTokenManagers"),
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

    def createTokenManager(self, body):
        """ Create a token management plugin instance.
        """
        
        payload = {
            "body": body
        }
        
        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/oauth/accessTokenManagers"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 201:
                self.logger.info('Access Token Management instance created.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its OAuth 2.0 authorization server role enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getTokenManager(self, id):
        """ Get a specific token management plugin instance.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/oauth/accessTokenManagers/{id}"),
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

    def updateTokenManager(self, id, body):
        """ Update a token management plugin instance.
        """
        
        payload = {
            "id": id"body": body
        }
        
        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/oauth/accessTokenManagers/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('Access Token Management instance updated.')
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

    def deleteTokenManager(self, id):
        """ Delete a token management plugin instance.
        """
        
        try:
            response = requests.delete(
                
                url=self._build_uri("/oauth/accessTokenManagers/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 204:
                self.logger.info('Access token management instance deleted.')
            if response.status_code == 403:
                self.logger.info('The operation is not permitted, based on the current configuration of the server.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

