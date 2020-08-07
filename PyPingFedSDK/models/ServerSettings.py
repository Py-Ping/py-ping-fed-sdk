class ServerSettings():
    """Server configuration settings.

    Attributes
    ----------
    captchaSettings : str
 Captcha Settings.
    contactInfo : str
 Information that identifies the server.
    emailServer : str
 Email Server Settings.
    federationInfo : str
 Federation Info.
    notifications : str
 Notification settings for license and certificate expiration events.
    rolesAndProtocols : str
 Configure roles and protocols.

    """

<<<<<<< HEAD
    def __init__(self, captchaSettings=None, contactInfo=None, emailServer=None, federationInfo=None, notifications=None, rolesAndProtocols=None) -> None:
        self.captchaSettings = captchaSettings
        self.contactInfo = contactInfo
        self.emailServer = emailServer
        self.federationInfo = federationInfo
        self.notifications = notifications
        self.rolesAndProtocols = rolesAndProtocols
=======
    def __init__(self, captchaSettings=None, contactInfo=None, emailServer=None, federationInfo=None, notifications=None, rolesAndProtocols=None):
        self.captchaSettings: str = captchaSettings
        self.contactInfo: str = contactInfo
        self.emailServer: str = emailServer
        self.federationInfo: str = federationInfo
        self.notifications: str = notifications
        self.rolesAndProtocols: str = rolesAndProtocols
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ServerSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.captchaSettings, self.contactInfo, self.emailServer, self.federationInfo, self.notifications, self.rolesAndProtocols))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["captchaSettings", "contactInfo", "emailServer", "federationInfo", "notifications", "rolesAndProtocols"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
