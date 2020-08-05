import logging
import requests

class _license():
    def __init__(self, endpoint):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._license')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path):
        return f"{self.endpoint}{path}"

    def getLicenseAgreement(self):
        """ Get license agreement link.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/license/agreement"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def updateLicenseAgreement(self, body):
        """ Accept license agreement.
        """
        
        payload = {
            "body": body
        }
        
        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/license/agreement"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('License agreement accepted.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getLicense(self):
        """ Get a license summary.
        """
        
        try:
            response = requests.get(
                
                url=self._build_uri("/license"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def updateLicense(self, body):
        """ Import a license.
        """
        
        payload = {
            "body": body
        }
        
        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/license"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}') 
        else:
            if response.status_code == 200:
                self.logger.info('License imported.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

