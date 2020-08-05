import logging
import requests

class _localIdentity_identityProfiles():
    def __init__(self, endpoint):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._localIdentity_identityProfiles')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path):
        return f"{self.endpoint}{path}"

    def getIdentityProfiles(self, page, numberPerPage, filter):
        """ Get the list of configured local identity profiles.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/localIdentity/identityProfiles"),
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

    def createIdentityProfile(self, body, X-BypassExternalValidation):
        """ Create a new local identity profile.
        """
        
        payload = {
            "body": body"X-BypassExternalValidation": X-BypassExternalValidation
        }
        
        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/localIdentity/identityProfiles"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 201:
                self.logger.info('Local identity profile created.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its IdP role enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getIdentityProfile(self, id):
        """ Get the local identity profile by ID.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/localIdentity/identityProfiles/{id}"),
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

    def updateIdentityProfile(self, id, body, X-BypassExternalValidation):
        """ Update the local identity profile by ID.
        """
        
        payload = {
            "id": id"body": body"X-BypassExternalValidation": X-BypassExternalValidation
        }
        
        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/localIdentity/identityProfiles/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('Local identity profile updated.')
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

    def deleteIdentityProfile(self, id):
        """ Delete the local identity profile by ID.
        """
        
        try:
            response = requests.delete(
                
                url=self._build_uri("/localIdentity/identityProfiles/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 204:
                self.logger.info('Local identity profile deleted.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have its IdP role enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

