class SpSAML20Profile():
    """SP SAML 2.0 Profile.

    Attributes
    ----------
    enable : boolean
        Enable SAML2.0 profile.    enableAutoConnect : boolean
        This property has been deprecated and no longer used    enableXASP : boolean
        Enable Attribute Requester Mapping for X.509 Attribute Sharing Profile (XASP)
    """

    __slots__ = ["enable", "enableAutoConnect", "enableXASP"]

    def __init__(self, enable=None, enableAutoConnect=None, enableXASP=None):
        self.enable = enable
        self.enableAutoConnect = enableAutoConnect
        self.enableXASP = enableXASP

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, SpSAML20Profile):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.enable, self.enableAutoConnect, self.enableXASP))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["enable", "enableAutoConnect", "enableXASP"]}

        return cls(**valid_data)
