class RegistrationConfig():
    """A local identity profile registration configuration.

    Attributes
    ----------
    captchaEnabled : boolean
        Whether CAPTCHA is enabled or not in the registration configuration.
    createAuthnSessionAfterRegistration : boolean
        Whether to create an Authentication Session when registering a local account. Default is true.
    templateName : string
        The template name for the registration configuration.
    thisIsMyDeviceEnabled : boolean
        Allows users to indicate whether their device is shared or private. In this mode, PingFederate Authentication Sessions will not be stored unless the user indicates the device is private.
    usernameField : string
        When creating an Authentication Session after registering a local account, PingFederate will pass the Unique ID field's value as the username. If the Unique ID value is not the username, then override which field's value will be used as the username.

    """

    def __init__(self, templateName:str, captchaEnabled:bool=None, createAuthnSessionAfterRegistration:bool=None, thisIsMyDeviceEnabled:bool=None, usernameField:str=None) -> None:
        self.captchaEnabled = captchaEnabled
        self.createAuthnSessionAfterRegistration = createAuthnSessionAfterRegistration
        self.templateName = templateName
        self.thisIsMyDeviceEnabled = thisIsMyDeviceEnabled
        self.usernameField = usernameField

    def _validate(self) -> bool:
        return any(x for x in ["templateName"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, RegistrationConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.captchaEnabled, self.createAuthnSessionAfterRegistration, self.templateName, self.thisIsMyDeviceEnabled, self.usernameField]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["captchaEnabled", "createAuthnSessionAfterRegistration", "templateName", "thisIsMyDeviceEnabled", "usernameField"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__