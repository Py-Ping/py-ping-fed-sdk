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
from pingfedsdk.models.access_token_management_settings import AccessTokenManagementSettings as ModelAccessTokenManagementSettings
from pingfedsdk.models.access_token_manager import AccessTokenManager as ModelAccessTokenManager
from pingfedsdk.models.access_token_manager_descriptor import AccessTokenManagerDescriptor as ModelAccessTokenManagerDescriptor
from pingfedsdk.models.access_token_manager_descriptors import AccessTokenManagerDescriptors as ModelAccessTokenManagerDescriptors
from pingfedsdk.models.access_token_managers import AccessTokenManagers as ModelAccessTokenManagers
from pingfedsdk.models.api_result import ApiResult as ModelApiResult


class OauthAccessTokenManagers:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.OauthAccessTokenManagers")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getSettings(self):
        """ Get general access token management settings.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/oauth/accessTokenManagers/settings"),
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
                    return ModelAccessTokenManagementSettings.from_dict(response_dict)
                else:
                    return ModelAccessTokenManagementSettings.from_dict(response.json())

    def updateSettings(self, body: ModelAccessTokenManagementSettings):
        """ Update general access token management settings.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/oauth/accessTokenManagers/settings"),
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
                self.logger.info("Settings updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelAccessTokenManagementSettings.from_dict(response_dict)
                else:
                    return ModelAccessTokenManagementSettings.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getTokenManagers(self):
        """ Get a list of all token management plugin instances.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/oauth/accessTokenManagers"),
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
                    return ModelAccessTokenManagers.from_dict(response_dict)
                else:
                    return ModelAccessTokenManagers.from_dict(response.json())

    def createTokenManager(self, body: ModelAccessTokenManager):
        """ Create a token management plugin instance.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/oauth/accessTokenManagers"),
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
                self.logger.info("Access Token Management instance created.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelAccessTokenManager.from_dict(response_dict)
                else:
                    return ModelAccessTokenManager.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getTokenManager(self, id: str):
        """ Get a specific token management plugin instance.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/oauth/accessTokenManagers/{id}"),
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
                    return ModelAccessTokenManager.from_dict(response_dict)
                else:
                    return ModelAccessTokenManager.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateTokenManager(self, body: ModelAccessTokenManager, id: str):
        """ Update a token management plugin instance.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/oauth/accessTokenManagers/{id}"),
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
                self.logger.info("Access Token Management instance updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelAccessTokenManager.from_dict(response_dict)
                else:
                    return ModelAccessTokenManager.from_dict(response.json())
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

    def deleteTokenManager(self, id: str):
        """ Delete a token management plugin instance.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/oauth/accessTokenManagers/{id}"),
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
                self.logger.info("Access token management instance deleted.")
                return ModelApiResult(message="Access token management instance deleted.", validationErrors=[])
            if response.status_code == 403:
                message = "(403) The operation is not permitted, based on the current configuration of the server."
                self.logger.info(message)
                raise NotImplementedError(message)
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getTokenManagerDescriptors(self):
        """ Get the list of available token management plugin descriptors.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/oauth/accessTokenManagers/descriptors"),
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
                    return ModelAccessTokenManagerDescriptors.from_dict(response_dict)
                else:
                    return ModelAccessTokenManagerDescriptors.from_dict(response.json())

    def getTokenManagerDescriptor(self, id: str):
        """ Get the description of a token management plugin descriptor.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/oauth/accessTokenManagers/descriptors/{id}"),
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
                    return ModelAccessTokenManagerDescriptor.from_dict(response_dict)
                else:
                    return ModelAccessTokenManagerDescriptor.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
