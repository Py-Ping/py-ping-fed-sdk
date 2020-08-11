class DataStore():
    """The set of attributes used to configure a data store.

    Attributes
    ----------
    id : string
        The persistent, unique ID for the data store. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.
    maskAttributeValues : boolean
        Whether attribute values should be masked in the log.
    type : str
        The data store type.

    """

    def __init__(self, var_type, var_id:str=None, maskAttributeValues:bool=None) -> None:
        self.var_id = var_id
        self.maskAttributeValues = maskAttributeValues
        self.var_type = var_type

    def _validate(self) -> bool:
        return any(x for x in ["var_type"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, DataStore):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.var_id, self.maskAttributeValues, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["var_id", "maskAttributeValues", "var_type"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__