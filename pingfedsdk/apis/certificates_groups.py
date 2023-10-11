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
from pingfedsdk.models.cert_view import CertView as ModelCertView
from pingfedsdk.models.cert_views import CertViews as ModelCertViews
from pingfedsdk.models.x_5_0_9_file import X509File as ModelX509File


class CertificatesGroups:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.CertificatesGroups")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getCertificatesForGroup(self, groupName: str):
        """ Get list of all certificates for a group.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/certificates/groups/{groupName}"),
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
                    return ModelCertViews.from_dict(response_dict)
                else:
                    return ModelCertViews.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getCertificateFromGroup(self, groupName: str, id: str):
        """ Retrieve details of a certificate.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/certificates/groups/{groupName}/{id}"),
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
                    return ModelCertView.from_dict(response_dict)
                else:
                    return ModelCertView.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def deleteCertificateFromGroup(self, groupName: str, id: str):
        """ Delete a certificate from a group.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/certificates/groups/{groupName}/{id}"),
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
                self.logger.info("Group certificate deleted.")
                return ModelApiResult(message="Group certificate deleted.", validationErrors=[])
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def importFeatureCert(self, body: ModelX509File, groupName: str):
        """ Import a new certificate to a group.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/certificates/groups/{groupName}/import"),
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
                self.logger.info("Group certificate imported.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelCertView.from_dict(response_dict)
                else:
                    return ModelCertView.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())
