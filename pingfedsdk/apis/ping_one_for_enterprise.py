from json import dumps
import logging
import os
import traceback

from requests import Session
from requests.exceptions import HTTPError

from pingfedsdk.exceptions import NotImplementedError
from pingfedsdk.exceptions import ValidationError
from pingfedsdk.models.api_result import ApiResult as ModelApiResult
from pingfedsdk.models.p_1_4_e_keys_view import P14EKeysView as ModelP14EKeysView
from pingfedsdk.models.ping_one_for_enterprise_settings import PingOneForEnterpriseSettings as ModelPingOneForEnterpriseSettings


class PingOneForEnterprise:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.PingOneForEnterprise")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def disconnect(self):
        """ Disconnect from PingOne for Enterprise
        """

        try:
            response = self.session.post(
                url=self._build_uri("/pingOneForEnterprise/disconnect"),
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
                self.logger.info("Disconnected from PingOne for Enterprise")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelPingOneForEnterpriseSettings.from_dict(response_dict)
                else:
                    return ModelPingOneForEnterpriseSettings.from_dict(response.json())
            if response.status_code == 403:
                message = "(403) PingFederate is not connected to PingOne for Enterprise. Operation not available."
                self.logger.info(message)
                raise NotImplementedError(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getPingOneForEnterpriseSettings(self):
        """ Get the PingOne for Enterprise settings
        """

        try:
            response = self.session.get(
                url=self._build_uri("/pingOneForEnterprise"),
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
                    return ModelPingOneForEnterpriseSettings.from_dict(response_dict)
                else:
                    return ModelPingOneForEnterpriseSettings.from_dict(response.json())
            if response.status_code == 403:
                message = "(403) PingFederate is not connected to PingOne for Enterprise. Operation not available."
                self.logger.info(message)
                raise NotImplementedError(message)

    def updatePingOneSettings(self, body: ModelPingOneForEnterpriseSettings):
        """ Update the PingOne for Enterprise settings.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/pingOneForEnterprise"),
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
                    return ModelPingOneForEnterpriseSettings.from_dict(response_dict)
                else:
                    return ModelPingOneForEnterpriseSettings.from_dict(response.json())
            if response.status_code == 403:
                message = "(403) PingFederate is not connected to PingOne for Enterprise. Operation not available."
                self.logger.info(message)
                raise NotImplementedError(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def updatePingOneForEnterpriseIdentityRepository(self):
        """ Update the PingOne Identity Repository
        """

        try:
            response = self.session.post(
                url=self._build_uri("/pingOneForEnterprise/updateIdentityRepository"),
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
                    return ModelPingOneForEnterpriseSettings.from_dict(response_dict)
                else:
                    return ModelPingOneForEnterpriseSettings.from_dict(response.json())
            if response.status_code == 403:
                message = "(403) PingFederate is not connected to PingOne for Enterprise. Operation not available."
                self.logger.info(message)
                raise NotImplementedError(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def rotateKeys(self):
        """ Rotate the authentication key
        """

        try:
            response = self.session.post(
                url=self._build_uri("/pingOneForEnterprise/keyPairs/rotate"),
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
                    return ModelP14EKeysView.from_dict(response_dict)
                else:
                    return ModelP14EKeysView.from_dict(response.json())
            if response.status_code == 403:
                message = "(403) PingFederate is not connected to PingOne for Enterprise. Operation not available."
                self.logger.info(message)
                raise NotImplementedError(message)

    def getKeyPairs(self):
        """ Get the PingOne for Enterprise key pair settings
        """

        try:
            response = self.session.get(
                url=self._build_uri("/pingOneForEnterprise/keyPairs"),
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
                    return ModelP14EKeysView.from_dict(response_dict)
                else:
                    return ModelP14EKeysView.from_dict(response.json())
            if response.status_code == 403:
                message = "(403) PingFederate is not connected to PingOne for Enterprise. Operation not available."
                self.logger.info(message)
                raise NotImplementedError(message)
