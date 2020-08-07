class LdapDataStoreAttribute():
    """LDAP data store attribute.

    Attributes
    ----------
    metadata : str
    name : string
    type : str
        The data store type.
    """

    __slots__ = ["metadata", "name", "type"]

    def __init__(self, type, metadata=None, name=None):
        self.metadata: str = metadata
        self.name: str = name
        self.type: str = type

    def _validate(self):
        return any(x for x in ['type'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, LdapDataStoreAttribute):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.metadata, self.name, self.type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["metadata", "name", "type"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__