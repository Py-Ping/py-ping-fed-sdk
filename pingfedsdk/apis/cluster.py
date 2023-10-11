from json import dumps
import logging
import os
import traceback

from requests import Session
from requests.exceptions import HTTPError

from pingfedsdk.exceptions import NotImplementedError
from pingfedsdk.models.api_result import ApiResult as ModelApiResult
from pingfedsdk.models.cluster_status import ClusterStatus as ModelClusterStatus


class Cluster:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.Cluster")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
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
                headers={"Content-Type": "application/json"}
            )
        except HTTPError as http_err:
            print(traceback.format_exc())
            self.logger.error(f"HTTP error occurred: {http_err}")
            raise http_err
        except Exception as err:
            print(traceback.format_exc())
            self.logger.error(f"Error occurred: {err}")
            raise err
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelClusterStatus.from_dict(response_dict)
                else:
                    return ModelClusterStatus.from_dict(response.json())
            if response.status_code == 403:
                message = "(403) This PingFederate instance is not deployed in clustered mode."
                self.logger.info(message)
                raise NotImplementedError(message)

    def startReplication(self):
        """ Replicate configuration updates to all nodes in the cluster.
        """

        try:
            response = self.session.post(
                url=self._build_uri("/cluster/replicate"),
                headers={"Content-Type": "application/json"}
            )
        except HTTPError as http_err:
            print(traceback.format_exc())
            self.logger.error(f"HTTP error occurred: {http_err}")
            raise http_err
        except Exception as err:
            print(traceback.format_exc())
            self.logger.error(f"Error occurred: {err}")
            raise err
        else:
            if response.status_code == 200:
                self.logger.info("Replication completed successfully.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelApiResult.from_dict(response.json())
                else:
                    return ModelApiResult.from_dict(response.json())
            if response.status_code == 403:
                message = "(403) This PingFederate instance is not deployed in clustered mode."
                self.logger.info(message)
                raise NotImplementedError(message)
