from enum import Enum

from pingfedsdk.model import Model


class JdbcTagConfig(Model):
    """A JDBC data store's connection URLs and tags configuration. This is required if no default JDBC database location is specified.

    Attributes
    ----------
    connectionUrl: str
        The location of the JDBC database.

    tags: str
        Tags associated with this data source.

    defaultSource: bool
        Whether this is the default connection. Defaults to false if not specified.

    """
    def __init__(self, connectionUrl: str, tags: str = None, defaultSource: bool = None) -> None:
        self.connectionUrl = connectionUrl
        self.tags = tags
        self.defaultSource = defaultSource

    def _validate(self) -> bool:
        return any(x for x in ["connectionUrl"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, JdbcTagConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.connectionUrl, self.tags, self.defaultSource]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["connectionUrl", "tags", "defaultSource"] and v is not None:
                if k == "connectionUrl":
                    valid_data[k] = str(v)
                if k == "tags":
                    valid_data[k] = str(v)
                if k == "defaultSource":
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
            if k in ["connectionUrl", "tags", "defaultSource"]:
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
