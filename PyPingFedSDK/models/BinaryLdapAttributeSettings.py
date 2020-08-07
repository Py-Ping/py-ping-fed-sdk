class BinaryLdapAttributeSettings():
    """Binary settings for a LDAP attribute.

    Attributes
    ----------
    binaryEncoding : str
 Get the encoding type for this attribute. If not specified, the default is BASE64.

    """

    def __init__(self, binaryEncoding=None) -> None:
        self.binaryEncoding = binaryEncoding

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, BinaryLdapAttributeSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.binaryEncoding))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["binaryEncoding"]}

        return cls(**valid_data)