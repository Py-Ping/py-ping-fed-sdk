from enum import Enum

from pingfedsdk.model import Model


class ConfigField(Model):
    """A plugin configuration field value.

    Attributes
    ----------
    name: str
        The name of the configuration field.

    value: str
        The value for the configuration field. For encrypted or hashed fields, GETs will not return this attribute. To update an encrypted or hashed field, specify the new value in this attribute.

    encryptedValue: str
        For encrypted or hashed fields, this attribute contains the encrypted representation of the field's value, if a value is defined. If you do not want to update the stored value, this attribute should be passed back unchanged.

    inherited: bool
        Whether this field is inherited from its parent instance. If true, the value/encrypted value properties become read-only. The default value is false.

    """
    def __init__(self, name: str, value: str = None, encryptedValue: str = None, inherited: bool = None) -> None:
        self.name = name
        self.value = value
        self.encryptedValue = encryptedValue
        self.inherited = inherited

    def _validate(self) -> bool:
        return any(x for x in ["name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ConfigField):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.name, self.value, self.encryptedValue, self.inherited]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["name", "value", "encryptedValue", "inherited"] and v is not None:
                if k == "name":
                    valid_data[k] = str(v)
                if k == "value":
                    valid_data[k] = str(v)
                if k == "encryptedValue":
                    valid_data[k] = str(v)
                if k == "inherited":
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
            if k in ["name", "value", "encryptedValue", "inherited"]:
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
