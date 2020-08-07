class NotificationPublishersSettings():
    """General notification publisher settings.

    Attributes
    ----------
    defaultNotificationPublisherRef : str
 Reference to the default notification publisher, if one is defined.

    """

    def __init__(self, defaultNotificationPublisherRef=None) -> None:
        self.defaultNotificationPublisherRef = defaultNotificationPublisherRef

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, NotificationPublishersSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.defaultNotificationPublisherRef))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["defaultNotificationPublisherRef"]}

        return cls(**valid_data)