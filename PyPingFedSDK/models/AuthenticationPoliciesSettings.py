class AuthenticationPoliciesSettings():
    """The settings for the authentication policies.

    Attributes
    ----------
    enableIdpAuthnSelection : boolean
 Enable IdP authentication policies.
    enableSpAuthnSelection : boolean
 Enable SP authentication policies.

    """

    def __init__(self, enableIdpAuthnSelection=None, enableSpAuthnSelection=None) -> None:
        self.enableIdpAuthnSelection = enableIdpAuthnSelection
        self.enableSpAuthnSelection = enableSpAuthnSelection

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthenticationPoliciesSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.enableIdpAuthnSelection, self.enableSpAuthnSelection))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["enableIdpAuthnSelection", "enableSpAuthnSelection"]}

        return cls(**valid_data)