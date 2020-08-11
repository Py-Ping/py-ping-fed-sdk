class SpSAML20Profile():
    """SP SAML 2.0 Profile.

    Attributes
    ----------
    enable : boolean
 Enable SAML2.0 profile.
    enableAutoConnect : boolean
 This property has been deprecated and no longer used
    enableXASP : boolean
 Enable Attribute Requester Mapping for X.509 Attribute Sharing Profile (XASP)

    """

    def __init__(self, enable:bool=None, enableAutoConnect:bool=None, enableXASP:bool=None) -> None:
        self.enable = enable
        self.enableAutoConnect = enableAutoConnect
        self.enableXASP = enableXASP

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SpSAML20Profile):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.enable, self.enableAutoConnect, self.enableXASP))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["enable", "enableAutoConnect", "enableXASP"]}

        return cls(**valid_data)