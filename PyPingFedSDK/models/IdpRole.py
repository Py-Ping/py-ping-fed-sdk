class IdpRole():
    """This property has been deprecated and is no longer used. All Roles and protocols are always enabled.

    Attributes
    ----------
    enable : boolean
        Enable Identity Provider Role.
    enableOutboundProvisioning : boolean
        Enable Outbound Provisioning.
    enableSaml10 : boolean
        Enable SAML 1.0.
    enableSaml11 : boolean
        Enable SAML 1.1.
    enableWsFed : boolean
        Enable WS Federation.
    enableWsTrust : boolean
        Enable WS Trust.
    saml20Profile : str
        SAML 2.0 Profile settings.

    """

    def __init__(self, enable:bool=None, enableOutboundProvisioning:bool=None, enableSaml10:bool=None, enableSaml11:bool=None, enableWsFed:bool=None, enableWsTrust:bool=None, saml20Profile=None) -> None:
        self.enable = enable
        self.enableOutboundProvisioning = enableOutboundProvisioning
        self.enableSaml10 = enableSaml10
        self.enableSaml11 = enableSaml11
        self.enableWsFed = enableWsFed
        self.enableWsTrust = enableWsTrust
        self.saml20Profile = saml20Profile

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpRole):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.enable, self.enableOutboundProvisioning, self.enableSaml10, self.enableSaml11, self.enableWsFed, self.enableWsTrust, self.saml20Profile]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["enable", "enableOutboundProvisioning", "enableSaml10", "enableSaml11", "enableWsFed", "enableWsTrust", "saml20Profile"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__