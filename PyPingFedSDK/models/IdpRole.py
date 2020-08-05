class IdpRole():
    """ Identity Provider (IdP) role settings.

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

    __slots__ = ["enable", "enableOutboundProvisioning", "enableSaml10", "enableSaml11", "enableWsFed", "enableWsTrust", "saml20Profile"]
    def __init__(self, enable=None, enableOutboundProvisioning=None, enableSaml10=None, enableSaml11=None, enableWsFed=None, enableWsTrust=None, saml20Profile=None):
            self.enable = enable
            self.enableOutboundProvisioning = enableOutboundProvisioning
            self.enableSaml10 = enableSaml10
            self.enableSaml11 = enableSaml11
            self.enableWsFed = enableWsFed
            self.enableWsTrust = enableWsTrust
            self.saml20Profile = saml20Profile
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, IdpRole):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((enable, enableOutboundProvisioning, enableSaml10, enableSaml11, enableWsFed, enableWsTrust, saml20Profile))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
