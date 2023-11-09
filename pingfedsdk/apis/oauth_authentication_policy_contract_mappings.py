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
from pingfedsdk.models.apc_to_persistent_grant_mapping import ApcToPersistentGrantMapping as ModelApcToPersistentGrantMapping
from pingfedsdk.models.apc_to_persistent_grant_mappings import ApcToPersistentGrantMappings as ModelApcToPersistentGrantMappings
from pingfedsdk.models.api_result import ApiResult as ModelApiResult


class OauthAuthenticationPolicyContractMappings:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.OauthAuthenticationPolicyContractMappings")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getApcMappings(self):
        """ Get the list of authentication policy contract to persistent grant mappings.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/oauth/authenticationPolicyContractMappings"),
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
                    return ModelApcToPersistentGrantMappings.from_dict(response_dict)
                else:
                    return ModelApcToPersistentGrantMappings.from_dict(response.json())

    def createApcMapping(self, body: ModelApcToPersistentGrantMapping, XBypassExternalValidation: bool = None):
        """ Create a new authentication policy contract to persistent grant mapping.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/oauth/authenticationPolicyContractMappings"),
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
                self.logger.info("Authentication policy contract to persistent grant mapping created.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelApcToPersistentGrantMapping.from_dict(response_dict)
                else:
                    return ModelApcToPersistentGrantMapping.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getApcMapping(self, id: str):
        """ Find the authentication policy contract to persistent grant mapping by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/oauth/authenticationPolicyContractMappings/{id}"),
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
                    return ModelApcToPersistentGrantMapping.from_dict(response_dict)
                else:
                    return ModelApcToPersistentGrantMapping.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateApcMapping(self, body: ModelApcToPersistentGrantMapping, id: str, XBypassExternalValidation: bool = None):
        """ Update an authentication policy contract to persistent grant mapping.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/oauth/authenticationPolicyContractMappings/{id}"),
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
                self.logger.info("Authentication policy contract to persistent grant mapping updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelApcToPersistentGrantMapping.from_dict(response_dict)
                else:
                    return ModelApcToPersistentGrantMapping.from_dict(response.json())
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

    def deleteApcMapping(self, id: str):
        """ Delete an authentication policy contract to persistent grant mapping.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/oauth/authenticationPolicyContractMappings/{id}"),
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
                self.logger.info("Authentication policy contract to persistent grant mapping deleted.")
                return ModelApiResult(message="Authentication policy contract to persistent grant mapping deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)