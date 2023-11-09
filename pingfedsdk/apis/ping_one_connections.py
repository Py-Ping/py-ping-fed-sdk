from json import dumps
import logging
import os
import traceback

from requests import Session
from requests.exceptions import HTTPError

from pingfedsdk.exceptions import BadRequest
from pingfedsdk.exceptions import NotFound
from pingfedsdk.exceptions import ObjectDeleted
from pingfedsdk.exceptions import ServerError
from pingfedsdk.exceptions import ValidationError
from pingfedsdk.models.api_result import ApiResult as ModelApiResult
from pingfedsdk.models.ping_one_connection import PingOneConnection as ModelPingOneConnection
from pingfedsdk.models.ping_one_connections import PingOneConnections as ModelPingOneConnections
from pingfedsdk.models.ping_one_credential_status import PingOneCredentialStatus as ModelPingOneCredentialStatus
from pingfedsdk.models.ping_one_environments import PingOneEnvironments as ModelPingOneEnvironments
from pingfedsdk.models.resource_usages import ResourceUsages as ModelResourceUsages
from pingfedsdk.models.service_associations import ServiceAssociations as ModelServiceAssociations


class PingOneConnections:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.PingOneConnections")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getPingOneConnection(self, id: str):
        """ Get a PingOne connection with the specified ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/pingOneConnections/{id}"),
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
                    return ModelPingOneConnection.from_dict(response_dict)
                else:
                    return ModelPingOneConnection.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updatePingOneConnection(self, body: ModelPingOneConnection, id: str, XBypassExternalValidation: bool = None):
        """ Update a PingOne connection.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/pingOneConnections/{id}"),
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
                self.logger.info("PingOne connection updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelPingOneConnection.from_dict(response_dict)
                else:
                    return ModelPingOneConnection.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def deletePingOneConnection(self, id: str):
        """ Delete a PingOne connection.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/pingOneConnections/{id}"),
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
            if response.status_code == 204:
                self.logger.info("PingOne connection deleted.")
                return ModelApiResult(message="PingOne connection deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getPingOneConnectionUsages(self, id: str):
        """ Get the list of resources that reference this PingOne connection.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/pingOneConnections/{id}/usage"),
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
                    return ModelResourceUsages.from_dict(response_dict)
                else:
                    return ModelResourceUsages.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getPingOneConnectionAssociations(self, id: str):
        """ Get information about components using this connection to access PingOne services.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/pingOneConnections/{id}/serviceAssociations"),
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
                    return ModelServiceAssociations.from_dict(response_dict)
                else:
                    return ModelServiceAssociations.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getPingOneConnections(self):
        """ Get the list of all PingOne connections.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/pingOneConnections"),
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
                    return ModelPingOneConnections.from_dict(response_dict)
                else:
                    return ModelPingOneConnections.from_dict(response.json())

    def createPingOneConnection(self, body: ModelPingOneConnection, XBypassExternalValidation: bool = None):
        """ Create a new PingOne connection.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/pingOneConnections"),
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
            if response.status_code == 201:
                self.logger.info("PingOne connection created.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelPingOneConnection.from_dict(response_dict)
                else:
                    return ModelPingOneConnection.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getCredentialStatus(self, id: str):
        """ Get the status of the credential associated with the PingOne connection
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/pingOneConnections/{id}/credentialStatus"),
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
                    return ModelPingOneCredentialStatus.from_dict(response_dict)
                else:
                    return ModelPingOneCredentialStatus.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getPingOneConnectionEnvironments(self, id: str, filter: str = None, numberPerPage: int = None, page: int = None):
        """ Get the list of environments that the PingOne connection has access to.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/pingOneConnections/{id}/environments"),
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
                    return ModelPingOneEnvironments.from_dict(response_dict)
                else:
                    return ModelPingOneEnvironments.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 500:
                message = "(500) Error connecting to PingOne"
                self.logger.info(message)
                raise ServerError(message)