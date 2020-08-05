import logging
import requests

class _idp_adapters():
    def __init__(self, endpoint):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._idp_adapters')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path):
        return f"{self.endpoint}{path}"

    def getIdpAdapterDescriptors(self):
        """ Get the list of available IdP adapter descriptors.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/idp/adapters/descriptors"),
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
                self.logger.info('PingFederate does not have its IdP role enabled. Operation not available.')
        finally:
            return response

    def getIdpAdapterDescriptorsById(self, id):
        """ Get the description of an IdP adapter plugin by ID.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/idp/adapters/descriptors/{id}"),
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
                self.logger.info('PingFederate does not have its IdP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def getIdpAdapters(self, page, numberPerPage, filter):
        """ Get the list of configured IdP adapter instances.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/idp/adapters"),
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
                self.logger.info('PingFederate does not have its IdP role enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def createIdpAdapter(self, body, X-BypassExternalValidation):
        """ Create a new IdP adapter instance.
        """
        
        payload = {
            "body": body"X-BypassExternalValidation": X-BypassExternalValidation
        }
        
        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/idp/adapters"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 201:
                self.logger.info('Adapter created.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its IdP role enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getIdpAdapter(self, id):
        """ Find an IdP adapter instance by ID.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/idp/adapters/{id}"),
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
                self.logger.info('PingFederate does not have its IdP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def updateIdpAdapter(self, id, body, X-BypassExternalValidation):
        """ Update an IdP adapter instance.
        """
        
        payload = {
            "id": id"body": body"X-BypassExternalValidation": X-BypassExternalValidation
        }
        
        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/idp/adapters/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('Adapter updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its IdP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def deleteIdpAdapter(self, id):
        """ Delete an IdP adapter instance.
        """
        
        try:
            response = requests.delete(
                
                url=self._build_uri("/idp/adapters/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 204:
                self.logger.info('Adapter deleted.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its IdP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Resource is in use and cannot be deleted.')
        finally:
            return response

    def getActions(self, id):
        """ List the actions for an IdP adapter instance.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/idp/adapters/{id}/actions"),
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
                self.logger.info('PingFederate does not have its IdP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def getAction(self, id, actionId):
        """ Find an IdP adapter instance's action by ID.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/idp/adapters/{id}/actions/{actionId}"),
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
                self.logger.info('PingFederate does not have its IdP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def invokeAction(self, id, actionId):
        """ Invokes an action for an IdP adapter instance.
        """
        
        payload = {
            "id": id"actionId": actionId
        }
        
        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/idp/adapters/{id}/actions/{actionId}/invokeAction"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('Action invoked on adapter.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its IdP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

