class ConfigStoreSetting():
    """Single configuration setting.

    Attributes
    ----------
    id : string
        The id of the configuration setting.    listValue : array
        The list of values for the configuration setting. This is used when the setting has a list of string values.    mapValue : str
        The map of key/value pairs for the configuration setting. This is used when the setting has a map of string keys and values.    stringValue : string
        The value of the configuration setting. This is used when the setting has a single string value.    type : str
        The type of configuration setting. This could be a single string, list of strings, or map of string keys and values.
    """

    __slots__ = ["id", "listValue", "mapValue", "stringValue", "type"]

    def __init__(self, id, type, listValue=None, mapValue=None, stringValue=None):
        self.id = id
        self.listValue = listValue
        self.mapValue = mapValue
        self.stringValue = stringValue
        self.type = type

    def _validate(self):
        return any(x for x in ['id', 'type'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ConfigStoreSetting):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.id, self.listValue, self.mapValue, self.stringValue, self.type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["id", "listValue", "mapValue", "stringValue", "type"]}

        return cls(**valid_data)
