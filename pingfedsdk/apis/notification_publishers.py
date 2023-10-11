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
from pingfedsdk.models.action import Action as ModelAction
from pingfedsdk.models.action_options import ActionOptions as ModelActionOptions
from pingfedsdk.models.action_result import ActionResult as ModelActionResult
from pingfedsdk.models.actions import Actions as ModelActions
from pingfedsdk.models.api_result import ApiResult as ModelApiResult
from pingfedsdk.models.notification_publisher import NotificationPublisher as ModelNotificationPublisher
from pingfedsdk.models.notification_publisher_descriptor import NotificationPublisherDescriptor as ModelNotificationPublisherDescriptor
from pingfedsdk.models.notification_publisher_descriptors import NotificationPublisherDescriptors as ModelNotificationPublisherDescriptors
from pingfedsdk.models.notification_publishers import NotificationPublishers as ModelNotificationPublishers
from pingfedsdk.models.notification_publishers_settings import NotificationPublishersSettings as ModelNotificationPublishersSettings


class NotificationPublishers:
    def __init__(self, endpoint: str, session: Session) -> None:
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingSDK.NotificationPublishers")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getSettings(self):
        """ Get general notification publisher settings.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/notificationPublishers/settings"),
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
                    return ModelNotificationPublishersSettings.from_dict(response_dict)
                else:
                    return ModelNotificationPublishersSettings.from_dict(response.json())

    def updateSettings(self, body: ModelNotificationPublishersSettings):
        """ Update general notification publisher settings.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/notificationPublishers/settings"),
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
                self.logger.info("Notification publisher settings updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelNotificationPublishersSettings.from_dict(response_dict)
                else:
                    return ModelNotificationPublishersSettings.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getAction(self, actionId: str, id: str):
        """ Find an notification publisher plugin instance's action by ID.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/notificationPublishers/{id}/actions/{actionId}"),
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
                    return ModelAction.from_dict(response_dict)
                else:
                    return ModelAction.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getNotificationPublisherPluginDescriptors(self):
        """ Get the list of available Notification Publisher Plugin descriptors.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/notificationPublishers/descriptors"),
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
                    return ModelNotificationPublisherDescriptors.from_dict(response_dict)
                else:
                    return ModelNotificationPublisherDescriptors.from_dict(response.json())

    def getNotificationPublisherPluginDescriptor(self, id: str):
        """ Get the description of a notification publisher plugin descriptor.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/notificationPublishers/descriptors/{id}"),
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
                    return ModelNotificationPublisherDescriptor.from_dict(response_dict)
                else:
                    return ModelNotificationPublisherDescriptor.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getNotificationPublishers(self):
        """ Get a list of notification publisher plugin instances.
        """

        try:
            response = self.session.get(
                url=self._build_uri("/notificationPublishers"),
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
                    return ModelNotificationPublishers.from_dict(response_dict)
                else:
                    return ModelNotificationPublishers.from_dict(response.json())

    def createNotificationPublisher(self, body: ModelNotificationPublisher):
        """ Create a notification publisher plugin instance.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri("/notificationPublishers"),
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
                self.logger.info("Notification Publisher plugin created.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelNotificationPublisher.from_dict(response_dict)
                else:
                    return ModelNotificationPublisher.from_dict(response.json())
            if response.status_code == 400:
                message = "(400) The request was improperly formatted or contained invalid fields."
                self.logger.info(message)
                raise BadRequest(message)
            if response.status_code == 422:
                raise ValidationError(response.json())

    def getNotificationPublisher(self, id: str):
        """ Get a specific notification publisher plugin instance.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/notificationPublishers/{id}"),
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
                    return ModelNotificationPublisher.from_dict(response_dict)
                else:
                    return ModelNotificationPublisher.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def updateNotificationPublisher(self, body: ModelNotificationPublisher, id: str):
        """ Update a notification publisher plugin instance.
        """

        try:
            response = self.session.put(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/notificationPublishers/{id}"),
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
                self.logger.info("Notification Publisher plugin updated.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelNotificationPublisher.from_dict(response_dict)
                else:
                    return ModelNotificationPublisher.from_dict(response.json())
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

    def deleteNotificationPublisher(self, id: str):
        """ Delete a notification publisher plugin instance.
        """

        try:
            response = self.session.delete(
                url=self._build_uri(f"/notificationPublishers/{id}"),
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
                self.logger.info("Notification Publisher plugin deleted.")
                return ModelApiResult(message="Notification Publisher plugin deleted.", validationErrors=[])
            if response.status_code == 403:
                message = "(403) The operation is not permitted, based on the current configuration of the server."
                self.logger.info(message)
                raise NotImplementedError(message)
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def invokeActionWithOptions(self, actionId: str, id: str, body: ModelActionOptions = None):
        """ Invokes an action for notification publisher plugin instance.
        """

        try:
            response = self.session.post(
                data=dumps({x: y for x, y in body.to_dict().items() if y is not None}),
                url=self._build_uri(f"/notificationPublishers/{id}/actions/{actionId}/invokeAction"),
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
                self.logger.info("Notification Publisher plugin action invoked.")
                if isinstance(response.json(), list):
                    response_dict = {'items': response.json()}
                    return ModelActionResult.from_dict(response_dict)
                else:
                    return ModelActionResult.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)

    def getActions(self, id: str):
        """ List the actions for a notification publisher plugin instance.
        """

        try:
            response = self.session.get(
                url=self._build_uri(f"/notificationPublishers/{id}/actions"),
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
                    return ModelActions.from_dict(response_dict)
                else:
                    return ModelActions.from_dict(response.json())
            if response.status_code == 404:
                message = "(404) Resource not found."
                self.logger.info(message)
                raise NotFound(message)
