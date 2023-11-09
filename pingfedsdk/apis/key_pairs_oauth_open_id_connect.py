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
from pingfedsdk.models.additional_key_set import AdditionalKeySet as ModelAdditionalKeySet
from pingfedsdk.models.additional_key_sets import AdditionalKeySets as ModelAdditionalKeySets
from pingfedsdk.models.api_result import ApiResult as ModelApiResult
from pingfedsdk.models.o_auth_oidc_keys_settings import OAuthOidcKeysSettings as ModelOAuthOidcKeysSettings


class KeyPairsOauthOpenIdConnect:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.KeyPairsOauthOpenIdConnect")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getKeySets(self):
        """ Retrieve OAuth/OpenID Connect additional signing key sets.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/keyPairs/oauthOpenIdConnect/additionalKeySets"),
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
                    return ModelAdditionalKeySets.from_dict(response_dict)
                else:
                    return ModelAdditionalKeySets.from_dict(response.json())

    def createKeySet(self, body: ModelAdditionalKeySet):
        """ Create a new OAuth/OpenID Connect additional signing key set.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/keyPairs/oauthOpenIdConnect/additionalKeySets"),
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
                self.logger.info("OAuth/OpenID Connect key set created.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelAdditionalKeySet.from_dict(response_dict)
                else:
                    return ModelAdditionalKeySet.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getOauthOidcKeysSettings(self):
        """ Retrieve OAuth/OpenID Connect key settings.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/keyPairs/oauthOpenIdConnect"),
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
                    return ModelOAuthOidcKeysSettings.from_dict(response_dict)
                else:
                    return ModelOAuthOidcKeysSettings.from_dict(response.json())

    def updateOAuthOidcKeysSettings(self, body: ModelOAuthOidcKeysSettings):
        """ Update OAuth/OpenID Connect key settings.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/keyPairs/oauthOpenIdConnect"),
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
                self.logger.info("OAuth/Open ID Connect key settings updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelOAuthOidcKeysSettings.from_dict(response_dict)
                else:
                    return ModelOAuthOidcKeysSettings.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getKeySet(self, id: str):
        """ Retrieve an OAuth/OpenID Connect additional signing key set.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/keyPairs/oauthOpenIdConnect/additionalKeySets/{id}"),
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
                    return ModelAdditionalKeySet.from_dict(response_dict)
                else:
                    return ModelAdditionalKeySet.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateKeySet(self, body: ModelAdditionalKeySet, id: str):
        """ Update an existing OAuth/OpenID Connect additional signing key set.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/keyPairs/oauthOpenIdConnect/additionalKeySets/{id}"),
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
                self.logger.info("OAuth/OpenID Connect key set updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelAdditionalKeySet.from_dict(response_dict)
                else:
                    return ModelAdditionalKeySet.from_dict(response.json())
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

    def deleteKeySet(self, id: str):
        """ Delete an existing OAuth/OpenID Connect additional signing key set.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/keyPairs/oauthOpenIdConnect/additionalKeySets/{id}"),
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
                self.logger.info("OAuth/OpenID Connect key set deleted.")
                return ModelApiResult(message="OAuth/OpenID Connect key set deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
