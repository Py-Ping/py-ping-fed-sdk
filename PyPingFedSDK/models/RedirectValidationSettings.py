class RedirectValidationSettings():
    """ Settings for redirect validation for SSO, SLO and IdP discovery.

    Attributes
    ----------
    redirectValidationLocalSettings : str
        Settings for local redirect validation.
    redirectValidationPartnerSettings : str
        Settings for redirection at a partner site.

    """

    __slots__ = ["redirectValidationLocalSettings", "redirectValidationPartnerSettings"]
    def __init__(self, redirectValidationLocalSettings=None, redirectValidationPartnerSettings=None):
            self.redirectValidationLocalSettings = redirectValidationLocalSettings
            self.redirectValidationPartnerSettings = redirectValidationPartnerSettings
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, RedirectValidationSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((redirectValidationLocalSettings, redirectValidationPartnerSettings))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
