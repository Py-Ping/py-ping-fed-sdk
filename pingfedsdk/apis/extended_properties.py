from json import dumps
import logging
import os
import traceback

from requests import Session
from requests.exceptions import HTTPError

from pingfedsdk.exceptions import ValidationError
from pingfedsdk.models.api_result import ApiResult as ModelApiResult
from pingfedsdk.models.extended_properties import ExtendedProperties as ModelExtendedProperties


class ExtendedProperties:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.ExtendedProperties")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getExtendedProperties(self):
        """ Get the defined Extended Properties.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/extendedProperties"),
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
                    return ModelExtendedProperties.from_dict(response_dict)
                else:
                    return ModelExtendedProperties.from_dict(response.json())

    def updateExtendedProperties(self, body: ModelExtendedProperties):
        """ Update the Extended Properties.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/extendedProperties"),
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
                self.logger.info("Extended properties updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelExtendedProperties.from_dict(response_dict)
                else:
                    return ModelExtendedProperties.from_dict(response.json())
            if response.status_code == 422:
                raise ValidationError(response.json())