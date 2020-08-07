class ConfigStoreSetting():
    """Single configuration setting.

    Attributes
    ----------
    id : string
 The id of the configuration setting.
    listValue : array
 The list of values for the configuration setting. This is used when the setting has a list of string values.
    mapValue : str
 The map of key/value pairs for the configuration setting. This is used when the setting has a map of string keys and values.
    stringValue : string
 The value of the configuration setting. This is used when the setting has a single string value.
    type : str
 The type of configuration setting. This could be a single string, list of strings, or map of string keys and values.

    """

<<<<<<< HEAD
    def __init__(self, var_id, var_type, listValue=None, mapValue=None, stringValue=None) -> None:
        self.var_id = var_id
        self.listValue = listValue
        self.mapValue = mapValue
        self.stringValue = stringValue
        self.var_type = var_type
=======
    def __init__(self, id, type, listValue=None, mapValue=None, stringValue=None):
        self.id: str = id
        self.listValue: list = listValue
        self.mapValue: str = mapValue
        self.stringValue: str = stringValue
        self.type: str = type
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["var_id", "var_type"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ConfigStoreSetting):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.var_id, self.listValue, self.mapValue, self.stringValue, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["var_id", "listValue", "mapValue", "stringValue", "var_type"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
