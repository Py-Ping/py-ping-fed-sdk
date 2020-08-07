class OpenIdConnectSettings():
    """Settings for the OpenID Connect configuration.

    Attributes
    ----------
    defaultPolicyRef : str
 Reference to the default policy.
    sessionSettings : str
 Settings relating to OpenID Connect session management.

    """

    def __init__(self, defaultPolicyRef=None, sessionSettings=None) -> None:
        self.defaultPolicyRef = defaultPolicyRef
        self.sessionSettings = sessionSettings

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, OpenIdConnectSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.defaultPolicyRef, self.sessionSettings))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["defaultPolicyRef", "sessionSettings"]}

        return cls(**valid_data)