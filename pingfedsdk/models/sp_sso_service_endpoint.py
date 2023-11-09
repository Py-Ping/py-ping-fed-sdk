from enum import Enum

from pingfedsdk.enums import Binding
from pingfedsdk.model import Model


class SpSsoServiceEndpoint(Model):
    """The settings that define a service endpoint to a SP SSO service.

    Attributes
    ----------
    binding: Binding
        The binding of this endpoint, if applicable - usually only required for SAML 2.0 endpoints.  Supported bindings are Artifact and POST.

    url: str
        The absolute or relative URL of the endpoint. A relative URL can be specified if a base URL for the connection has been defined.

    isDefault: bool
        Whether or not this endpoint is the default endpoint. Defaults to false.

    index: int
        The priority of the endpoint.

    """
    def __init__(self, url: str, binding: Binding = None, isDefault: bool = None, index: int = None) -> None:
        self.binding = binding
        self.url = url
        self.isDefault = isDefault
        self.index = index

    def _validate(self) -> bool:
        return any(x for x in ["url"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SpSsoServiceEndpoint):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.binding, self.url, self.isDefault, self.index]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["binding", "url", "isDefault", "index"] and v is not None:
                if k == "binding":
                    valid_data[k] = Binding[v]
                if k == "url":
                    valid_data[k] = str(v)
                if k == "isDefault":
                    valid_data[k] = bool(v)
                if k == "index":
                    valid_data[k] = int(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["binding", "url", "isDefault", "index"]:
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
