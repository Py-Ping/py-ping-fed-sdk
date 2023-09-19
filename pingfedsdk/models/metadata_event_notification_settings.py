from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.resource_link import ResourceLink


class MetadataEventNotificationSettings(Model):
    """Notification settings for metadata update events.

    Attributes
    ----------
    emailAddress: str
        The email address where metadata update notifications are sent.

    notificationPublisherRef: ResourceLink
        Reference to the associated notification publisher.

    """
    def __init__(self, emailAddress: str, notificationPublisherRef: ResourceLink = None) -> None:
        self.emailAddress = emailAddress
        self.notificationPublisherRef = notificationPublisherRef

    def _validate(self) -> bool:
        return any(x for x in ["emailAddress"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, MetadataEventNotificationSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.emailAddress, self.notificationPublisherRef]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["emailAddress", "notificationPublisherRef"] and v is not None:
                if k == "emailAddress":
                    valid_data[k] = str(v)
                if k == "notificationPublisherRef":
                    valid_data[k] = ResourceLink.from_dict(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["emailAddress", "notificationPublisherRef"]:
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
