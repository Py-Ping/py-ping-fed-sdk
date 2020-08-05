import logging
import requests

class _sp_idpConnections():
    def __init__(self, endpoint):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._sp_idpConnections')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path):
        return f"{self.endpoint}{path}"

    def getConnections(self, entityId, page, numberPerPage, filter):
        """ Get list of IdP connections.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/sp/idpConnections"),
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
                self.logger.info('PingFederate does not have its SP role enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def createConnection(self, body, X-BypassExternalValidation):
        """ Create a new IdP connection.
        """
        
        payload = {
            "body": body"X-BypassExternalValidation": X-BypassExternalValidation
        }
        
        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/sp/idpConnections"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 201:
                self.logger.info('Connection created.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its SP role enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getConnection(self, id):
        """ Find IdP connection by ID.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/sp/idpConnections/{id}"),
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
                self.logger.info('PingFederate does not have its SP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def updateConnection(self, id, body, X-BypassExternalValidation):
        """ Update an IdP connection.
        """
        
        payload = {
            "id": id"body": body"X-BypassExternalValidation": X-BypassExternalValidation
        }
        
        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/sp/idpConnections/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('Connection updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its SP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def deleteConnection(self, id):
        """ Delete an IdP connection.
        """
        
        try:
            response = requests.delete(
                
                url=self._build_uri("/sp/idpConnections/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 204:
                self.logger.info('Connection deleted.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its SP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Resource is in use and cannot be deleted.')
        finally:
            return response

    def getSigningSettings(self, id):
        """ Get the IdP connection's signature settings.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/sp/idpConnections/{id}/credentials/signingSettings"),
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
                self.logger.info('PingFederate does not have its SP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def updateSigningSettings(self, id, body):
        """ Update the IdP connection's signature settings.
        """
        
        payload = {
            "id": id"body": body
        }
        
        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/sp/idpConnections/{id}/credentials/signingSettings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('Connection updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its SP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def addConnectionCert(self, id, body):
        """ Add a new IdP connection certificate.
        """
        
        payload = {
            "id": id"body": body
        }
        
        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/sp/idpConnections/{id}/credentials/certs"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 201:
                self.logger.info('Connection Certificate added.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its SP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getConnectionCerts(self, id):
        """ Get the IdP connection's certificates.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/sp/idpConnections/{id}/credentials/certs"),
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
                self.logger.info('PingFederate does not have its SP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def updateConnectionCerts(self, id, body):
        """ Update the IdP connection's certificates.
        """
        
        payload = {
            "id": id"body": body
        }
        
        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/sp/idpConnections/{id}/credentials/certs"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('Connection updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its SP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getDecryptionKeys(self, id):
        """ Get the decryption keys of an IdP connection.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/sp/idpConnections/{id}/credentials/decryptionKeys"),
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
                self.logger.info('PingFederate does not have its SP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def updateDecryptionKeys(self, id, body):
        """ Updating the IdP connection's decryption keys.
        """
        
        payload = {
            "id": id"body": body
        }
        
        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/sp/idpConnections/{id}/credentials/decryptionKeys"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('Connection updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its SP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

