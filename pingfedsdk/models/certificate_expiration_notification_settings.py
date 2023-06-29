from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink


class CertificateExpirationNotificationSettings(Model):
    """Notification settings for certificate expiration events.

    Attributes
    ----------
    emailAddress: str
        Email address where notifications are sent.

    initialWarningPeriod: int
        Time before certificate expiration when initial warning is sent (in days).

    finalWarningPeriod: int
        Time before certificate expiration when final warning is sent (in days).

    notificationPublisherRef: ResourceLink
        Reference to the associated notification publisher.

    """

    def __init__(self, emailAddress: str, finalWarningPeriod: int, initialWarningPeriod: int = None, notificationPublisherRef: ResourceLink = None) -> None:
        self.emailAddress = emailAddress
        self.initialWarningPeriod = initialWarningPeriod
        self.finalWarningPeriod = finalWarningPeriod
        self.notificationPublisherRef = notificationPublisherRef

    def _validate(self) -> bool:
        return any(x for x in ["emailAddress", "finalWarningPeriod"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, CertificateExpirationNotificationSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.emailAddress, self.initialWarningPeriod, self.finalWarningPeriod, self.notificationPublisherRef]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["emailAddress", "initialWarningPeriod", "finalWarningPeriod", "notificationPublisherRef"] and v is not None:
                if k == "emailAddress":
                    valid_data[k] = str(v)
                if k == "initialWarningPeriod":
                    valid_data[k] = int(v)
                if k == "finalWarningPeriod":
                    valid_data[k] = int(v)
                if k == "notificationPublisherRef":
                    valid_data[k] = ResourceLink(**v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["emailAddress", "initialWarningPeriod", "finalWarningPeriod", "notificationPublisherRef"]:
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
