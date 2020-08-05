import logging
import requests

class _dataStores():
    def __init__(self, endpoint):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._dataStores')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path):
        return f"{self.endpoint}{path}"

    def getCustomDataStoreDescriptors(self):
        """ Get the list of available custom data store descriptors.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/dataStores/descriptors"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
        finally:
            return response

    def getCustomDataStoreDescriptor(self, id):
        """ Get the description of a custom data store plugin by ID.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/dataStores/descriptors/{id}"),
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

    def getDataStores(self):
        """ Get list of data stores.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/dataStores"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
        finally:
            return response

    def createDataStore(self, body, X-BypassExternalValidation):
        """ Create a new data store.
        """
        
        payload = {
            "body": body"X-BypassExternalValidation": X-BypassExternalValidation
        }
        
        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/dataStores"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 201:
                self.logger.info('Data store created.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getDataStore(self, id):
        """ Find data store by ID.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/dataStores/{id}"),
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

    def updateDataStore(self, id, body, X-BypassExternalValidation):
        """ Update a data store.
        """
        
        payload = {
            "id": id"body": body"X-BypassExternalValidation": X-BypassExternalValidation
        }
        
        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/dataStores/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('Data store updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def deleteDataStore(self, id):
        """ Delete a data store.
        """
        
        try:
            response = requests.delete(
                
                url=self._build_uri("/dataStores/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 204:
                self.logger.info('Data store deleted.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Resource is in use and cannot be deleted.')
        finally:
            return response

    def getActions(self, id):
        """ List the actions for a data store instance.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/dataStores/{id}/actions"),
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

    def getAction(self, id, actionId):
        """ Find a data store instance's action by ID.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/dataStores/{id}/actions/{actionId}"),
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

    def invokeAction(self, id, actionId):
        """ Invokes an action for a data source instance.
        """
        
        payload = {
            "id": id"actionId": actionId
        }
        
        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/dataStores/{id}/actions/{actionId}/invokeAction"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('Action invoked on Data store.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

