class NotificationSettings():
    """ Settings for notifications relating to licensing and certificate expiration.

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

    __slots__ = ["accountChangesNotificationPublisherRef", "certificateExpirations", "licenseEvents", "metadataNotificationSettings", "notifyAdminUserPasswordChanges"]
    def __init__(self, accountChangesNotificationPublisherRef=None, certificateExpirations=None, licenseEvents=None, metadataNotificationSettings=None, notifyAdminUserPasswordChanges=None):
            self.accountChangesNotificationPublisherRef = accountChangesNotificationPublisherRef
            self.certificateExpirations = certificateExpirations
            self.licenseEvents = licenseEvents
            self.metadataNotificationSettings = metadataNotificationSettings
            self.notifyAdminUserPasswordChanges = notifyAdminUserPasswordChanges
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, NotificationSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((accountChangesNotificationPublisherRef, certificateExpirations, licenseEvents, metadataNotificationSettings, notifyAdminUserPasswordChanges))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
