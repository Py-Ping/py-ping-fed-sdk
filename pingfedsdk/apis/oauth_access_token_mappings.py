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
from pingfedsdk.models.access_token_mapping import AccessTokenMapping as ModelAccessTokenMapping
from pingfedsdk.models.access_token_mappings import AccessTokenMappings as ModelAccessTokenMappings
from pingfedsdk.models.api_result import ApiResult as ModelApiResult


class OauthAccessTokenMappings:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.OauthAccessTokenMappings")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getMapping(self, id: str):
        """ Find the Access Token Mapping by its ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/oauth/accessTokenMappings/{id}"),
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
                    return ModelAccessTokenMapping.from_dict(response_dict)
                else:
                    return ModelAccessTokenMapping.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateMapping(self, body: ModelAccessTokenMapping, id: str, XBypassExternalValidation: bool = None):
        """ Update an Access Token Mapping.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/oauth/accessTokenMappings/{id}"),
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
                self.logger.info("Access token attribute mapping updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelAccessTokenMapping.from_dict(response_dict)
                else:
                    return ModelAccessTokenMapping.from_dict(response.json())
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

    def deleteMapping(self, id: str):
        """ Delete an Access Token Mapping.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/oauth/accessTokenMappings/{id}"),
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
                self.logger.info("Access token attribute mapping deleted.")
                return ModelApiResult(message="Access token attribute mapping deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getMappings(self):
        """ Get the list of Access Token Mappings.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/oauth/accessTokenMappings"),
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
                    return ModelAccessTokenMappings.from_dict(response_dict)
                else:
                    return ModelAccessTokenMappings.from_dict(response.json())

    def createMapping(self, body: ModelAccessTokenMapping, XBypassExternalValidation: bool = None):
        """ Create a new Access Token Mapping.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/oauth/accessTokenMappings"),
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
                self.logger.info("Access token attribute mapping created.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelAccessTokenMapping.from_dict(response_dict)
                else:
                    return ModelAccessTokenMapping.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())