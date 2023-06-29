from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.license_event_notification_settings import LicenseEventNotificationSettings
from pingfedsdk.models.metadata_event_notification_settings import MetadataEventNotificationSettings
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.models.certificate_expiration_notification_settings import CertificateExpirationNotificationSettings


class NotificationSettings(Model):
    """Settings for notifications relating to licensing and certificate expiration.

    Attributes
    ----------
    licenseEvents: LicenseEventNotificationSettings
        Settings for license event notifications.

    certificateExpirations: CertificateExpirationNotificationSettings
        Settings for certificate expiration notifications.

    notifyAdminUserPasswordChanges: bool
        Determines whether admin users are notified through email when their account is changed.

    accountChangesNotificationPublisherRef: ResourceLink
        Reference to the associated notification publisher for admin user account changes.

    metadataNotificationSettings: MetadataEventNotificationSettings
        Settings for metadata update event notifications.

    """

    def __init__(self, licenseEvents: LicenseEventNotificationSettings = None, certificateExpirations: CertificateExpirationNotificationSettings = None, notifyAdminUserPasswordChanges: bool = None, accountChangesNotificationPublisherRef: ResourceLink = None, metadataNotificationSettings: MetadataEventNotificationSettings = None) -> None:
        self.licenseEvents = licenseEvents
        self.certificateExpirations = certificateExpirations
        self.notifyAdminUserPasswordChanges = notifyAdminUserPasswordChanges
        self.accountChangesNotificationPublisherRef = accountChangesNotificationPublisherRef
        self.metadataNotificationSettings = metadataNotificationSettings

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, NotificationSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.licenseEvents, self.certificateExpirations, self.notifyAdminUserPasswordChanges, self.accountChangesNotificationPublisherRef, self.metadataNotificationSettings]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["licenseEvents", "certificateExpirations", "notifyAdminUserPasswordChanges", "accountChangesNotificationPublisherRef", "metadataNotificationSettings"] and v is not None:
                if k == "licenseEvents":
                    valid_data[k] = LicenseEventNotificationSettings(**v)
                if k == "certificateExpirations":
                    valid_data[k] = CertificateExpirationNotificationSettings(**v)
                if k == "notifyAdminUserPasswordChanges":
                    valid_data[k] = bool(v)
                if k == "accountChangesNotificationPublisherRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "metadataNotificationSettings":
                    valid_data[k] = MetadataEventNotificationSettings(**v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["licenseEvents", "certificateExpirations", "notifyAdminUserPasswordChanges", "accountChangesNotificationPublisherRef", "metadataNotificationSettings"]:
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
