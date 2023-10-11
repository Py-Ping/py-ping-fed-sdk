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
from pingfedsdk.models.authentication_policies_settings import AuthenticationPoliciesSettings as ModelAuthenticationPoliciesSettings
from pingfedsdk.models.authentication_policy import AuthenticationPolicy as ModelAuthenticationPolicy
from pingfedsdk.models.authentication_policy_fragment import AuthenticationPolicyFragment as ModelAuthenticationPolicyFragment
from pingfedsdk.models.authentication_policy_fragments import AuthenticationPolicyFragments as ModelAuthenticationPolicyFragments
from pingfedsdk.models.authentication_policy_tree import AuthenticationPolicyTree as ModelAuthenticationPolicyTree
from pingfedsdk.models.move_item_request import MoveItemRequest as ModelMoveItemRequest


class AuthenticationPolicies:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.AuthenticationPolicies")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getSettings(self):
        """ Get the authentication policies settings.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/authenticationPolicies/settings"),
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
                return ModelAuthenticationPoliciesSettings.from_dict(response_dict)
            else:
                return ModelAuthenticationPoliciesSettings.from_dict(response.json())

    def updateSettings(self, body: ModelAuthenticationPoliciesSettings):
        """ Set the authentication policies settings.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/authenticationPolicies/settings"),
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
                return ModelAuthenticationPoliciesSettings.from_dict(response_dict)
            else:
                return ModelAuthenticationPoliciesSettings.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)

    def getPolicy(self, id: str):
        """ Get an authentication policy by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/authenticationPolicies/policy/{id}"),
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
                return ModelAuthenticationPolicyTree.from_dict(response_dict)
            else:
                return ModelAuthenticationPolicyTree.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updatePolicy(self, body: ModelAuthenticationPolicyTree, id: str, XBypassExternalValidation: bool = None):
        """ Update an authentication policy.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/authenticationPolicies/policy/{id}"),
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
                self.logger.info("Authentication policy updated.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelAuthenticationPolicyTree.from_dict(response_dict)
            else:
                return ModelAuthenticationPolicyTree.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def deletePolicy(self, id: str):
        """ Delete an authentication policy.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/authenticationPolicies/policy/{id}"),
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
                self.logger.info("Authentication policy deleted.")
                return ModelApiResult(message="Authentication policy deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getFragment(self, id: str):
        """ Get an authentication policy fragment by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/authenticationPolicies/fragments/{id}"),
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
                return ModelAuthenticationPolicyFragment.from_dict(response_dict)
            else:
                return ModelAuthenticationPolicyFragment.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateFragment(self, body: ModelAuthenticationPolicyFragment, id: str, XBypassExternalValidation: bool = None):
        """ Update an authentication policy fragment.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/authenticationPolicies/fragments/{id}"),
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
                self.logger.info("Authentication policy fragment updated.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelAuthenticationPolicyFragment.from_dict(response_dict)
            else:
                return ModelAuthenticationPolicyFragment.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def deleteFragment(self, id: str):
        """ Delete an authentication policy fragment.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/authenticationPolicies/fragments/{id}"),
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
                self.logger.info("Authentication policy fragment deleted.")
                return ModelApiResult(message="Authentication policy fragment deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def createPolicy(self, body: ModelAuthenticationPolicyTree, XBypassExternalValidation: bool = None):
        """ Create a new authentication policy.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/authenticationPolicies/policy"),
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
                self.logger.info("Authentication policy created.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelAuthenticationPolicyTree.from_dict(response_dict)
            else:
                return ModelAuthenticationPolicyTree.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getFragments(self, filter: str = None, numberPerPage: int = None, page: int = None):
        """ Get all of the authentication policies fragments.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/authenticationPolicies/fragments"),
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
                return ModelAuthenticationPolicyFragments.from_dict(response_dict)
            else:
                return ModelAuthenticationPolicyFragments.from_dict(response.json())

    def createFragment(self, body: ModelAuthenticationPolicyFragment, XBypassExternalValidation: bool = None):
        """ Create an authentication policy fragment.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/authenticationPolicies/fragments"),
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
                self.logger.info("Authentication policy fragment created.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelAuthenticationPolicyFragment.from_dict(response_dict)
            else:
                return ModelAuthenticationPolicyFragment.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getDefaultAuthenticationPolicy(self):
        """ Get the default configured authentication policy.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/authenticationPolicies/default"),
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
                return ModelAuthenticationPolicy.from_dict(response_dict)
            else:
                return ModelAuthenticationPolicy.from_dict(response.json())

    def updateDefaultAuthenticationPolicy(self, body: ModelAuthenticationPolicy, XBypassExternalValidation: bool = None):
        """ Set the default authentication policy.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/authenticationPolicies/default"),
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
                self.logger.info("Default authentication policy updated.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelAuthenticationPolicy.from_dict(response_dict)
            else:
                return ModelAuthenticationPolicy.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def movePolicy(self, body: ModelMoveItemRequest, id: str):
        """ Move an authentication policy to a location within the policy tree.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/authenticationPolicies/policy/{id}/move"),
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
                return ModelNone.from_dict(response_dict)
            else:
                return response.json()
            if response.status_code == 422:
                raise ValidationError(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
