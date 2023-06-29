from pingfedsdk.model import Model
from enum import Enum


class SpSAML20Profile(Model):
    """SP SAML 2.0 Profile.

    Attributes
    ----------
    enable: bool
        Enable SAML2.0 profile.

    enableAutoConnect: bool
        This property has been deprecated and no longer used

    enableXASP: bool
        Enable Attribute Requester Mapping for X.509 Attribute Sharing Profile (XASP)

    """

    def __init__(self, enable: bool = None, enableAutoConnect: bool = None, enableXASP: bool = None) -> None:
        self.enable = enable
        self.enableAutoConnect = enableAutoConnect
        self.enableXASP = enableXASP

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SpSAML20Profile):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.enable, self.enableAutoConnect, self.enableXASP]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["enable", "enableAutoConnect", "enableXASP"] and v is not None:
                if k == "enable":
                    valid_data[k] = bool(v)
                if k == "enableAutoConnect":
                    valid_data[k] = bool(v)
                if k == "enableXASP":
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
            if k in ["enable", "enableAutoConnect", "enableXASP"]:
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
