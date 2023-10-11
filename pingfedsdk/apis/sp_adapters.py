from json import dumps
import logging
import os
import traceback

from requests import Session
from requests.exceptions import HTTPError

from pingfedsdk.exceptions import BadRequest
from pingfedsdk.exceptions import NotFound
from pingfedsdk.exceptions import ObjectDeleted
from pingfedsdk.exceptions import ValidationError
from pingfedsdk.models.action import Action as ModelAction
from pingfedsdk.models.action_options import ActionOptions as ModelActionOptions
from pingfedsdk.models.action_result import ActionResult as ModelActionResult
from pingfedsdk.models.actions import Actions as ModelActions
from pingfedsdk.models.api_result import ApiResult as ModelApiResult
from pingfedsdk.models.sp_adapter import SpAdapter as ModelSpAdapter
from pingfedsdk.models.sp_adapter_descriptor import SpAdapterDescriptor as ModelSpAdapterDescriptor
from pingfedsdk.models.sp_adapter_descriptors import SpAdapterDescriptors as ModelSpAdapterDescriptors
from pingfedsdk.models.sp_adapter_url_mappings import SpAdapterUrlMappings as ModelSpAdapterUrlMappings
from pingfedsdk.models.sp_adapters import SpAdapters as ModelSpAdapters


class SpAdapters:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.SpAdapters")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getAction(self, actionId: str, id: str):
        """ Find an SP adapter instance's action by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/sp/adapters/{id}/actions/{actionId}"),
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
                return ModelAction.from_dict(response_dict)
            else:
                return ModelAction.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def invokeActionWithOptions(self, actionId: str, id: str, body: ModelActionOptions = None):
        """ Invokes an action for an SP adapter instance.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/sp/adapters/{id}/actions/{actionId}/invokeAction"),
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
                self.logger.info("Action invoked on adapter.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelActionResult.from_dict(response_dict)
            else:
                return ModelActionResult.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getSpAdapterDescriptors(self):
        """ Get the list of available SP adapter descriptors.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/sp/adapters/descriptors"),
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
                return ModelSpAdapterDescriptors.from_dict(response_dict)
            else:
                return ModelSpAdapterDescriptors.from_dict(response.json())

    def getSpAdapterDescriptorsById(self, id: str):
        """ Get the description of an SP adapter plugin by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/sp/adapters/descriptors/{id}"),
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
                return ModelSpAdapterDescriptor.from_dict(response_dict)
            else:
                return ModelSpAdapterDescriptor.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getSpAdapters(self, filter: str = None, numberPerPage: int = None, page: int = None):
        """ Get the list of configured SP adapter instances.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/sp/adapters"),
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
                return ModelSpAdapters.from_dict(response_dict)
            else:
                return ModelSpAdapters.from_dict(response.json())
            if response.status_code == 422:
                raise ValidationError(response.json())

    def createSpAdapter(self, body: ModelSpAdapter):
        """ Create a new SP adapter instance.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/sp/adapters"),
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
                self.logger.info("Adapter created.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelSpAdapter.from_dict(response_dict)
            else:
                return ModelSpAdapter.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getSpAdapter(self, id: str):
        """ Find an SP adapter instance by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/sp/adapters/{id}"),
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
                return ModelSpAdapter.from_dict(response_dict)
            else:
                return ModelSpAdapter.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateSpAdapter(self, body: ModelSpAdapter, id: str):
        """ Update an SP adapter instance.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/sp/adapters/{id}"),
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
                self.logger.info("Adapter updated.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelSpAdapter.from_dict(response_dict)
            else:
                return ModelSpAdapter.from_dict(response.json())
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

    def deleteSpAdapter(self, id: str):
        """ Delete an SP adapter instance.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/sp/adapters/{id}"),
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
                self.logger.info("Adapter deleted.")
                return ModelApiResult(message="Adapter deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getUrlMappings(self):
        """ (Deprecated) List the mappings between URLs and adapter instances.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/sp/adapters/urlMappings"),
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
                return ModelSpAdapterUrlMappings.from_dict(response_dict)
            else:
                return ModelSpAdapterUrlMappings.from_dict(response.json())

    def updateUrlMappings(self, body: ModelSpAdapterUrlMappings):
        """ (Deprecated) Update the mappings between URLs and adapters instances.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/sp/adapters/urlMappings"),
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
                self.logger.info("Mapping updated.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelSpAdapterUrlMappings.from_dict(response_dict)
            else:
                return ModelSpAdapterUrlMappings.from_dict(response.json())
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getActions(self, id: str):
        """ List the actions for an SP adapter instance.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/sp/adapters/{id}/actions"),
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
                return ModelActions.from_dict(response_dict)
            else:
                return ModelActions.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
