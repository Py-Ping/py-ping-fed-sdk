from json import dumps
import logging
import os
import traceback

from requests import Session
from requests.exceptions import HTTPError

from pingfedsdk.exceptions import NotFound
from pingfedsdk.exceptions import ObjectDeleted
from pingfedsdk.exceptions import ValidationError
from pingfedsdk.models.administrative_account import AdministrativeAccount as ModelAdministrativeAccount
from pingfedsdk.models.administrative_accounts import AdministrativeAccounts as ModelAdministrativeAccounts
from pingfedsdk.models.api_result import ApiResult as ModelApiResult
from pingfedsdk.models.user_credentials import UserCredentials as ModelUserCredentials


class AdministrativeAccounts:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.AdministrativeAccounts")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def changePassword(self, body: ModelUserCredentials):
        """ Change the Password of current PingFederate native Account.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/administrativeAccounts/changePassword"),
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
                self.logger.info("Administrator password changed.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelUserCredentials.from_dict(response_dict)
                else:
                    return ModelUserCredentials.from_dict(response.json())
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getAccounts(self):
        """ Get all the PingFederate native Administrative Accounts.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/administrativeAccounts"),
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
                    return ModelAdministrativeAccounts.from_dict(response_dict)
                else:
                    return ModelAdministrativeAccounts.from_dict(response.json())
            if response.status_code == 422:
                raise ValidationError(response.json())

    def addAccount(self, body: ModelAdministrativeAccount):
        """ Add a new PingFederate native Administrative Account.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/administrativeAccounts"),
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
                self.logger.info("New Administrative Account created.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelAdministrativeAccount.from_dict(response_dict)
                else:
                    return ModelAdministrativeAccount.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getAccount(self, username: str):
        """ Get a PingFederate native Administrative Account.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/administrativeAccounts/{username}"),
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
                    return ModelAdministrativeAccount.from_dict(response_dict)
                else:
                    return ModelAdministrativeAccount.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateAccount(self, body: ModelAdministrativeAccount, username: str):
        """ Update the information for a native Administrative Account.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/administrativeAccounts/{username}"),
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
                self.logger.info("Administrator Account updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelAdministrativeAccount.from_dict(response_dict)
                else:
                    return ModelAdministrativeAccount.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def deleteAccount(self, username: str):
        """ Delete a PingFederate native Administrative Account information.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/administrativeAccounts/{username}"),
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
                self.logger.info("Administrator Account Deleted.")
                return ModelApiResult(message="Administrator Account Deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def resetPassword(self, body: ModelUserCredentials, username: str):
        """ Reset the Password of an existing PingFederate native Administrative Account.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/administrativeAccounts/{username}/resetPassword"),
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
                self.logger.info("Administrator password reset.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelUserCredentials.from_dict(response_dict)
                else:
                    return ModelUserCredentials.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())
