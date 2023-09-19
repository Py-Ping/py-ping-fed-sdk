from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.resource_link import ResourceLink


class TokenExchangeGeneratorMapping(Model):
    """A Token Generator mapping into an OAuth 2.0 Token Exchange requested token type.

    Attributes
    ----------
    requestedTokenType: str
        The Requested token type

    tokenGenerator: ResourceLink
        The Token Generator used to generate the requested token

    defaultMapping: bool
        Whether this is the default Token Generator Mapping. Defaults to false if not specified.

    """
    def __init__(self, requestedTokenType: str, tokenGenerator: ResourceLink, defaultMapping: bool = None) -> None:
        self.requestedTokenType = requestedTokenType
        self.tokenGenerator = tokenGenerator
        self.defaultMapping = defaultMapping

    def _validate(self) -> bool:
        return any(x for x in ["requestedTokenType", "tokenGenerator"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, TokenExchangeGeneratorMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.requestedTokenType, self.tokenGenerator, self.defaultMapping]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["requestedTokenType", "tokenGenerator", "defaultMapping"] and v is not None:
                if k == "requestedTokenType":
                    valid_data[k] = str(v)
                if k == "tokenGenerator":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "defaultMapping":
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
            if k in ["requestedTokenType", "tokenGenerator", "defaultMapping"]:
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
