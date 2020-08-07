class BaseProviderRole():
    """Base Provider Role.

    Attributes
    ----------
    enable : boolean
    enableSaml10 : boolean
 Enable SAML 1.0.
    enableSaml11 : boolean
 Enable SAML 1.1.
    enableWsFed : boolean
 Enable WS Federation.
    enableWsTrust : boolean
 Enable WS Trust.

    """

    def __init__(self, enable=None, enableSaml10=None, enableSaml11=None, enableWsFed=None, enableWsTrust=None) -> None:
        self.enable = enable
        self.enableSaml10 = enableSaml10
        self.enableSaml11 = enableSaml11
        self.enableWsFed = enableWsFed
        self.enableWsTrust = enableWsTrust

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, BaseProviderRole):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.enable, self.enableSaml10, self.enableSaml11, self.enableWsFed, self.enableWsTrust))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["enable", "enableSaml10", "enableSaml11", "enableWsFed", "enableWsTrust"]}

        return cls(**valid_data)