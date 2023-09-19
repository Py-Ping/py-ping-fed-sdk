from enum import Enum

from pingfedsdk.enums import CharacterCase
from pingfedsdk.enums import Parser
from pingfedsdk.model import Model


class SaasFieldConfiguration(Model):
    """The settings that represent how attribute values from source data store will be mapped into Fields specified by the service provider.

    Attributes
    ----------
    attributeNames: list
        The list of source attribute names used to generate or map to a target field

    defaultValue: str
        The default value for the target field

    expression: str
        An OGNL expression to obtain a value.

    createOnly: bool
        Indicates whether this field is a create only field and cannot be updated.

    trim: bool
        Indicates whether field should be trimmed before provisioning.

    characterCase: CharacterCase
        The character case of the field value.

    parser: Parser
        Indicates how the field shall be parsed.

    masked: bool
        Indicates whether the attribute should be masked in server logs.

    """
    def __init__(self, attributeNames: list = None, defaultValue: str = None, expression: str = None, createOnly: bool = None, trim: bool = None, characterCase: CharacterCase = None, parser: Parser = None, masked: bool = None) -> None:
        self.attributeNames = attributeNames
        self.defaultValue = defaultValue
        self.expression = expression
        self.createOnly = createOnly
        self.trim = trim
        self.characterCase = characterCase
        self.parser = parser
        self.masked = masked

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SaasFieldConfiguration):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.attributeNames, self.defaultValue, self.expression, self.createOnly, self.trim, self.characterCase, self.parser, self.masked]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["attributeNames", "defaultValue", "expression", "createOnly", "trim", "characterCase", "parser", "masked"] and v is not None:
                if k == "attributeNames":
                    valid_data[k] = [str(x) for x in v]
                if k == "defaultValue":
                    valid_data[k] = str(v)
                if k == "expression":
                    valid_data[k] = str(v)
                if k == "createOnly":
                    valid_data[k] = bool(v)
                if k == "trim":
                    valid_data[k] = bool(v)
                if k == "characterCase":
                    valid_data[k] = CharacterCase[v]
                if k == "parser":
                    valid_data[k] = Parser[v]
                if k == "masked":
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
            if k in ["attributeNames", "defaultValue", "expression", "createOnly", "trim", "characterCase", "parser", "masked"]:
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
