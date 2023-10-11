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
from pingfedsdk.models.authentication_selector import AuthenticationSelector as ModelAuthenticationSelector
from pingfedsdk.models.authentication_selector_descriptor import AuthenticationSelectorDescriptor as ModelAuthenticationSelectorDescriptor
from pingfedsdk.models.authentication_selector_descriptors import AuthenticationSelectorDescriptors as ModelAuthenticationSelectorDescriptors
from pingfedsdk.models.authentication_selectors import AuthenticationSelectors as ModelAuthenticationSelectors


class AuthenticationSelectors:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.AuthenticationSelectors")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getAuthenticationSelector(self, id: str):
        """ Get an Authentication Selector instance by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/authenticationSelectors/{id}"),
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
                    return ModelAuthenticationSelector.from_dict(response_dict)
                else:
                    return ModelAuthenticationSelector.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateAuthenticationSelector(self, body: ModelAuthenticationSelector, id: str):
        """ Update an authentication selector instance.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/authenticationSelectors/{id}"),
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
                self.logger.info("Authentication selector updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelAuthenticationSelector.from_dict(response_dict)
                else:
                    return ModelAuthenticationSelector.from_dict(response.json())
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

    def deleteAuthenticationSelector(self, id: str):
        """ Delete an Authentication Selector instance.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/authenticationSelectors/{id}"),
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
                self.logger.info("Authentication selector deleted.")
                return ModelApiResult(message="Authentication selector deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getAuthenticationSelectorDescriptors(self):
        """ Get the list of available Authentication Selector descriptors.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/authenticationSelectors/descriptors"),
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
                    return ModelAuthenticationSelectorDescriptors.from_dict(response_dict)
                else:
                    return ModelAuthenticationSelectorDescriptors.from_dict(response.json())

    def getAuthenticationSelectorDescriptorsById(self, id: str):
        """ Get the description of an Authentication Selector plugin by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/authenticationSelectors/descriptors/{id}"),
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
                    return ModelAuthenticationSelectorDescriptor.from_dict(response_dict)
                else:
                    return ModelAuthenticationSelectorDescriptor.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getAuthenticationSelectors(self, filter: str = None, numberPerPage: int = None, page: int = None):
        """ Get the list of configured Authentication Selector instances.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/authenticationSelectors"),
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
                    return ModelAuthenticationSelectors.from_dict(response_dict)
                else:
                    return ModelAuthenticationSelectors.from_dict(response.json())
            if response.status_code == 422:
                raise ValidationError(response.json())

    def createAuthenticationSelector(self, body: ModelAuthenticationSelector):
        """ Create a new authentication selector instance.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/authenticationSelectors"),
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
                self.logger.info("Authentication selector created.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelAuthenticationSelector.from_dict(response_dict)
                else:
                    return ModelAuthenticationSelector.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())
