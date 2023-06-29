import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingfedsdk.exceptions import ValidationError
from pingfedsdk.exceptions import ObjectDeleted
from pingfedsdk.exceptions import BadRequest
from pingfedsdk.exceptions import NotFound
from pingfedsdk.exceptions import NotImplementedError
from pingfedsdk.models.secret_manager_descriptors import SecretManagerDescriptors as ModelSecretManagerDescriptors
from pingfedsdk.models.action_options import ActionOptions as ModelActionOptions
from pingfedsdk.models.secret_managers import SecretManagers as ModelSecretManagers
from pingfedsdk.models.secret_manager import SecretManager as ModelSecretManager
from pingfedsdk.models.action import Action as ModelAction
from pingfedsdk.models.api_result import ApiResult as ModelApiResult
from pingfedsdk.models.actions import Actions as ModelActions
from pingfedsdk.models.action_result import ActionResult as ModelActionResult
from pingfedsdk.models.secret_manager_descriptor import SecretManagerDescriptor as ModelSecretManagerDescriptor


class SecretManagers:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.SecretManagers")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getSecretManagers(self):
        """ Get a list of secret manager plugin instances.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/secretManagers"),
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
                return ModelSecretManagers.from_dict(response.json())

    def createSecretManager(self, body: ModelSecretManager):
        """ Create a secret manager plugin instance.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/secretManagers"),
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
                return ModelApiResult.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                message = "(422) Validation error(s) occurred."
                self.logger.info(message)
                raise ValidationError(message)

    def getSecretManagerPluginDescriptors(self):
        """ Get a list of available secret manager plugin descriptors.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/secretManagers/descriptors"),
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
                return ModelSecretManagerDescriptors.from_dict(response.json())

    def getSecretManagerPluginDescriptor(self, id: str):
        """ Get a secret manager plugin descriptor.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/secretManagers/descriptors/{id}"),
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
                return ModelApiResult.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getSecretManager(self, id: str):
        """ Get a specific secret manager plugin instance.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/secretManagers/{id}"),
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
                return ModelApiResult.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateSecretManager(self, id: str, body: ModelSecretManager):
        """ Update a secret manager plugin instance.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/secretManagers/{id}"),
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
                return ModelApiResult.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                message = "(422) Validation error(s) occurred."
                self.logger.info(message)
                raise ValidationError(message)

    def deleteSecretManager(self, id: str):
        """ Delete a secret manager plugin instance.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/secretManagers/{id}"),
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
                message = "(204) Secret Manager plugin deleted."
                self.logger.info(message)
                raise ObjectDeleted(message)
            if response.status_code == 403:
                message = "(403) The operation is not permitted, based on the current configuration of the server."
                self.logger.info(message)
                raise NotImplementedError(message)
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def invokeActionWithOptions(self, id: str, actionId: str, body: ModelActionOptions = None):
        """ Invokes an action for secret manager plugin instance.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/secretManagers/{id}/actions/{actionId}/invokeAction"),
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
                return ModelApiResult.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getAction(self, id: str, actionId: str):
        """ Get a secret manager plugin instance's action by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/secretManagers/{id}/actions/{actionId}"),
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
                return ModelApiResult.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getActions(self, id: str):
        """ Get a list of actions for a secret manager plugin instance.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/secretManagers/{id}/actions"),
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
                return ModelApiResult.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
