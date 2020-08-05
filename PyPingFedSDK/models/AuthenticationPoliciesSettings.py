class AuthenticationPoliciesSettings():
    """ The settings for the authentication policies.

    Attributes
    ----------
    enableIdpAuthnSelection : boolean
        Enable IdP authentication policies.
    enableSpAuthnSelection : boolean
        Enable SP authentication policies.

    """

    __slots__ = ["enableIdpAuthnSelection", "enableSpAuthnSelection"]
    def __init__(self, enableIdpAuthnSelection=None, enableSpAuthnSelection=None):
            self.enableIdpAuthnSelection = enableIdpAuthnSelection
            self.enableSpAuthnSelection = enableSpAuthnSelection
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AuthenticationPoliciesSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((enableIdpAuthnSelection, enableSpAuthnSelection))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
