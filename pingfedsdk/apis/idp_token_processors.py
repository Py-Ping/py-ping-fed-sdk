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
from pingfedsdk.models.token_processor import TokenProcessor as ModelTokenProcessor
from pingfedsdk.models.token_processor_descriptor import TokenProcessorDescriptor as ModelTokenProcessorDescriptor
from pingfedsdk.models.token_processor_descriptors import TokenProcessorDescriptors as ModelTokenProcessorDescriptors
from pingfedsdk.models.token_processors import TokenProcessors as ModelTokenProcessors


class IdpTokenProcessors:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.IdpTokenProcessors")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getTokenProcessor(self, id: str):
        """ Find a token processor instance by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/idp/tokenProcessors/{id}"),
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
                return ModelTokenProcessor.from_dict(response_dict)
            else:
                return ModelTokenProcessor.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateTokenProcessor(self, body: ModelTokenProcessor, id: str):
        """ Update a token processor instance.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/idp/tokenProcessors/{id}"),
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
                self.logger.info("Token Processor updated.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelTokenProcessor.from_dict(response_dict)
            else:
                return ModelTokenProcessor.from_dict(response.json())
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

    def deleteTokenProcessor(self, id: str):
        """ Delete a token processor instance.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/idp/tokenProcessors/{id}"),
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
                self.logger.info("Token processor deleted.")
                return ModelApiResult(message="Token processor deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getTokenProcessorDescriptors(self):
        """ Get the list of available token processors.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/idp/tokenProcessors/descriptors"),
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
                return ModelTokenProcessorDescriptors.from_dict(response_dict)
            else:
                return ModelTokenProcessorDescriptors.from_dict(response.json())

    def getTokenProcessorDescriptorsById(self, id: str):
        """ Get the description of a token processor plugin by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/idp/tokenProcessors/descriptors/{id}"),
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
                return ModelTokenProcessorDescriptor.from_dict(response_dict)
            else:
                return ModelTokenProcessorDescriptor.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getTokenProcessors(self):
        """ Get the list of token processor instances.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/idp/tokenProcessors"),
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
                return ModelTokenProcessors.from_dict(response_dict)
            else:
                return ModelTokenProcessors.from_dict(response.json())

    def createTokenProcessor(self, body: ModelTokenProcessor):
        """ Create a new token processor instance.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/idp/tokenProcessors"),
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
                self.logger.info("Token processor created.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelTokenProcessor.from_dict(response_dict)
            else:
                return ModelTokenProcessor.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())
