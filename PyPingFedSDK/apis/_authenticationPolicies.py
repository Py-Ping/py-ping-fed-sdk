import logging
import requests

class _authenticationPolicies():
    def __init__(self, endpoint):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._authenticationPolicies')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path):
        return f"{self.endpoint}{path}"

    def getSettings(self):
        """ Get the authentication policies settings.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/authenticationPolicies/settings"),
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

    def updateSettings(self, body):
        """ Set the authentication policies settings.
        """
        
        payload = {
            "body": body
        }
        
        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/authenticationPolicies/settings"),
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
                self.logger.info('PingFederate does not have the appropriate IdP/SP role enabled. Operation not available.')
        finally:
            return response

    def getDefaultAuthenticationPolicy(self):
        """ Get the default configured authentication policy.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/authenticationPolicies/default"),
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

    def updateDefaultAuthenticationPolicy(self, body, X-BypassExternalValidation):
        """ Set the default authentication policy.
        """
        
        payload = {
            "body": body"X-BypassExternalValidation": X-BypassExternalValidation
        }
        
        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/authenticationPolicies/default"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('Default authentication policy updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the appropriate IdP/SP role enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

