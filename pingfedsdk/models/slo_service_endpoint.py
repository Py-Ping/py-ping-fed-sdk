from enum import Enum

from pingfedsdk.enums import Binding
from pingfedsdk.model import Model


class SloServiceEndpoint(Model):
    """Where SLO logout messages are sent. Only applicable for SAML 2.0.

    Attributes
    ----------
    binding: Binding
        The binding of this endpoint, if applicable - usually only required for SAML 2.0 endpoints.

    url: str
        The absolute or relative URL of the endpoint. A relative URL can be specified if a base URL for the connection has been defined.

    responseUrl: str
        The absolute or relative URL to which logout responses are sent. A relative URL can be specified if a base URL for the connection has been defined.

    """
    def __init__(self, binding: Binding, url: str, responseUrl: str = None) -> None:
        self.binding = binding
        self.url = url
        self.responseUrl = responseUrl

    def _validate(self) -> bool:
        return any(x for x in ["binding", "url"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SloServiceEndpoint):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.binding, self.url, self.responseUrl]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["binding", "url", "responseUrl"] and v is not None:
                if k == "binding":
                    valid_data[k] = Binding[v]
                if k == "url":
                    valid_data[k] = str(v)
                if k == "responseUrl":
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
            if k in ["binding", "url", "responseUrl"]:
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
