from enum import Enum

from pingfedsdk.enums import HiddenLocalIdentityFieldType
from pingfedsdk.model import Model


class HiddenLocalIdentityField(Model):
    """A hidden selection type field.

    Attributes
    ----------
    type: HiddenLocalIdentityFieldType
        The type of the local identity field.

    id: str
        Id of the local identity field.

    label: str
        Label of the local identity field.

    registrationPageField: bool
        Whether this is a registration page field or not.

    profilePageField: bool
        Whether this is a profile page field or not.

    attributes: dict
        Attributes of the local identity field.

    """
    def __init__(self, type: HiddenLocalIdentityFieldType, id: str, label: str, registrationPageField: bool = None, profilePageField: bool = None, attributes: dict = None) -> None:
        self.type = type
        self.id = id
        self.label = label
        self.registrationPageField = registrationPageField
        self.profilePageField = profilePageField
        self.attributes = attributes

    def _validate(self) -> bool:
        return any(x for x in ["id", "label", "type"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, HiddenLocalIdentityField):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.id, self.label, self.registrationPageField, self.profilePageField, self.attributes]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "id", "label", "registrationPageField", "profilePageField", "attributes"] and v is not None:
                if k == "type":
                    valid_data[k] = HiddenLocalIdentityFieldType[v]
                if k == "id":
                    valid_data[k] = str(v)
                if k == "label":
                    valid_data[k] = str(v)
                if k == "registrationPageField":
                    valid_data[k] = bool(v)
                if k == "profilePageField":
                    valid_data[k] = bool(v)
                if k == "attributes":
                    valid_data[k] = {str(x): bool(y) for x, y in v.items()}

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["type", "id", "label", "registrationPageField", "profilePageField", "attributes"]:
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