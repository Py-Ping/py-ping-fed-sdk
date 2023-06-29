from pingfedsdk.model import Model
from enum import Enum


class OpenIdConnectAttribute(Model):
    """An attribute for the OpenID Connect returned to OAuth clients.

    Attributes
    ----------
    name: str
        The name of this attribute.

    includeInIdToken: bool
        Attribute is included in the ID Token.

    includeInUserInfo: bool
        Attribute is included in the User Info.

    multiValued: bool
        Indicates whether attribute value is always returned as an array.

    """

    def __init__(self, name: str, includeInIdToken: bool = None, includeInUserInfo: bool = None, multiValued: bool = None) -> None:
        self.name = name
        self.includeInIdToken = includeInIdToken
        self.includeInUserInfo = includeInUserInfo
        self.multiValued = multiValued

    def _validate(self) -> bool:
        return any(x for x in ["name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OpenIdConnectAttribute):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.name, self.includeInIdToken, self.includeInUserInfo, self.multiValued]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["name", "includeInIdToken", "includeInUserInfo", "multiValued"] and v is not None:
                if k == "name":
                    valid_data[k] = str(v)
                if k == "includeInIdToken":
                    valid_data[k] = bool(v)
                if k == "includeInUserInfo":
                    valid_data[k] = bool(v)
                if k == "multiValued":
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
            if k in ["name", "includeInIdToken", "includeInUserInfo", "multiValued"]:
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
