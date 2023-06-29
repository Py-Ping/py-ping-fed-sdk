from pingfedsdk.model import Model
from enum import Enum


class ChannelSourceLocation(Model):
    """The location settings that includes a DN and a LDAP filter.

    Attributes
    ----------
    groupDN: str
        The group DN for users or groups.

    filter: str
        An LDAP filter.

    nestedSearch: bool
        Indicates whether the search is nested.

    """

    def __init__(self, groupDN: str = None, filter: str = None, nestedSearch: bool = None) -> None:
        self.groupDN = groupDN
        self.filter = filter
        self.nestedSearch = nestedSearch

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ChannelSourceLocation):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.groupDN, self.filter, self.nestedSearch]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["groupDN", "filter", "nestedSearch"] and v is not None:
                if k == "groupDN":
                    valid_data[k] = str(v)
                if k == "filter":
                    valid_data[k] = str(v)
                if k == "nestedSearch":
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
            if k in ["groupDN", "filter", "nestedSearch"]:
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
