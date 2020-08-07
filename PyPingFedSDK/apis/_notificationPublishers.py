import logging
import requests
import os
from requests.exceptions import HTTPError


class _notificationPublishers():
    def __init__(self, endpoint):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._notificationPublishers')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint

    def _build_uri(self, path):
        return f"{self.endpoint}{path}"

    def getSettings(self):
        """ Get general notification publisher settings.
        """

        try:
            response = requests.get(

                url=self._build_uri("/notificationPublishers/settings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
        finally:
            return response.json()

    def updateSettings(self, body):
        """ Update general notification publisher settings.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/notificationPublishers/settings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Notification publisher settings updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getNotificationPublisherPluginDescriptors(self):
        """ Get the list of available Notification Publisher Plugin descriptors.
        """

        try:
            response = requests.get(

                url=self._build_uri("/notificationPublishers/descriptors"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
        finally:
            return response.json()

    def getNotificationPublisherPluginDescriptor(self, id):
        """ Get the description of a notification publisher plugin descriptor.
        """

        try:
            response = requests.get(

                url=self._build_uri("/notificationPublishers/descriptors/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def getNotificationPublishers(self):
        """ Get a list of notification publisher plugin instances.
        """

        try:
            response = requests.get(

                url=self._build_uri("/notificationPublishers"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
        finally:
            return response.json()

    def createNotificationPublisher(self, body):
        """ Create a notification publisher plugin instance.
        """

        payload = {
            "body": body

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/notificationPublishers"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info("Notification Publisher plugin created.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def getNotificationPublisher(self, id):
        """ Get a specific notification publisher plugin instance.
        """

        try:
            response = requests.get(

                url=self._build_uri("/notificationPublishers/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def updateNotificationPublisher(self, id, body):
        """ Update a notification publisher plugin instance.
        """

        payload = {
            "id": id,
            "body": body

        }

        try:
            response = requests.put(
                data=payload,
                url=self._build_uri("/notificationPublishers/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Notification Publisher plugin updated.")
            if response.status_code == 400:
                self.logger.info("The request was improperly formatted or contained invalid fields.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
            if response.status_code == 422:
                self.logger.info("Validation error(s) occurred.")
        finally:
            return response.json()

    def deleteNotificationPublisher(self, id):
        """ Delete a notification publisher plugin instance.
        """

        try:
            response = requests.delete(

                url=self._build_uri("/notificationPublishers/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info("Notification Publisher plugin deleted.")
            if response.status_code == 403:
                self.logger.info("The operation is not permitted, based on the current configuration of the server.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def getActions(self, id):
        """ List the actions for a notification publisher plugin instance.
        """

        try:
            response = requests.get(

                url=self._build_uri("/notificationPublishers/{id}/actions"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def getAction(self, id, actionId):
        """ Find an notification publisher plugin instance's action by ID.
        """

        try:
            response = requests.get(

                url=self._build_uri("/notificationPublishers/{id}/actions/{actionId}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Success.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

    def invokeAction(self, id, actionId):
        """ Invokes an action for notification publisher plugin instance.
        """

        payload = {
            "id": id,
            "actionId": actionId

        }

        try:
            response = requests.post(
                data=payload,
                url=self._build_uri("/notificationPublishers/{id}/actions/{actionId}/invokeAction"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info("Notification Publisher plugin action invoked.")
            if response.status_code == 404:
                self.logger.info("Resource not found.")
        finally:
            return response.json()

