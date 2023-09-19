from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.captcha_settings import CaptchaSettings
from pingfedsdk.models.contact_info import ContactInfo
from pingfedsdk.models.email_server_settings import EmailServerSettings
from pingfedsdk.models.federation_info import FederationInfo
from pingfedsdk.models.notification_settings import NotificationSettings
from pingfedsdk.models.roles_and_protocols import RolesAndProtocols


class ServerSettings(Model):
    """Server configuration settings.

    Attributes
    ----------
    contactInfo: ContactInfo
        Information that identifies the server.

    notifications: NotificationSettings
        Notification settings for license and certificate expiration events.

    rolesAndProtocols: RolesAndProtocols
        Configure roles and protocols.

    federationInfo: FederationInfo
        Federation Info.

    emailServer: EmailServerSettings
        Email Server Settings.

    captchaSettings: CaptchaSettings
        Captcha Settings.

    """
    def __init__(self, contactInfo: ContactInfo = None, notifications: NotificationSettings = None, rolesAndProtocols: RolesAndProtocols = None, federationInfo: FederationInfo = None, emailServer: EmailServerSettings = None, captchaSettings: CaptchaSettings = None) -> None:
        self.contactInfo = contactInfo
        self.notifications = notifications
        self.rolesAndProtocols = rolesAndProtocols
        self.federationInfo = federationInfo
        self.emailServer = emailServer
        self.captchaSettings = captchaSettings

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ServerSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.contactInfo, self.notifications, self.rolesAndProtocols, self.federationInfo, self.emailServer, self.captchaSettings]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["contactInfo", "notifications", "rolesAndProtocols", "federationInfo", "emailServer", "captchaSettings"] and v is not None:
                if k == "contactInfo":
                    valid_data[k] = ContactInfo.from_dict(v)
                if k == "notifications":
                    valid_data[k] = NotificationSettings.from_dict(v)
                if k == "rolesAndProtocols":
                    valid_data[k] = RolesAndProtocols.from_dict(v)
                if k == "federationInfo":
                    valid_data[k] = FederationInfo.from_dict(v)
                if k == "emailServer":
                    valid_data[k] = EmailServerSettings.from_dict(v)
                if k == "captchaSettings":
                    valid_data[k] = CaptchaSettings.from_dict(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["contactInfo", "notifications", "rolesAndProtocols", "federationInfo", "emailServer", "captchaSettings"]:
                if isinstance(v, Model):
                    body[k] = v.to_dict(remove_nonetypes)
                elif isinstance(v, list):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, dict):
                    vals = {}
                    for x, y in v.items():
                        if isinstance(y, Model):
                            vals[x] = y.to_dict(remove_nonetypes)
                        elif not remove_nonetypes or (remove_nonetypes and y is not None):
                            vals[x] = y
                    body[k] = vals
                elif isinstance(v, set):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, Enum):
                    body[k] = str(v).split('.')[-1]
                elif not remove_nonetypes or (remove_nonetypes and v is not None):
                    body[k] = v
        return body
