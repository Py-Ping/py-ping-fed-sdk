from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.token_processor_attribute import TokenProcessorAttribute


class TokenProcessorAttributeContract(Model):
    """A set of attributes exposed by a token processor.

    Attributes
    ----------
    coreAttributes: list
        A list of token processor attributes that correspond to the attributes exposed by the token processor type.

    extendedAttributes: list
        A list of additional attributes that can be returned by the token processor. The extended attributes are only used if the token processor supports them.

    maskOgnlValues: bool
        Whether or not all OGNL expressions used to fulfill an outgoing assertion contract should be masked in the logs. Defaults to false.

    inherited: bool
        Whether this attribute contract is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false.

    """

    def __init__(self, coreAttributes: list, extendedAttributes: list = None, maskOgnlValues: bool = None, inherited: bool = None) -> None:
        self.coreAttributes = coreAttributes
        self.extendedAttributes = extendedAttributes
        self.maskOgnlValues = maskOgnlValues
        self.inherited = inherited

    def _validate(self) -> bool:
        return any(x for x in ["coreAttributes"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, TokenProcessorAttributeContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.coreAttributes, self.extendedAttributes, self.maskOgnlValues, self.inherited]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["coreAttributes", "extendedAttributes", "maskOgnlValues", "inherited"] and v is not None:
                if k == "coreAttributes":
                    valid_data[k] = [TokenProcessorAttribute(**x) for x in v]
                if k == "extendedAttributes":
                    valid_data[k] = [TokenProcessorAttribute(**x) for x in v]
                if k == "maskOgnlValues":
                    valid_data[k] = bool(v)
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
            if k in ["coreAttributes", "extendedAttributes", "maskOgnlValues", "inherited"]:
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
