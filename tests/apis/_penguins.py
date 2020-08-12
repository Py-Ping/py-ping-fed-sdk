import os
import logging
from requests import Session
from requests.exceptions import HTTPError


class _penguins():
    def __init__(self, endpoint:str, session:Session) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._penguins')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getPenguinDetails(self):
        """ Retrieve list of available penguins.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/penguins"),
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

    def addPenguin(self, firstName):
        """ Add a new penguin.
        """

        payload = {
            "firstName": firstName

        }

        try:
            response = self.session.post(
                data=payload,
                url=self._build_uri("/penguins"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Penguin uploaded.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

