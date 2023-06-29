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
from pingfedsdk.models.action_options import ActionOptions as ModelActionOptions
from pingfedsdk.models.custom_data_store_descriptor import CustomDataStoreDescriptor as ModelCustomDataStoreDescriptor
from pingfedsdk.models.action import Action as ModelAction
from pingfedsdk.models.api_result import ApiResult as ModelApiResult
from pingfedsdk.models.data_store import DataStore as ModelDataStore
from pingfedsdk.models.actions import Actions as ModelActions
from pingfedsdk.models.custom_data_store_descriptors import CustomDataStoreDescriptors as ModelCustomDataStoreDescriptors
from pingfedsdk.models.data_stores import DataStores as ModelDataStores
from pingfedsdk.models.action_result import ActionResult as ModelActionResult


class DataStores:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.DataStores")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getDataStores(self):
        """ Get list of all data stores.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/dataStores"),
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
                return ModelDataStores.from_dict(response.json())

    def createDataStore(self, body: ModelDataStore, XBypassExternalValidation: bool = None):
        """ Create a new data store.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/dataStores"),
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

    def getDataStore(self, id: str):
        """ Find data store by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/dataStores/{id}"),
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

    def updateDataStore(self, id: str, body: ModelDataStore, XBypassExternalValidation: bool = None):
        """ Update a data store.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/dataStores/{id}"),
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

    def deleteDataStore(self, id: str):
        """ Delete a data store.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/dataStores/{id}"),
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
                message = "(204) Data store deleted."
                self.logger.info(message)
                raise ObjectDeleted(message)
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                message = "(422) Resource is in use and cannot be deleted."
                self.logger.info(message)
                raise ValidationError(message)

    def getCustomDataStoreDescriptors(self):
        """ Get the list of available custom data store descriptors.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/dataStores/descriptors"),
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
                return ModelCustomDataStoreDescriptors.from_dict(response.json())

    def getCustomDataStoreDescriptor(self, id: str):
        """ Get the description of a custom data store plugin by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/dataStores/descriptors/{id}"),
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

    def invokeActionWithOptions(self, id: str, actionId: str, body: ModelActionOptions = None):
        """ Invokes an action for a data source instance.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/dataStores/{id}/actions/{actionId}/invokeAction"),
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
        """ Find a data store instance's action by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/dataStores/{id}/actions/{actionId}"),
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
        """ List the actions for a data store instance.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/dataStores/{id}/actions"),
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
