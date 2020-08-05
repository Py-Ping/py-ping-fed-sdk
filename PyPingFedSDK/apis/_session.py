import logging
import requests

class _session():
    def __init__(self, endpoint):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._session')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path):
        return f"{self.endpoint}{path}"

    def getSessionSettings(self):
        """ Get general session management settings.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/session/settings"),
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

    def updateSessionSettings(self, body):
        """ Update general session management settings.
        """
        
        payload = {
            "body": body
        }
        
        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/session/settings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('General session management settings updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the appropriate IdP/SP role enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getGlobalPolicy(self):
        """ Get the global authentication session policy.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/session/authenticationSessionPolicies/global"),
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

    def updateGlobalPolicy(self, body):
        """ Update the global authentication session policy.
        """
        
        payload = {
            "body": body
        }
        
        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/session/authenticationSessionPolicies/global"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('Global authentication session policy updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the appropriate IdP/SP role enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getApplicationPolicy(self):
        """ Get the application session policy.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/session/applicationSessionPolicy"),
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

    def updateApplicationPolicy(self, body):
        """ Update the application session policy.
        """
        
        payload = {
            "body": body
        }
        
        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/session/applicationSessionPolicy"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('Application session policy updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the appropriate IdP/SP role enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getSourcePolicies(self):
        """ Get list of session policies.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/session/authenticationSessionPolicies"),
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

    def createSourcePolicy(self, body):
        """ Create a new session policy.
        """
        
        payload = {
            "body": body
        }
        
        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/session/authenticationSessionPolicies"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 201:
                self.logger.info('Authentication session policy created.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the appropriate IdP/SP role enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getSourcePolicy(self, id):
        """ Find session policy by ID.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/session/authenticationSessionPolicies/{id}"),
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
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def updateSourcePolicy(self, id, body):
        """ Update a session policy.
        """
        
        payload = {
            "id": id"body": body
        }
        
        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/session/authenticationSessionPolicies/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('Authentication session policy updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the appropriate IdP/SP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def deleteSourcePolicy(self, id):
        """ Delete a session policy.
        """
        
        try:
            response = requests.delete(
                
                url=self._build_uri("/session/authenticationSessionPolicies/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 204:
                self.logger.info('Authentication session policy deleted.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the appropriate IdP/SP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

