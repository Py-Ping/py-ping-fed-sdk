from enum import Enum

from pingfedsdk.enums import RadioGroupFieldDescriptorType
from pingfedsdk.model import Model
from pingfedsdk.models.option_value import OptionValue


class RadioGroupFieldDescriptor(Model):
    """A selection-type field intended to be rendered as a group of radio buttons in a UI.

    Attributes
    ----------
    type: RadioGroupFieldDescriptorType
        The type of field descriptor.

    name: str
        Name of the field.

    description: str
        Description of the field.

    defaultValue: str
        Default value of the field.

    advanced: bool
        Whether this is an advanced field or not.

    required: bool
        Whether a value is required for this field or not.

    label: str
        Label of the field to be displayed in the administrative console.

    optionValues: list
        The list of option values for this selection field.

    """
    def __init__(self, type: RadioGroupFieldDescriptorType = None, name: str = None, description: str = None, defaultValue: str = None, advanced: bool = None, required: bool = None, label: str = None, optionValues: list = None) -> None:
        self.type = type
        self.name = name
        self.description = description
        self.defaultValue = defaultValue
        self.advanced = advanced
        self.required = required
        self.label = label
        self.optionValues = optionValues

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, RadioGroupFieldDescriptor):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.name, self.description, self.defaultValue, self.advanced, self.required, self.label, self.optionValues]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "name", "description", "defaultValue", "advanced", "required", "label", "optionValues"] and v is not None:
                if k == "type":
                    valid_data[k] = RadioGroupFieldDescriptorType[v]
                if k == "name":
                    valid_data[k] = str(v)
                if k == "description":
                    valid_data[k] = str(v)
                if k == "defaultValue":
                    valid_data[k] = str(v)
                if k == "advanced":
                    valid_data[k] = bool(v)
                if k == "required":
                    valid_data[k] = bool(v)
                if k == "label":
                    valid_data[k] = str(v)
                if k == "optionValues":
                    valid_data[k] = [OptionValue.from_dict(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["type", "name", "description", "defaultValue", "advanced", "required", "label", "optionValues"]:
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
