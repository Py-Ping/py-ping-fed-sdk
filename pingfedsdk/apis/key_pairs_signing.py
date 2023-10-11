from json import dumps
import logging
import os
import traceback

from requests import Session
from requests.exceptions import HTTPError

from pingfedsdk.exceptions import BadRequest
from pingfedsdk.exceptions import NotFound
from pingfedsdk.exceptions import NotImplementedError
from pingfedsdk.exceptions import ObjectDeleted
from pingfedsdk.exceptions import ValidationError
from pingfedsdk.models.api_result import ApiResult as ModelApiResult
from pingfedsdk.models.c_s_r_response import CSRResponse as ModelCSRResponse
from pingfedsdk.models.key_pair_export_settings import KeyPairExportSettings as ModelKeyPairExportSettings
from pingfedsdk.models.key_pair_file import KeyPairFile as ModelKeyPairFile
from pingfedsdk.models.key_pair_rotation_settings import KeyPairRotationSettings as ModelKeyPairRotationSettings
from pingfedsdk.models.key_pair_view import KeyPairView as ModelKeyPairView
from pingfedsdk.models.key_pair_views import KeyPairViews as ModelKeyPairViews
from pingfedsdk.models.new_key_pair_settings import NewKeyPairSettings as ModelNewKeyPairSettings


class KeyPairsSigning:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.KeyPairsSigning")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getRotationSettings(self, id: str):
        """ Retrieve details of rotation settings for a key pair.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/keyPairs/signing/{id}/rotationSettings"),
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
                    return ModelKeyPairRotationSettings.from_dict(response_dict)
                else:
                    return ModelKeyPairRotationSettings.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateRotationSettings(self, body: ModelKeyPairRotationSettings, id: str):
        """ Add rotation settings to a key pair
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/keyPairs/signing/{id}/rotationSettings"),
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
                self.logger.info("Key Pair updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelKeyPairRotationSettings.from_dict(response_dict)
                else:
                    return ModelKeyPairRotationSettings.from_dict(response.json())
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

    def deleteKeyPairRotationSettings(self, id: str):
        """ Delete rotation settings for a signing key pair.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/keyPairs/signing/{id}/rotationSettings"),
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
                self.logger.info("Rotation Settings deleted.")
                return ModelApiResult(message="Rotation Settings deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def importKeyPair(self, body: ModelKeyPairFile):
        """ Import a new key pair.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/keyPairs/signing/import"),
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
                self.logger.info("Key Pair imported.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelKeyPairView.from_dict(response_dict)
                else:
                    return ModelKeyPairView.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 403:
                message = "(403) The operation is not permitted, based on the current configuration of the server."
                self.logger.info(message)
                raise NotImplementedError(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getKeyPair(self, id: str):
        """ Retrieve details of a key pair.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/keyPairs/signing/{id}"),
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
                    return ModelKeyPairView.from_dict(response_dict)
                else:
                    return ModelKeyPairView.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def deleteKeyPair(self, id: str):
        """ Delete a key pair.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/keyPairs/signing/{id}"),
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
                self.logger.info("Key Pair deleted.")
                return ModelApiResult(message="Key Pair deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getKeyPairs(self):
        """ Get list of key pairs.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/keyPairs/signing"),
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
                    return ModelKeyPairViews.from_dict(response_dict)
                else:
                    return ModelKeyPairViews.from_dict(response.json())

    def createKeyPair(self, body: ModelNewKeyPairSettings):
        """ Generate a new key pair.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/keyPairs/signing/generate"),
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
                self.logger.info("Key Pair created.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelKeyPairView.from_dict(response_dict)
                else:
                    return ModelKeyPairView.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def exportCsr(self, id: str):
        """ Generate a new certificate signing request (CSR) for this key pair.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/keyPairs/signing/{id}/csr"),
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
                    return Modelstr.from_dict(response_dict)
                else:
                    return str(response)

    def importCsrResponse(self, body: ModelCSRResponse, id: str):
        """ Import a CSR response for this key pair.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/keyPairs/signing/{id}/csr"),
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
                self.logger.info("CSR Response imported.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelKeyPairView.from_dict(response_dict)
                else:
                    return ModelKeyPairView.from_dict(response.json())
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

    def exportPKCS12File(self, body: ModelKeyPairExportSettings, id: str):
        """ Download the key pair in PKCS12 format.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/keyPairs/signing/{id}/pkcs12"),
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
                self.logger.info("Key Pair downloaded.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return Modelstr.from_dict(response_dict)
                else:
                    return str(response)
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 403:
                message = "(403) The operation is not permitted, based on the current configuration of the server."
                self.logger.info(message)
                raise NotImplementedError(message)
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def exportPEMFile(self, body: ModelKeyPairExportSettings, id: str):
        """ Download the key pair in PEM format.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/keyPairs/signing/{id}/pem"),
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
                self.logger.info("Key Pair downloaded.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return Modelstr.from_dict(response_dict)
                else:
                    return str(response)
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 403:
                message = "(403) The operation is not permitted, based on the current configuration of the server."
                self.logger.info(message)
                raise NotImplementedError(message)
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def exportCertificateFile(self, id: str):
        """ Download the certificate from a given key pair.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/keyPairs/signing/{id}/certificate"),
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
                    return Modelstr.from_dict(response_dict)
                else:
                    return str(response)
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
