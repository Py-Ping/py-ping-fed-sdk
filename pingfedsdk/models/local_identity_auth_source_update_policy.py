from enum import Enum

from pingfedsdk.model import Model


class LocalIdentityAuthSourceUpdatePolicy(Model):
    """Settings to determine whether to store attributes that came from third-party authentication sources.

    Attributes
    ----------
    storeAttributes: bool
        Whether or not to store attributes that came from authentication sources.

    retainAttributes: bool
        Whether or not to keep attributes after user disconnects.

    updateAttributes: bool
        Whether or not to update attributes when users authenticate.

    updateInterval: float
        The minimum number of days between updates.

    """
    def __init__(self, storeAttributes: bool = None, retainAttributes: bool = None, updateAttributes: bool = None, updateInterval: float = None) -> None:
        self.storeAttributes = storeAttributes
        self.retainAttributes = retainAttributes
        self.updateAttributes = updateAttributes
        self.updateInterval = updateInterval

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, LocalIdentityAuthSourceUpdatePolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.storeAttributes, self.retainAttributes, self.updateAttributes, self.updateInterval]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["storeAttributes", "retainAttributes", "updateAttributes", "updateInterval"] and v is not None:
                if k == "storeAttributes":
                    valid_data[k] = bool(v)
                if k == "retainAttributes":
                    valid_data[k] = bool(v)
                if k == "updateAttributes":
                    valid_data[k] = bool(v)
                if k == "updateInterval":
                    valid_data[k] = float(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["storeAttributes", "retainAttributes", "updateAttributes", "updateInterval"]:
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
