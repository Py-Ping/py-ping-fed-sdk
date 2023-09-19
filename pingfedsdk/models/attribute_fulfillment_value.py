from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.source_type_id_key import SourceTypeIdKey


class AttributeFulfillmentValue(Model):
    """Defines how an attribute in an attribute contract should be populated.

    Attributes
    ----------
    source: SourceTypeIdKey
        The attribute value source.

    value: str
        The value for this attribute.

    """
    def __init__(self, source: SourceTypeIdKey, value: str) -> None:
        self.source = source
        self.value = value

    def _validate(self) -> bool:
        return any(x for x in ["source", "value"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AttributeFulfillmentValue):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.source, self.value]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["source", "value"] and v is not None:
                if k == "source":
                    valid_data[k] = SourceTypeIdKey.from_dict(v)
                if k == "value":
                    valid_data[k] = str(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["source", "value"]:
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
