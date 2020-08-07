class MetadataEventNotificationSettings():
    """Notification settings for metadata update events.

    Attributes
    ----------
    emailAddress : string
 The email address where metadata update notifications are sent.
    notificationPublisherRef : str
 Reference to the associated notification publisher.

    """

<<<<<<< HEAD
    def __init__(self, emailAddress, notificationPublisherRef=None) -> None:
        self.emailAddress = emailAddress
        self.notificationPublisherRef = notificationPublisherRef
=======
    def __init__(self, emailAddress, notificationPublisherRef=None):
        self.emailAddress: str = emailAddress
        self.notificationPublisherRef: str = notificationPublisherRef
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["emailAddress"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, MetadataEventNotificationSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.emailAddress, self.notificationPublisherRef))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["emailAddress", "notificationPublisherRef"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
