class NotificationPublishersSettings():
    """General notification publisher settings.

    Attributes
    ----------
    defaultNotificationPublisherRef : str
        Reference to the default notification publisher, if one is defined.
    """

    __slots__ = ["defaultNotificationPublisherRef"]

    def __init__(self, defaultNotificationPublisherRef=None):
        self.defaultNotificationPublisherRef = defaultNotificationPublisherRef

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, NotificationPublishersSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.defaultNotificationPublisherRef))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["defaultNotificationPublisherRef"]}

        return cls(**valid_data)
