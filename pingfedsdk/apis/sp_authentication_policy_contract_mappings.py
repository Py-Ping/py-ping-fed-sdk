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
from pingfedsdk.models.apc_to_sp_adapter_mapping import ApcToSpAdapterMapping as ModelApcToSpAdapterMapping
from pingfedsdk.models.apc_to_sp_adapter_mappings import ApcToSpAdapterMappings as ModelApcToSpAdapterMappings
from pingfedsdk.models.api_result import ApiResult as ModelApiResult


class SpAuthenticationPolicyContractMappings:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.SpAuthenticationPolicyContractMappings")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getApcToSpAdapterMappings(self):
        """ Get the list of APC-to-SP Adapter Mappings.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/sp/authenticationPolicyContractMappings"),
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
                    return ModelApcToSpAdapterMappings.from_dict(response_dict)
                else:
                    return ModelApcToSpAdapterMappings.from_dict(response.json())

    def createApcToSpAdapterMapping(self, body: ModelApcToSpAdapterMapping, XBypassExternalValidation: bool = None):
        """ Create a new APC-to-SP Adapter Mapping.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/sp/authenticationPolicyContractMappings"),
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
                self.logger.info("Authentication policy contract-to-SP adapter mapping created.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelApcToSpAdapterMapping.from_dict(response_dict)
                else:
                    return ModelApcToSpAdapterMapping.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getApcToSpAdapterMappingById(self, id: str):
        """ Get an APC-to-SP Adapter Mapping.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/sp/authenticationPolicyContractMappings/{id}"),
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
                    return ModelApcToSpAdapterMapping.from_dict(response_dict)
                else:
                    return ModelApcToSpAdapterMapping.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateApcToSpAdapterMappingById(self, body: ModelApcToSpAdapterMapping, id: str, XBypassExternalValidation: bool = None):
        """ Update an APC-to-SP Adapter Mapping.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/sp/authenticationPolicyContractMappings/{id}"),
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
                self.logger.info("Authentication policy contract-to-SP adapter mapping updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelApcToSpAdapterMapping.from_dict(response_dict)
                else:
                    return ModelApcToSpAdapterMapping.from_dict(response.json())
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

    def deleteApcToSpAdapterMappingById(self, id: str):
        """ Delete an APC-to-SP Adapter Mapping.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/sp/authenticationPolicyContractMappings/{id}"),
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
                self.logger.info("Authentication policy contract-to-SP adapter mapping deleted.")
                return ModelApiResult(message="Authentication policy contract-to-SP adapter mapping deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)