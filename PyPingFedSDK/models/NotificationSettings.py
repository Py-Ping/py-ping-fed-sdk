class NotificationSettings():
    """Settings for notifications relating to licensing and certificate expiration.

    Attributes
    ----------
    accountChangesNotificationPublisherRef : str
 Reference to the associated notification publisher for admin user account changes.
    certificateExpirations : str
 Settings for certificate expiration notifications.
    licenseEvents : str
 Settings for license event notifications.
    metadataNotificationSettings : str
 Settings for metadata update event notifications.
    notifyAdminUserPasswordChanges : boolean
 Determines whether admin users are notified through email when their account is changed.

    """

<<<<<<< HEAD
    def __init__(self, accountChangesNotificationPublisherRef=None, certificateExpirations=None, licenseEvents=None, metadataNotificationSettings=None, notifyAdminUserPasswordChanges=None) -> None:
        self.accountChangesNotificationPublisherRef = accountChangesNotificationPublisherRef
        self.certificateExpirations = certificateExpirations
        self.licenseEvents = licenseEvents
        self.metadataNotificationSettings = metadataNotificationSettings
        self.notifyAdminUserPasswordChanges = notifyAdminUserPasswordChanges
=======
    def __init__(self, accountChangesNotificationPublisherRef=None, certificateExpirations=None, licenseEvents=None, metadataNotificationSettings=None, notifyAdminUserPasswordChanges=None):
        self.accountChangesNotificationPublisherRef: str = accountChangesNotificationPublisherRef
        self.certificateExpirations: str = certificateExpirations
        self.licenseEvents: str = licenseEvents
        self.metadataNotificationSettings: str = metadataNotificationSettings
        self.notifyAdminUserPasswordChanges: bool = notifyAdminUserPasswordChanges
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, NotificationSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.accountChangesNotificationPublisherRef, self.certificateExpirations, self.licenseEvents, self.metadataNotificationSettings, self.notifyAdminUserPasswordChanges))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["accountChangesNotificationPublisherRef", "certificateExpirations", "licenseEvents", "metadataNotificationSettings", "notifyAdminUserPasswordChanges"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
