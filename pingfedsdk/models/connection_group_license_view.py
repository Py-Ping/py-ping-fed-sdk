from enum import Enum

from pingfedsdk.model import Model


class ConnectionGroupLicenseView(Model):
    """Connection group license information.

    Attributes
    ----------
    name: str
        Group name from the license file.

    connectionCount: int
        Maximum number of connections permitted under the group.

    startDate: str
        Start date for the group.

    endDate: str
        End date for the group.

    """
    def __init__(self, name: str = None, connectionCount: int = None, startDate: str = None, endDate: str = None) -> None:
        self.name = name
        self.connectionCount = connectionCount
        self.startDate = startDate
        self.endDate = endDate

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ConnectionGroupLicenseView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.name, self.connectionCount, self.startDate, self.endDate]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["name", "connectionCount", "startDate", "endDate"] and v is not None:
                if k == "name":
                    valid_data[k] = str(v)
                if k == "connectionCount":
                    valid_data[k] = int(v)
                if k == "startDate":
                    valid_data[k] = str(v)
                if k == "endDate":
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
            if k in ["name", "connectionCount", "startDate", "endDate"]:
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
