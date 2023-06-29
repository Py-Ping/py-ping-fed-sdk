from pingfedsdk.model import Model
from enum import Enum


class SchemaAttribute(Model):
    """A custom SCIM attribute.

    Attributes
    ----------
    name: str
        Name of the attribute.

    multiValued: bool
        Indicates whether the attribute is multi-valued.

    types: list
        Represents the name of each attribute type in case of multi-valued attribute.

    subAttributes: list
        List of sub-attributes for an attribute.

    """

    def __init__(self, name: str = None, multiValued: bool = None, types: list = None, subAttributes: list = None) -> None:
        self.name = name
        self.multiValued = multiValued
        self.types = types
        self.subAttributes = subAttributes

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SchemaAttribute):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.name, self.multiValued, self.types, self.subAttributes]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["name", "multiValued", "types", "subAttributes"] and v is not None:
                if k == "name":
                    valid_data[k] = str(v)
                if k == "multiValued":
                    valid_data[k] = bool(v)
                if k == "types":
                    valid_data[k] = [str(x) for x in v]
                if k == "subAttributes":
                    valid_data[k] = [str(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["name", "multiValued", "types", "subAttributes"]:
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
