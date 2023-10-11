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
from pingfedsdk.models.idp_to_sp_adapter_mapping import IdpToSpAdapterMapping as ModelIdpToSpAdapterMapping
from pingfedsdk.models.idp_to_sp_adapter_mappings import IdpToSpAdapterMappings as ModelIdpToSpAdapterMappings


class IdpToSpAdapterMapping:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.IdpToSpAdapterMapping")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getIdpToSpAdapterMappings(self):
        """ Get list of IdP-to-SP Adapter Mappings.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/idpToSpAdapterMapping"),
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
                    return ModelIdpToSpAdapterMappings.from_dict(response_dict)
                else:
                    return ModelIdpToSpAdapterMappings.from_dict(response.json())

    def createIdpToSpAdapterMapping(self, body: ModelIdpToSpAdapterMapping, XBypassExternalValidation: bool = None):
        """ Create a new IdP-to-SP Adapter mapping.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/idpToSpAdapterMapping"),
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
                self.logger.info("IdP-to-SP adapter mapping created.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelIdpToSpAdapterMapping.from_dict(response_dict)
                else:
                    return ModelIdpToSpAdapterMapping.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getIdpToSpAdapterMappingsById(self, id: str):
        """ Get an IdP-to-SP Adapter Mapping.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/idpToSpAdapterMapping/{id}"),
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
                    return ModelIdpToSpAdapterMapping.from_dict(response_dict)
                else:
                    return ModelIdpToSpAdapterMapping.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateIdpToSpAdapterMapping(self, body: ModelIdpToSpAdapterMapping, id: str, XBypassExternalValidation: bool = None):
        """ Update the specified IdP-to-SP Adapter mapping.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/idpToSpAdapterMapping/{id}"),
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
                self.logger.info("IdP-to-SP adapter mapping updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelIdpToSpAdapterMapping.from_dict(response_dict)
                else:
                    return ModelIdpToSpAdapterMapping.from_dict(response.json())
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

    def deleteIdpToSpAdapterMappingsById(self, id: str):
        """ Delete an Adapter to Adapter Mapping.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/idpToSpAdapterMapping/{id}"),
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
                self.logger.info("IdP-to-SP adapter mapping deleted.")
                return ModelApiResult(message="IdP-to-SP adapter mapping deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
