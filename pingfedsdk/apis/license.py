from json import dumps
import logging
import os
import traceback

from requests import Session
from requests.exceptions import HTTPError

from pingfedsdk.exceptions import NotFound
from pingfedsdk.exceptions import ValidationError
from pingfedsdk.models.api_result import ApiResult as ModelApiResult
from pingfedsdk.models.license_agreement_info import LicenseAgreementInfo as ModelLicenseAgreementInfo
from pingfedsdk.models.license_file import LicenseFile as ModelLicenseFile
from pingfedsdk.models.license_view import LicenseView as ModelLicenseView


class License:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.License")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getLicense(self):
        """ Get a license summary.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/license"),
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
                    return ModelLicenseView.from_dict(response_dict)
                else:
                    return ModelLicenseView.from_dict(response.json())
            if response.status_code == 422:
                raise ValidationError(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateLicense(self, body: ModelLicenseFile):
        """ Import a license.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/license"),
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
                self.logger.info("License imported.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelLicenseView.from_dict(response_dict)
                else:
                    return ModelLicenseView.from_dict(response.json())
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getLicenseAgreement(self):
        """ Get license agreement link.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/license/agreement"),
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
                    return ModelLicenseAgreementInfo.from_dict(response_dict)
                else:
                    return ModelLicenseAgreementInfo.from_dict(response.json())
            if response.status_code == 422:
                raise ValidationError(response.json())

    def updateLicenseAgreement(self, body: ModelLicenseAgreementInfo):
        """ Accept license agreement.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/license/agreement"),
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
                self.logger.info("License agreement accepted.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelLicenseAgreementInfo.from_dict(response_dict)
                else:
                    return ModelLicenseAgreementInfo.from_dict(response.json())
            if response.status_code == 422:
                raise ValidationError(response.json())
