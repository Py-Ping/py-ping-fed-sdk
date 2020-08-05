class MetadataEventNotificationSettings():
    """Notification settings for metadata update events.

    Attributes
    ----------
    emailAddress : string
        The email address where metadata update notifications are sent.    notificationPublisherRef : str
        Reference to the associated notification publisher.
    """

    __slots__ = ["emailAddress", "notificationPublisherRef"]

    def __init__(self, emailAddress, notificationPublisherRef=None):
        self.emailAddress = emailAddress
        self.notificationPublisherRef = notificationPublisherRef

    def _validate(self):
        return any(x for x in ['emailAddress'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, MetadataEventNotificationSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.emailAddress, self.notificationPublisherRef))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["emailAddress", "notificationPublisherRef"]}

        return cls(**valid_data)
