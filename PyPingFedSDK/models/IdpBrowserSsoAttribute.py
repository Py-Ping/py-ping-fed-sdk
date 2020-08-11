class IdpBrowserSsoAttribute():
    """An attribute for the IdP Browser SSO attribute contract.

    Attributes
    ----------
    masked : boolean
        Specifies whether this attribute is masked in PingFederate logs. Defaults to false.
    name : string
        The name of this attribute.

    """

    def __init__(self, name:str, masked:bool=None) -> None:
        self.masked = masked
        self.name = name

    def _validate(self) -> bool:
        return any(x for x in ["name"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpBrowserSsoAttribute):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.masked, self.name))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["masked", "name"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__