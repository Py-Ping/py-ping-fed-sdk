from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.enums import ConfigStoreSettingType


class ConfigStoreSetting(Model):
    """Single configuration setting.

    Attributes
    ----------
    id: str
        The id of the configuration setting.

    stringValue: str
        The value of the configuration setting. This is used when the setting has a single string value.

    listValue: list
        The list of values for the configuration setting. This is used when the setting has a list of string values.

    mapValue: object
        The map of key/value pairs for the configuration setting. This is used when the setting has a map of string keys and values.

    type: ConfigStoreSettingType
        The type of configuration setting. This could be a single string, list of strings, or map of string keys and values.

    """

    def __init__(self, id: str, type: ConfigStoreSettingType, stringValue: str = None, listValue: list = None, mapValue: object = None) -> None:
        self.id = id
        self.stringValue = stringValue
        self.listValue = listValue
        self.mapValue = mapValue
        self.type = type

    def _validate(self) -> bool:
        return any(x for x in ["id", "type"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ConfigStoreSetting):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.stringValue, self.listValue, self.mapValue, self.type]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "stringValue", "listValue", "mapValue", "type"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "stringValue":
                    valid_data[k] = str(v)
                if k == "listValue":
                    valid_data[k] = [str(x) for x in v]
                if k == "mapValue":
                    valid_data[k] = object(**v)
                if k == "type":
                    valid_data[k] = ConfigStoreSettingType[v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "stringValue", "listValue", "mapValue", "type"]:
                if isinstance(v, Model):
                    body[k] = v.to_dict(remove_nonetypes)
                elif isinstance(v, list):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, dict):
                    vals = {}
                    for x, y in v.items():
                        if isinstance(y, Model):
                            vals[x] = y.to_dict(remove_nonetypes)
                        elif not remove_nonetypes or (remove_nonetypes and y is not None):
                            vals[x] = y
                    body[k] = vals
                elif isinstance(v, set):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, Enum):
                    body[k] = str(v).split('.')[-1]
                elif not remove_nonetypes or (remove_nonetypes and v is not None):
                    body[k] = v
        return body
