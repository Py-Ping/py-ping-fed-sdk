import os
import logging
import traceback

from json import dumps
from requests import Session
from requests.exceptions import HTTPError
from pingfedsdk.exceptions import ValidationError
from pingfedsdk.exceptions import NotImplementedError
from pingfedsdk.exceptions import ObjectDeleted
from pingfedsdk.exceptions import BadRequest
from pingfedsdk.exceptions import NotFound
from pingfedsdk.models.config_store_setting import ConfigStoreSetting as ModelConfigStoreSetting
from pingfedsdk.models.api_result import ApiResult as ModelApiResult
from pingfedsdk.models.config_store_bundle import ConfigStoreBundle as ModelConfigStoreBundle


class ConfigStore:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.ConfigStore")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getSetting(self, bundle: str, id: str):
        """ Get a single setting from a bundle.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/configStore/{bundle}/{id}"),
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
                return ModelConfigStoreSetting.from_dict(response.json())
            if response.status_code == 403:
                message = "(403) The specified configuration bundle is unavailable."
                self.logger.info(message)
                raise NotImplementedError(message)
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateSetting(self, bundle: str, id: str, body: ModelConfigStoreSetting):
        """ Create or update a setting/bundle.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/configStore/{bundle}/{id}"),
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
                return ModelConfigStoreSetting.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 403:
                message = "(403) The specified configuration bundle is unavailable."
                self.logger.info(message)
                raise NotImplementedError(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def deleteSetting(self, bundle: str, id: str):
        """ Delete a setting.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/configStore/{bundle}/{id}"),
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
                message = "(204) Configuration setting deleted."
                self.logger.info(message)
                raise ObjectDeleted(message)
            if response.status_code == 403:
                message = "(403) The specified configuration bundle is unavailable."
                self.logger.info(message)
                raise NotImplementedError(message)
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getSettings(self, bundle: str):
        """ Get all settings from a bundle.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/configStore/{bundle}"),
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
                return ModelConfigStoreBundle.from_dict(response.json())
            if response.status_code == 403:
                message = "(403) The specified configuration bundle is unavailable."
                self.logger.info(message)
                raise NotImplementedError(message)
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
