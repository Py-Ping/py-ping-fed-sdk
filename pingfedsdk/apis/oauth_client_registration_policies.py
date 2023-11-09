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
from pingfedsdk.models.client_registration_policies import ClientRegistrationPolicies as ModelClientRegistrationPolicies
from pingfedsdk.models.client_registration_policy import ClientRegistrationPolicy as ModelClientRegistrationPolicy
from pingfedsdk.models.client_registration_policy_descriptor import ClientRegistrationPolicyDescriptor as ModelClientRegistrationPolicyDescriptor
from pingfedsdk.models.client_registration_policy_descriptors import ClientRegistrationPolicyDescriptors as ModelClientRegistrationPolicyDescriptors


class OauthClientRegistrationPolicies:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.OauthClientRegistrationPolicies")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getDynamicClientRegistrationDescriptor(self, id: str):
        """ Get the description of a client registration policy plugin descriptor.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/oauth/clientRegistrationPolicies/descriptors/{id}"),
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
                    return ModelClientRegistrationPolicyDescriptor.from_dict(response_dict)
                else:
                    return ModelClientRegistrationPolicyDescriptor.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getDynamicClientRegistrationPolicies(self):
        """ Get a list of client registration policy plugin instances.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/oauth/clientRegistrationPolicies"),
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
                    return ModelClientRegistrationPolicies.from_dict(response_dict)
                else:
                    return ModelClientRegistrationPolicies.from_dict(response.json())

    def createDynamicClientRegistrationPolicy(self, body: ModelClientRegistrationPolicy):
        """ Create a client registration policy plugin instance.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/oauth/clientRegistrationPolicies"),
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
                self.logger.info("Client Registration Policy plugin created.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelClientRegistrationPolicy.from_dict(response_dict)
                else:
                    return ModelClientRegistrationPolicy.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getDynamicClientRegistrationPolicy(self, id: str):
        """ Get a specific client registration policy plugin instance.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/oauth/clientRegistrationPolicies/{id}"),
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
                    return ModelClientRegistrationPolicy.from_dict(response_dict)
                else:
                    return ModelClientRegistrationPolicy.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateDynamicClientRegistrationPolicy(self, body: ModelClientRegistrationPolicy, id: str):
        """ Update a client registration policy plugin instance.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/oauth/clientRegistrationPolicies/{id}"),
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
                self.logger.info("Client Registration Policy plugin updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelClientRegistrationPolicy.from_dict(response_dict)
                else:
                    return ModelClientRegistrationPolicy.from_dict(response.json())
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

    def deleteDynamicClientRegistrationPolicy(self, id: str):
        """ Delete a client registration policy plugin instance.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/oauth/clientRegistrationPolicies/{id}"),
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
                self.logger.info("Client Registration Policy plugin deleted.")
                return ModelApiResult(message="Client Registration Policy plugin deleted.", validationErrors=[])
            if response.status_code == 403:
                message = "(403) The operation is not permitted, based on the current configuration of the server."
                self.logger.info(message)
                raise NotImplementedError(message)
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getDynamicClientRegistrationDescriptors(self):
        """ Get the list of available client registration policy plugin descriptors.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/oauth/clientRegistrationPolicies/descriptors"),
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
                    return ModelClientRegistrationPolicyDescriptors.from_dict(response_dict)
                else:
                    return ModelClientRegistrationPolicyDescriptors.from_dict(response.json())
