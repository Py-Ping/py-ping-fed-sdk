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
from pingfedsdk.models.identity_store_provisioner import IdentityStoreProvisioner as ModelIdentityStoreProvisioner
from pingfedsdk.models.identity_store_provisioner_descriptor import IdentityStoreProvisionerDescriptor as ModelIdentityStoreProvisionerDescriptor
from pingfedsdk.models.identity_store_provisioner_descriptors import IdentityStoreProvisionerDescriptors as ModelIdentityStoreProvisionerDescriptors
from pingfedsdk.models.identity_store_provisioners import IdentityStoreProvisioners as ModelIdentityStoreProvisioners


class IdentityStoreProvisioners:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.IdentityStoreProvisioners")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getIdentityStoreProvisioner(self, id: str):
        """ Get an identity store provisioner by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/identityStoreProvisioners/{id}"),
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
                    return ModelIdentityStoreProvisioner.from_dict(response_dict)
                else:
                    return ModelIdentityStoreProvisioner.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateIdentityStoreProvisioner(self, body: ModelIdentityStoreProvisioner, id: str):
        """ Update an identity store provisioner instance
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/identityStoreProvisioners/{id}"),
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
                self.logger.info("Identity store provisioner updated")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelIdentityStoreProvisioner.from_dict(response_dict)
                else:
                    return ModelIdentityStoreProvisioner.from_dict(response.json())
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

    def deleteIdentityStoreProvisioner(self, id: str):
        """ Delete an identity store provisioner instance
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/identityStoreProvisioners/{id}"),
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
                self.logger.info("Identity store provisioner deleted")
                return ModelApiResult(message="Identity store provisioner deleted", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getIdentityStoreProvisioners(self):
        """ Get the list of configured identity store provisioner instances.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/identityStoreProvisioners"),
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
                    return ModelIdentityStoreProvisioners.from_dict(response_dict)
                else:
                    return ModelIdentityStoreProvisioners.from_dict(response.json())

    def createIdentityStoreProvisioner(self, body: ModelIdentityStoreProvisioner):
        """ Create a new identity store provisioner instance.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/identityStoreProvisioners"),
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
                    return ModelIdentityStoreProvisioner.from_dict(response_dict)
                else:
                    return ModelIdentityStoreProvisioner.from_dict(response.json())
            if response.status_code == 201:
                self.logger.info("Identity store provisioner created.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelIdentityStoreProvisioner.from_dict(response_dict)
                else:
                    return ModelIdentityStoreProvisioner.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getIdentityStoreProvisionerDescriptors(self):
        """ Get the list of available identity store provisioner descriptors.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/identityStoreProvisioners/descriptors"),
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
                    return ModelIdentityStoreProvisionerDescriptors.from_dict(response_dict)
                else:
                    return ModelIdentityStoreProvisionerDescriptors.from_dict(response.json())

    def getIdentityStoreProvisionerDescriptorById(self, id: str):
        """ Get the descriptor of an identity store provisioner by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/identityStoreProvisioners/descriptors/{id}"),
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
                    return ModelIdentityStoreProvisionerDescriptor.from_dict(response_dict)
                else:
                    return ModelIdentityStoreProvisionerDescriptor.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
