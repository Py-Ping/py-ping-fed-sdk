class LdapDataStoreAttribute():
    """LDAP data store attribute.

    Attributes
    ----------
    metadata : str
    name : string
    type : str
        The data store type.

    """

    def __init__(self, var_type, metadata=None, name:str=None) -> None:
        self.metadata = metadata
        self.name = name
        self.var_type = var_type

    def _validate(self) -> bool:
        return any(x for x in ["var_type"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, LdapDataStoreAttribute):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.metadata, self.name, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["metadata", "name", "var_type"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__