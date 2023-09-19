from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.local_identity_field import LocalIdentityField


class FieldConfig(Model):
    """A local identity profile field configuration.

    Attributes
    ----------
    fields: list
        The field configuration for the local identity profile.

    stripSpaceFromUniqueField: bool
        Strip leading/trailing spaces from unique ID field. Default is true.

    """
    def __init__(self, fields: list = None, stripSpaceFromUniqueField: bool = None) -> None:
        self.fields = fields
        self.stripSpaceFromUniqueField = stripSpaceFromUniqueField

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, FieldConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.fields, self.stripSpaceFromUniqueField]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["fields", "stripSpaceFromUniqueField"] and v is not None:
                if k == "fields":
                    valid_data[k] = [LocalIdentityField.from_dict(x) for x in v]
                if k == "stripSpaceFromUniqueField":
                    valid_data[k] = bool(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["fields", "stripSpaceFromUniqueField"]:
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
