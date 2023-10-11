from json import dumps
import logging
import os
import traceback

from requests import Session
from requests.exceptions import HTTPError

from pingfedsdk.exceptions import BadRequest
from pingfedsdk.exceptions import ValidationError
from pingfedsdk.models.api_result import ApiResult as ModelApiResult
from pingfedsdk.models.convert_metadata_request import ConvertMetadataRequest as ModelConvertMetadataRequest
from pingfedsdk.models.convert_metadata_response import ConvertMetadataResponse as ModelConvertMetadataResponse
from pingfedsdk.models.export_metadata_request import ExportMetadataRequest as ModelExportMetadataRequest


class ConnectionMetadata:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.ConnectionMetadata")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def convert(self, body: ModelConvertMetadataRequest):
        """ Convert a partner's SAML metadata into a JSON representation.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/connectionMetadata/convert"),
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
                self.logger.info("Partner's SAML metadata converted.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return ModelConvertMetadataResponse.from_dict(response_dict)
            else:
                return ModelConvertMetadataResponse.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def export(self, body: ModelExportMetadataRequest):
        """ Export a connection's SAML metadata that can be given to a partner.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/connectionMetadata/export"),
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
                self.logger.info("Connection SAML metadata exported.")
            if isinstance(response.json(), list):
                response_dict = {'items': response.json()}
                return Modelstr.from_dict(response_dict)
            else:
                return str(response)
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())
