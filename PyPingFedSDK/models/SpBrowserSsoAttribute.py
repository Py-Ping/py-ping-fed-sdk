class SpBrowserSsoAttribute():
    """An attribute for the SP Browser SSO attribute contract.

    Attributes
    ----------
    name : string
 The name of this attribute.
    nameFormat : string
 The SAML Name Format for the attribute.

    """

    def __init__(self, nameFormat:str, name:str) -> None:
        self.name = name
        self.nameFormat = nameFormat

    def _validate(self) -> bool:
        return any(x for x in ["nameFormat", "name"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SpBrowserSsoAttribute):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.name, self.nameFormat))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["name", "nameFormat"]}

        return cls(**valid_data)