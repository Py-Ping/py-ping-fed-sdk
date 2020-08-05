class OpenIdConnectSettings():
    """ Settings for the OpenID Connect configuration.

    Attributes
    ----------
    defaultPolicyRef : str
        Reference to the default policy.
    sessionSettings : str
        Settings relating to OpenID Connect session management.

    """

    __slots__ = ["defaultPolicyRef", "sessionSettings"]
    def __init__(self, defaultPolicyRef=None, sessionSettings=None):
            self.defaultPolicyRef = defaultPolicyRef
            self.sessionSettings = sessionSettings
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, OpenIdConnectSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((defaultPolicyRef, sessionSettings))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
