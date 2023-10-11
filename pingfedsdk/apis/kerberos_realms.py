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
from pingfedsdk.models.kerberos_realm import KerberosRealm as ModelKerberosRealm
from pingfedsdk.models.kerberos_realms import KerberosRealms as ModelKerberosRealms
from pingfedsdk.models.kerberos_realms_settings import KerberosRealmsSettings as ModelKerberosRealmsSettings


class KerberosRealms:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.KerberosRealms")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getKerberosRealms(self):
        """ Gets the Kerberos Realms.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/kerberos/realms"),
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
                    return ModelKerberosRealms.from_dict(response_dict)
                else:
                    return ModelKerberosRealms.from_dict(response.json())

    def createKerberosRealm(self, body: ModelKerberosRealm, XBypassExternalValidation: bool = None):
        """ Create a new Kerberos Realm.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/kerberos/realms"),
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
                self.logger.info("Kerberos realm created.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelKerberosRealm.from_dict(response_dict)
                else:
                    return ModelKerberosRealm.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getKerberosRealm(self, id: str):
        """ Find a Kerberos Realm by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/kerberos/realms/{id}"),
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
                    return ModelKerberosRealm.from_dict(response_dict)
                else:
                    return ModelKerberosRealm.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateKerberosRealm(self, body: ModelKerberosRealm, id: str, XBypassExternalValidation: bool = None):
        """ Update a Kerberos Realm by ID.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/kerberos/realms/{id}"),
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
                self.logger.info("Kerberos realm updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelKerberosRealm.from_dict(response_dict)
                else:
                    return ModelKerberosRealm.from_dict(response.json())
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

    def deleteKerberosRealm(self, id: str):
        """ Delete a Kerberos Realm.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/kerberos/realms/{id}"),
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
                self.logger.info("Kerberos realm deleted.")
                return ModelApiResult(message="Kerberos realm deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getKerberosRealmSettings(self):
        """ Gets the Kerberos Realms Settings.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/kerberos/realms/settings"),
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
                    return ModelKerberosRealmsSettings.from_dict(response_dict)
                else:
                    return ModelKerberosRealmsSettings.from_dict(response.json())

    def updateSettings(self, body: ModelKerberosRealmsSettings):
        """ Set/Update the Kerberos Realms Settings.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/kerberos/realms/settings"),
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
                    return ModelKerberosRealmsSettings.from_dict(response_dict)
                else:
                    return ModelKerberosRealmsSettings.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())
