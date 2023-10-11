from json import dumps
import logging
import os
import traceback

from requests import Session
from requests.exceptions import HTTPError

from pingfedsdk.exceptions import BadRequest
from pingfedsdk.exceptions import NotFound
from pingfedsdk.exceptions import NotImplementedError
from pingfedsdk.exceptions import ObjectDeleted
from pingfedsdk.exceptions import ValidationError
from pingfedsdk.models.action import Action as ModelAction
from pingfedsdk.models.action_options import ActionOptions as ModelActionOptions
from pingfedsdk.models.action_result import ActionResult as ModelActionResult
from pingfedsdk.models.actions import Actions as ModelActions
from pingfedsdk.models.api_result import ApiResult as ModelApiResult
from pingfedsdk.models.out_of_band_auth_plugin_descriptor import OutOfBandAuthPluginDescriptor as ModelOutOfBandAuthPluginDescriptor
from pingfedsdk.models.out_of_band_auth_plugin_descriptors import OutOfBandAuthPluginDescriptors as ModelOutOfBandAuthPluginDescriptors
from pingfedsdk.models.out_of_band_authenticator import OutOfBandAuthenticator as ModelOutOfBandAuthenticator
from pingfedsdk.models.out_of_band_authenticators import OutOfBandAuthenticators as ModelOutOfBandAuthenticators


class OauthOutOfBandAuthPlugins:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.OauthOutOfBandAuthPlugins")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getAction(self, actionId: str, id: str):
        """ Find an Out of Band authenticator plugin instance's action by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/oauth/outOfBandAuthPlugins/{id}/actions/{actionId}"),
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
        """ Invokes an action for Out of Band authenticator plugin instance.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/oauth/outOfBandAuthPlugins/{id}/actions/{actionId}/invokeAction"),
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
                self.logger.info("Action invoked on Out of Band authenticator.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelActionResult.from_dict(response_dict)
                else:
                    return ModelActionResult.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getOOBAuthPluginDescriptors(self):
        """ Get the list of available Out of Band authenticator plugin descriptors.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/oauth/outOfBandAuthPlugins/descriptors"),
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
                    return ModelOutOfBandAuthPluginDescriptors.from_dict(response_dict)
                else:
                    return ModelOutOfBandAuthPluginDescriptors.from_dict(response.json())

    def getOOBAuthPluginDescriptor(self, id: str):
        """ Get the descriptor of an Out of Band authenticator plugin.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/oauth/outOfBandAuthPlugins/descriptors/{id}"),
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
                    return ModelOutOfBandAuthPluginDescriptor.from_dict(response_dict)
                else:
                    return ModelOutOfBandAuthPluginDescriptor.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getOOBAuthenticators(self):
        """ Get a list of Out of Band authenticator plugin instances.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/oauth/outOfBandAuthPlugins"),
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
                    return ModelOutOfBandAuthenticators.from_dict(response_dict)
                else:
                    return ModelOutOfBandAuthenticators.from_dict(response.json())

    def createOOBAuthenticator(self, body: ModelOutOfBandAuthenticator):
        """ Create an Out of Band authenticator plugin instance.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/oauth/outOfBandAuthPlugins"),
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
                self.logger.info("Out of Band Authenticator created.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelOutOfBandAuthenticator.from_dict(response_dict)
                else:
                    return ModelOutOfBandAuthenticator.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getOOBAuthenticator(self, id: str):
        """ Get a specific Out of Band authenticator plugin instance.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/oauth/outOfBandAuthPlugins/{id}"),
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
                    return ModelOutOfBandAuthenticator.from_dict(response_dict)
                else:
                    return ModelOutOfBandAuthenticator.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateOOBAuthenticator(self, body: ModelOutOfBandAuthenticator, id: str):
        """ Update an Out of Band authenticator plugin instance.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/oauth/outOfBandAuthPlugins/{id}"),
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
                self.logger.info("Out of Band Authenticator updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelOutOfBandAuthenticator.from_dict(response_dict)
                else:
                    return ModelOutOfBandAuthenticator.from_dict(response.json())
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

    def deleteOOBAuthenticator(self, id: str):
        """ Delete an Out of Band authenticator plugin instance.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/oauth/outOfBandAuthPlugins/{id}"),
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
                self.logger.info("Out of Band Authenticator deleted.")
                return ModelApiResult(message="Out of Band Authenticator deleted.", validationErrors=[])
            if response.status_code == 403:
                message = "(403) The operation is not permitted, based on the current configuration of the server."
                self.logger.info(message)
                raise NotImplementedError(message)
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getActions(self, id: str):
        """ List of actions for an Out of Band authenticator plugin instance.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/oauth/outOfBandAuthPlugins/{id}/actions"),
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
