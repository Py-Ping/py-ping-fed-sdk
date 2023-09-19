from enum import Enum

from pingfedsdk.model import Model


class AttributeQueryNameMapping(Model):
    """The attribute query name mappings between the SP and the IdP.

    Attributes
    ----------
    localName: str
        The local attribute name.

    remoteName: str
        The remote attribute name as defined by the attribute authority.

    """
    def __init__(self, localName: str, remoteName: str) -> None:
        self.localName = localName
        self.remoteName = remoteName

    def _validate(self) -> bool:
        return any(x for x in ["localName", "remoteName"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AttributeQueryNameMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.localName, self.remoteName]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["localName", "remoteName"] and v is not None:
                if k == "localName":
                    valid_data[k] = str(v)
                if k == "remoteName":
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
            if k in ["localName", "remoteName"]:
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
