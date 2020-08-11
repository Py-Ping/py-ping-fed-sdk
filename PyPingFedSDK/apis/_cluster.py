import os
import logging
from requests import Session
from requests.exceptions import HTTPError


class _cluster():
    def __init__(self, endpoint:str, session:Session) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._cluster')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getClusterStatus(self):
        """ Get information on the current status of the cluster.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/cluster/status"),
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
                self.logger.info('This PingFederate instance is not deployed in clustered mode.')
        finally:
            return response

    def startReplication(self):
        """ Replicate configuration updates to all nodes in the cluster.
        """

        payload = {

        }

        try:
            response = self.session.post(
                data=payload,
                url=self._build_uri("/cluster/replicate"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Replication completed successfully.')
            if response.status_code == 403:
                self.logger.info('This PingFederate instance is not deployed in clustered mode.')
        finally:
            return response

