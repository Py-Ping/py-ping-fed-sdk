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
from pingfedsdk.models.token_exchange_generator_group import TokenExchangeGeneratorGroup as ModelTokenExchangeGeneratorGroup
from pingfedsdk.models.token_exchange_generator_groups import TokenExchangeGeneratorGroups as ModelTokenExchangeGeneratorGroups
from pingfedsdk.models.token_exchange_generator_settings import TokenExchangeGeneratorSettings as ModelTokenExchangeGeneratorSettings


class OauthTokenExchangeGenerator:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.OauthTokenExchangeGenerator")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getSettings(self):
        """ Get general OAuth 2.0 Token Exchange Generator settings.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/oauth/tokenExchange/generator/settings"),
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
                    return ModelTokenExchangeGeneratorSettings.from_dict(response_dict)
                else:
                    return ModelTokenExchangeGeneratorSettings.from_dict(response.json())

    def updateSettings(self, body: ModelTokenExchangeGeneratorSettings, bypassExternalValidation: bool = None):
        """ Update general OAuth 2.0 Token Exchange Generator settings.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/oauth/tokenExchange/generator/settings"),
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
                    return ModelTokenExchangeGeneratorSettings.from_dict(response_dict)
                else:
                    return ModelTokenExchangeGeneratorSettings.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getGroups(self):
        """ Get list of OAuth 2.0 Token Exchange Generator groups.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/oauth/tokenExchange/generator/groups"),
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
                    return ModelTokenExchangeGeneratorGroups.from_dict(response_dict)
                else:
                    return ModelTokenExchangeGeneratorGroups.from_dict(response.json())

    def createGroup(self, body: ModelTokenExchangeGeneratorGroup, bypassExternalValidation: bool = None):
        """ Create a new OAuth 2.0 Token Exchange Generator group.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/oauth/tokenExchange/generator/groups"),
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
                self.logger.info("Token Exchange Processor Policy created.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelTokenExchangeGeneratorGroup.from_dict(response_dict)
                else:
                    return ModelTokenExchangeGeneratorGroup.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getGroup(self, id: str):
        """ Find an OAuth 2.0 Token Exchange Generator group by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/oauth/tokenExchange/generator/groups/{id}"),
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
                    return ModelTokenExchangeGeneratorGroup.from_dict(response_dict)
                else:
                    return ModelTokenExchangeGeneratorGroup.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateGroup(self, body: ModelTokenExchangeGeneratorGroup, id: str, bypassExternalValidation: bool = None):
        """ Update an OAuth 2.0 Token Exchange Generator group.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/oauth/tokenExchange/generator/groups/{id}"),
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
                self.logger.info("Token Exchange Processor Policy updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelTokenExchangeGeneratorGroup.from_dict(response_dict)
                else:
                    return ModelTokenExchangeGeneratorGroup.from_dict(response.json())
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

    def deleteGroup(self, id: str):
        """ Delete an OAuth 2.0 Token Exchange Generator group.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/oauth/tokenExchange/generator/groups/{id}"),
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
                self.logger.info("Token Exchange Processor Policy deleted.")
                return ModelApiResult(message="Token Exchange Processor Policy deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())
