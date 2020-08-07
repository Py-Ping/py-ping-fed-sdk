class DataStoreConfig():
    """Local identity profile data store.

    Attributes
    ----------
    dataStoreMapping : str
 The data store mapping.
    dataStoreRef : str
 Reference to the associated data store.
    type : str
 The data store config type.

    """

<<<<<<< HEAD
    def __init__(self, var_type, dataStoreRef, dataStoreMapping=None) -> None:
        self.dataStoreMapping = dataStoreMapping
        self.dataStoreRef = dataStoreRef
        self.var_type = var_type
=======
    def __init__(self, type, dataStoreRef, dataStoreMapping=None):
        self.dataStoreMapping: str = dataStoreMapping
        self.dataStoreRef: str = dataStoreRef
        self.type: str = type
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["var_type", "dataStoreRef"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, DataStoreConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.dataStoreMapping, self.dataStoreRef, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["dataStoreMapping", "dataStoreRef", "var_type"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
