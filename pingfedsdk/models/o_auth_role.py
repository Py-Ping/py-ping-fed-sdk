from enum import Enum

from pingfedsdk.model import Model


class OAuthRole(Model):
    """This property has been deprecated and is no longer used. OAuth and OpenID Connect are always enabled.

    Attributes
    ----------
    enableOauth: bool
        Enable OAuth 2.0 Authorization Server (AS) Role.

    enableOpenIdConnect: bool
        Enable Open ID Connect.

    """
    def __init__(self, enableOauth: bool = None, enableOpenIdConnect: bool = None) -> None:
        self.enableOauth = enableOauth
        self.enableOpenIdConnect = enableOpenIdConnect

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OAuthRole):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.enableOauth, self.enableOpenIdConnect]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["enableOauth", "enableOpenIdConnect"] and v is not None:
                if k == "enableOauth":
                    valid_data[k] = bool(v)
                if k == "enableOpenIdConnect":
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
            if k in ["enableOauth", "enableOpenIdConnect"]:
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