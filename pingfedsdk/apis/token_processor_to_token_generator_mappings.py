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
from pingfedsdk.models.token_to_token_mapping import TokenToTokenMapping as ModelTokenToTokenMapping
from pingfedsdk.models.token_to_token_mappings import TokenToTokenMappings as ModelTokenToTokenMappings


class TokenProcessorToTokenGeneratorMappings:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.TokenProcessorToTokenGeneratorMappings")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getTokenToTokenMappings(self):
        """ Get the list of Token Processor to Token Generator Mappings.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/tokenProcessorToTokenGeneratorMappings"),
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
                return ModelTokenToTokenMappings.from_dict(response_dict)
            else:
                return ModelTokenToTokenMappings.from_dict(response.json())

    def createTokenToTokenMapping(self, body: ModelTokenToTokenMapping, XBypassExternalValidation: bool = None):
        """ Create a new Token Processor to Token Generator Mapping.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/tokenProcessorToTokenGeneratorMappings"),
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
                self.logger.info("Token Processor to Token Generator mapping created.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelTokenToTokenMapping.from_dict(response_dict)
            else:
                return ModelTokenToTokenMapping.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getTokenToTokenMappingById(self, id: str):
        """ Get a Token Processor to Token Generator Mapping.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/tokenProcessorToTokenGeneratorMappings/{id}"),
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
                return ModelTokenToTokenMapping.from_dict(response_dict)
            else:
                return ModelTokenToTokenMapping.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateTokenToTokenMappingById(self, body: ModelTokenToTokenMapping, id: str, XBypassExternalValidation: bool = None):
        """ Update a Token Processor to Token Generator Mapping.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/tokenProcessorToTokenGeneratorMappings/{id}"),
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
                self.logger.info("Token Processor to Token Generator mapping updated.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelTokenToTokenMapping.from_dict(response_dict)
            else:
                return ModelTokenToTokenMapping.from_dict(response.json())
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

    def deleteTokenToTokenMappingById(self, id: str):
        """ Delete a Token Processor to Token Generator Mapping.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/tokenProcessorToTokenGeneratorMappings/{id}"),
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
                self.logger.info("Token Processor to Token Generator mapping deleted.")
                return ModelApiResult(message="Token Processor to Token Generator mapping deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
