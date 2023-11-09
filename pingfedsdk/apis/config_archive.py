from json import dumps
import logging
import os
from tempfile import SpooledTemporaryFile
import traceback

from requests import Session
from requests.exceptions import HTTPError

from pingfedsdk.exceptions import ValidationError
from pingfedsdk.models.api_result import ApiResult as ModelApiResult


class ConfigArchive:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.ConfigArchive")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def importConfigArchive(self, file: SpooledTemporaryFile, forceImport: bool = None, forceUnsupportedImport: bool = None, reencryptData: bool = None):
        """ Import a configuration archive.
        """

        try:
            response = self.session.post(
                files={'file': file},
                url=self._build_uri("/configArchive/import"),
                headers={"Accept": "application/json"}
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
                self.logger.info("Configuration Archive imported.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelApiResult.from_dict(response.json())
                else:
                    return ModelApiResult.from_dict(response.json())
            elif response.status_code in (400, 415, 422):
                raise ValidationError(response.json())

    def exportConfigArchive(self):
        """ Export a configuration archive.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/configArchive/export"),
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
                return response