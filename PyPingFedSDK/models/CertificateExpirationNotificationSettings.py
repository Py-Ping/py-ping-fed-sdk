class CertificateExpirationNotificationSettings():
    """Notification settings for certificate expiration events.

    Attributes
    ----------
    emailAddress : string
        Email address where notifications are sent.    finalWarningPeriod : integer
        Time before certificate expiration when final warning is sent (in days).    initialWarningPeriod : integer
        Time before certificate expiration when initial warning is sent (in days).    notificationPublisherRef : str
        Reference to the associated notification publisher.
    """

    __slots__ = ["emailAddress", "finalWarningPeriod", "initialWarningPeriod", "notificationPublisherRef"]

    def __init__(self, emailAddress, finalWarningPeriod, initialWarningPeriod=None, notificationPublisherRef=None):
        self.emailAddress = emailAddress
        self.finalWarningPeriod = finalWarningPeriod
        self.initialWarningPeriod = initialWarningPeriod
        self.notificationPublisherRef = notificationPublisherRef

    def _validate(self):
        return any(x for x in ['emailAddress', 'finalWarningPeriod'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, CertificateExpirationNotificationSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.emailAddress, self.finalWarningPeriod, self.initialWarningPeriod, self.notificationPublisherRef))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["emailAddress", "finalWarningPeriod", "initialWarningPeriod", "notificationPublisherRef"]}

        return cls(**valid_data)
