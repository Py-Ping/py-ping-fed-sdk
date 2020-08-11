class RedirectValidationSettings():
    """Settings for redirect validation for SSO, SLO and IdP discovery.

    Attributes
    ----------
    redirectValidationLocalSettings : str
        Settings for local redirect validation.
    redirectValidationPartnerSettings : str
        Settings for redirection at a partner site.

    """

    def __init__(self, redirectValidationLocalSettings=None, redirectValidationPartnerSettings=None) -> None:
        self.redirectValidationLocalSettings = redirectValidationLocalSettings
        self.redirectValidationPartnerSettings = redirectValidationPartnerSettings

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, RedirectValidationSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.redirectValidationLocalSettings, self.redirectValidationPartnerSettings]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["redirectValidationLocalSettings", "redirectValidationPartnerSettings"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__