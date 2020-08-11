import os
import logging
from requests import Session
from requests.exceptions import HTTPError


class _configArchive():
    def __init__(self, endpoint:str, session:Session) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._configArchive')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def importConfigArchive(self, file, forceImport):
        """ Import a configuration archive.
        """

        payload = {
            "file": file,
            "forceImport": forceImport

        }

        try:
            response = self.session.post(
                data=payload,
                url=self._build_uri("/configArchive/import"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Configuration Archive imported.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def exportConfigArchive(self):
        """ Export a configuration archive.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/configArchive/export"),
                headers={'Accept': '['application/json', 'application/zip']'}
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

