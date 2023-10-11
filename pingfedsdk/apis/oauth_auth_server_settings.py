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
from pingfedsdk.models.api_result import ApiResult as ModelApiResult
from pingfedsdk.models.authorization_server_settings import AuthorizationServerSettings as ModelAuthorizationServerSettings
from pingfedsdk.models.scope_entry import ScopeEntry as ModelScopeEntry
from pingfedsdk.models.scope_group_entry import ScopeGroupEntry as ModelScopeGroupEntry


class OauthAuthServerSettings:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.OauthAuthServerSettings")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getAuthorizationServerSettings(self):
        """ Get the Authorization Server Settings.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/oauth/authServerSettings"),
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
                return ModelAuthorizationServerSettings.from_dict(response_dict)
            else:
                return ModelAuthorizationServerSettings.from_dict(response.json())

    def updateAuthorizationServerSettings(self, body: ModelAuthorizationServerSettings):
        """ Update the Authorization Server Settings.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/oauth/authServerSettings"),
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
                self.logger.info("Authorization Server Settings updated.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelAuthorizationServerSettings.from_dict(response_dict)
            else:
                return ModelAuthorizationServerSettings.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def addCommonScope(self, body: ModelScopeEntry):
        """ Add a new common scope.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/oauth/authServerSettings/scopes/commonScopes"),
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
                self.logger.info("Common Scope added.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelScopeEntry.from_dict(response_dict)
            else:
                return ModelScopeEntry.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getCommonScope(self, name: str):
        """ Get an existing common scope.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/oauth/authServerSettings/scopes/commonScopes/{name}"),
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
                return ModelScopeEntry.from_dict(response_dict)
            else:
                return ModelScopeEntry.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateCommonScope(self, body: ModelScopeEntry, name: str):
        """ Update an existing common scope.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/oauth/authServerSettings/scopes/commonScopes/{name}"),
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
                self.logger.info("Common Scope updated.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelScopeEntry.from_dict(response_dict)
            else:
                return ModelScopeEntry.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def removeCommonScope(self, name: str):
        """ Remove an existing common scope.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/oauth/authServerSettings/scopes/commonScopes/{name}"),
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
                self.logger.info("Common Scope deleted.")
                return ModelApiResult(message="Common Scope deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def addCommonScopeGroup(self, body: ModelScopeGroupEntry):
        """ Create a new common scope group.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/oauth/authServerSettings/scopes/commonScopeGroups"),
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
                self.logger.info("Common Scope Group created.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelScopeGroupEntry.from_dict(response_dict)
            else:
                return ModelScopeGroupEntry.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getCommonScopeGroup(self, name: str):
        """ Get an existing common scope group.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/oauth/authServerSettings/scopes/commonScopeGroups/{name}"),
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
                return ModelScopeGroupEntry.from_dict(response_dict)
            else:
                return ModelScopeGroupEntry.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateCommonScopeGroup(self, body: ModelScopeGroupEntry, name: str):
        """ Update an existing common scope group.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/oauth/authServerSettings/scopes/commonScopeGroups/{name}"),
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
                self.logger.info("Common Scope Group updated.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelScopeGroupEntry.from_dict(response_dict)
            else:
                return ModelScopeGroupEntry.from_dict(response.json())
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

    def removeCommonScopeGroup(self, name: str):
        """ Remove an existing common scope group.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/oauth/authServerSettings/scopes/commonScopeGroups/{name}"),
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
                self.logger.info("Common Scope Group deleted.")
                return ModelApiResult(message="Common Scope Group deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def addExclusiveScope(self, body: ModelScopeEntry):
        """ Add a new exclusive scope.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/oauth/authServerSettings/scopes/exclusiveScopes"),
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
                self.logger.info("Exclusive Scope added.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelScopeEntry.from_dict(response_dict)
            else:
                return ModelScopeEntry.from_dict(response.json())
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

    def getExclusiveScope(self, name: str):
        """ Get an existing exclusive scope.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/oauth/authServerSettings/scopes/exclusiveScopes/{name}"),
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
                return ModelScopeEntry.from_dict(response_dict)
            else:
                return ModelScopeEntry.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateExclusiveScope(self, body: ModelScopeEntry, name: str):
        """ Update an existing exclusive scope.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/oauth/authServerSettings/scopes/exclusiveScopes/{name}"),
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
                self.logger.info("Exclusive Scope updated.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelScopeEntry.from_dict(response_dict)
            else:
                return ModelScopeEntry.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def removeExclusiveScope(self, name: str):
        """ Remove an existing exclusive scope.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/oauth/authServerSettings/scopes/exclusiveScopes/{name}"),
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
                self.logger.info("Exclusive Scope deleted.")
                return ModelApiResult(message="Exclusive Scope deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def addExclusiveScopeGroup(self, body: ModelScopeGroupEntry):
        """ Create a new exclusive scope group.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/oauth/authServerSettings/scopes/exclusiveScopeGroups"),
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
                self.logger.info("Exclusive Scope Group created.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelScopeGroupEntry.from_dict(response_dict)
            else:
                return ModelScopeGroupEntry.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getExclusiveScopeGroup(self, name: str):
        """ Get an existing exclusive scope group.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/oauth/authServerSettings/scopes/exclusiveScopeGroups/{name}"),
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
                return ModelScopeGroupEntry.from_dict(response_dict)
            else:
                return ModelScopeGroupEntry.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateExclusiveScopeGroups(self, body: ModelScopeGroupEntry, name: str):
        """ Update an existing exclusive scope group.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/oauth/authServerSettings/scopes/exclusiveScopeGroups/{name}"),
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
                self.logger.info("Exclusive Scope Group updated.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelScopeGroupEntry.from_dict(response_dict)
            else:
                return ModelScopeGroupEntry.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def removeExclusiveScopeGroup(self, name: str):
        """ Remove an existing exclusive scope group.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/oauth/authServerSettings/scopes/exclusiveScopeGroups/{name}"),
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
                self.logger.info("Exclusive Scope Group deleted.")
                return ModelApiResult(message="Exclusive Scope Group deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())
