class DataStoreAttribute():
    """The data store attribute.

    Attributes
    ----------
    metadata : str
 The data store attribute metadata.
    name : string
 The data store attribute name.
    type : str
 The data store attribute type.

    """

    def __init__(self, var_type, name, metadata=None) -> None:
        self.metadata = metadata
        self.name = name
        self.var_type = var_type

    def _validate(self) -> bool:
        return any(x for x in ["var_type", "name"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, DataStoreAttribute):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.metadata, self.name, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["metadata", "name", "var_type"]}

        return cls(**valid_data)