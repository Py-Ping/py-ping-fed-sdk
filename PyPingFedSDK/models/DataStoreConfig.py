class DataStoreConfig():
    """Local identity profile data store.

    Attributes
    ----------
    dataStoreMapping : str
        The data store mapping.    dataStoreRef : str
        Reference to the associated data store.    type : str
        The data store config type.
    """

    __slots__ = ["dataStoreMapping", "dataStoreRef", "type"]

    def __init__(self, type, dataStoreRef, dataStoreMapping=None):
        self.dataStoreMapping: str = dataStoreMapping
        self.dataStoreRef: str = dataStoreRef
        self.type: str = type

    def _validate(self):
        return any(x for x in ['type', 'dataStoreRef'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, DataStoreConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.dataStoreMapping, self.dataStoreRef, self.type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["dataStoreMapping", "dataStoreRef", "type"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__