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
from pingfedsdk.models.api_response import ApiResponse as ModelApiResponse
from pingfedsdk.models.api_result import ApiResult as ModelApiResult
from pingfedsdk.models.captcha_settings import CaptchaSettings as ModelCaptchaSettings
from pingfedsdk.models.email_server_settings import EmailServerSettings as ModelEmailServerSettings
from pingfedsdk.models.general_settings import GeneralSettings as ModelGeneralSettings
from pingfedsdk.models.issuer_cert import IssuerCert as ModelIssuerCert
from pingfedsdk.models.issuer_certs import IssuerCerts as ModelIssuerCerts
from pingfedsdk.models.notification_settings import NotificationSettings as ModelNotificationSettings
from pingfedsdk.models.outbound_provision_database import OutboundProvisionDatabase as ModelOutboundProvisionDatabase
from pingfedsdk.models.server_settings import ServerSettings as ModelServerSettings
from pingfedsdk.models.system_keys import SystemKeys as ModelSystemKeys
from pingfedsdk.models.ws_trust_sts_settings import WsTrustStsSettings as ModelWsTrustStsSettings
from pingfedsdk.models.x_5_0_9_file import X509File as ModelX509File


class ServerSettings:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.ServerSettings")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getCerts(self):
        """ Get the list of certificates for WS-Trust STS Settings.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/serverSettings/wsTrustStsSettings/issuerCertificates"),
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
                    return ModelIssuerCerts.from_dict(response_dict)
                else:
                    return ModelIssuerCerts.from_dict(response.json())

    def importCertificate(self, body: ModelX509File):
        """ Import a new certificate.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/serverSettings/wsTrustStsSettings/issuerCertificates"),
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
                self.logger.info("New certificate has been imported to WS-Trust STS Settings")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelApiResponse.from_dict(response_dict)
                else:
                    return ModelApiResponse.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getCaptchaSettings(self):
        """ Gets the CAPTCHA settings.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/serverSettings/captchaSettings"),
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
                    return ModelCaptchaSettings.from_dict(response_dict)
                else:
                    return ModelCaptchaSettings.from_dict(response.json())

    def updateCaptchaSettings(self, body: ModelCaptchaSettings):
        """ Update the CAPTCHA settings.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/serverSettings/captchaSettings"),
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
                self.logger.info("Captcha settings updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelCaptchaSettings.from_dict(response_dict)
                else:
                    return ModelCaptchaSettings.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getNotificationSettings(self):
        """ Gets the notification settings
        """

        try:
            response = self.session.get(
                url=self._build_uri("/serverSettings/notifications"),
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
                    return ModelNotificationSettings.from_dict(response_dict)
                else:
                    return ModelNotificationSettings.from_dict(response.json())

    def updateNotificationSettings(self, body: ModelNotificationSettings):
        """ Update the notification settings.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/serverSettings/notifications"),
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
                self.logger.info("Notifications updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelNotificationSettings.from_dict(response_dict)
                else:
                    return ModelNotificationSettings.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getCert(self, id: str):
        """ Retrieve details of a certificate.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/serverSettings/wsTrustStsSettings/issuerCertificates/{id}"),
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
                    return ModelApiResponse.from_dict(response_dict)
                else:
                    return ModelApiResponse.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def deleteCertificate(self, id: str):
        """ Delete a certificate from WS-Trust STS Settings.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/serverSettings/wsTrustStsSettings/issuerCertificates/{id}"),
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
                self.logger.info("Certificate has been deleted from WS-Trust STS Settings")
                return ModelApiResult(message="Certificate has been deleted from WS-Trust STS Settings", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getServerSettings(self):
        """ Gets the server settings
        """

        try:
            response = self.session.get(
                url=self._build_uri("/serverSettings"),
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
                    return ModelServerSettings.from_dict(response_dict)
                else:
                    return ModelServerSettings.from_dict(response.json())

    def updateServerSettings(self, body: ModelServerSettings):
        """ Update the server settings.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/serverSettings"),
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
                self.logger.info("Server Settings updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelServerSettings.from_dict(response_dict)
                else:
                    return ModelServerSettings.from_dict(response.json())
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

    def getEmailServerSettings(self):
        """ (Deprecated) Gets the email server settings
        """

        try:
            response = self.session.get(
                url=self._build_uri("/serverSettings/emailServer"),
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
                    return ModelEmailServerSettings.from_dict(response_dict)
                else:
                    return ModelEmailServerSettings.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateEmailServerSettings(self, body: ModelEmailServerSettings, validateOnly: bool = None, validationEmail: str = None):
        """ (Deprecated) Update the email server settings
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/serverSettings/emailServer"),
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
                self.logger.info("Email Server updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelEmailServerSettings.from_dict(response_dict)
                else:
                    return ModelEmailServerSettings.from_dict(response.json())
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

    def getSystemKeys(self):
        """ Get the system keys.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/serverSettings/systemKeys"),
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
                    return ModelSystemKeys.from_dict(response_dict)
                else:
                    return ModelSystemKeys.from_dict(response.json())

    def updateSystemKeys(self, body: ModelSystemKeys):
        """ Update the system keys.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/serverSettings/systemKeys"),
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
                self.logger.info("System keys updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelSystemKeys.from_dict(response_dict)
                else:
                    return ModelSystemKeys.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def rotateSystemKeys(self):
        """ Rotate the system keys.
        """

        try:
            response = self.session.post(
                url=self._build_uri("/serverSettings/systemKeys/rotate"),
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
                self.logger.info("successful operation")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelSystemKeys.from_dict(response_dict)
                else:
                    return ModelSystemKeys.from_dict(response.json())
            if response.status_code == 201:
                self.logger.info("System Keys rotated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelSystemKeys.from_dict(response_dict)
                else:
                    return ModelSystemKeys.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getOutBoundProvisioningSettings(self):
        """ Get database used for outbound provisioning
        """

        try:
            response = self.session.get(
                url=self._build_uri("/serverSettings/outboundProvisioning"),
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
                    return ModelOutboundProvisionDatabase.from_dict(response_dict)
                else:
                    return ModelOutboundProvisionDatabase.from_dict(response.json())

    def updateOutBoundProvisioningSettings(self, body: ModelOutboundProvisionDatabase):
        """ Update database used for outbound provisioning
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/serverSettings/outboundProvisioning"),
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
                self.logger.info("Database updated for outbound provisioning.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelOutboundProvisionDatabase.from_dict(response_dict)
                else:
                    return ModelOutboundProvisionDatabase.from_dict(response.json())
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getWsTrustStsSettings(self):
        """ Get the current WS-Trust STS Settings.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/serverSettings/wsTrustStsSettings"),
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
                    return ModelWsTrustStsSettings.from_dict(response_dict)
                else:
                    return ModelWsTrustStsSettings.from_dict(response.json())

    def updateWsTrustStsSettings(self, body: ModelWsTrustStsSettings):
        """ Update WS-Trust STS Settings.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/serverSettings/wsTrustStsSettings"),
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
                self.logger.info("Server Settings updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelWsTrustStsSettings.from_dict(response_dict)
                else:
                    return ModelWsTrustStsSettings.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getGeneralSettings(self):
        """ Gets the general settings.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/serverSettings/generalSettings"),
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
                    return ModelGeneralSettings.from_dict(response_dict)
                else:
                    return ModelGeneralSettings.from_dict(response.json())

    def updateGeneralSettings(self, body: ModelGeneralSettings):
        """ Update general settings.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/serverSettings/generalSettings"),
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
                self.logger.info("General settings have been updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelGeneralSettings.from_dict(response_dict)
                else:
                    return ModelGeneralSettings.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())
