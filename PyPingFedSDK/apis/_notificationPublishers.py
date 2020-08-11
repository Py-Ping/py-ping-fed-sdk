import os
import logging
from requests import Session
from requests.exceptions import HTTPError


class _notificationPublishers():
    def __init__(self, endpoint:str, session:Session) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._notificationPublishers')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
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
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
        finally:
            return response

    def updateSettings(self, body):
        """ Update general notification publisher settings.
        """

        payload = {
            "body": body

        }

        try:
            response = self.session.put(
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
                self.logger.info('Notification publisher settings updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getNotificationPublisherPluginDescriptors(self):
        """ Get the list of available Notification Publisher Plugin descriptors.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/notificationPublishers/descriptors"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
        finally:
            return response

    def getNotificationPublisherPluginDescriptor(self, var_id):
        """ Get the description of a notification publisher plugin descriptor.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/notificationPublishers/descriptors/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def getNotificationPublishers(self):
        """ Get a list of notification publisher plugin instances.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/notificationPublishers"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
        finally:
            return response

    def createNotificationPublisher(self, body):
        """ Create a notification publisher plugin instance.
        """

        payload = {
            "body": body

        }

        try:
            response = self.session.post(
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
                self.logger.info('Notification Publisher plugin created.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getNotificationPublisher(self, var_id):
        """ Get a specific notification publisher plugin instance.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/notificationPublishers/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def updateNotificationPublisher(self, var_id, body):
        """ Update a notification publisher plugin instance.
        """

        payload = {
            "var_id": var_id,
            "body": body

        }

        try:
            response = self.session.put(
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
                self.logger.info('Notification Publisher plugin updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def deleteNotificationPublisher(self, var_id):
        """ Delete a notification publisher plugin instance.
        """

        try:
            response = self.session.delete(

                url=self._build_uri("/notificationPublishers/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info('Notification Publisher plugin deleted.')
            if response.status_code == 403:
                self.logger.info('The operation is not permitted, based on the current configuration of the server.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def getActions(self, var_id):
        """ List the actions for a notification publisher plugin instance.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/notificationPublishers/{id}/actions"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def getAction(self, var_id, actionId):
        """ Find an notification publisher plugin instance's action by ID.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/notificationPublishers/{id}/actions/{actionId}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def invokeAction(self, var_id, actionId):
        """ Invokes an action for notification publisher plugin instance.
        """

        payload = {
            "var_id": var_id,
            "actionId": actionId

        }

        try:
            response = self.session.post(
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
                self.logger.info('Notification Publisher plugin action invoked.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

