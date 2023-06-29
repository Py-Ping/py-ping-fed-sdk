from pingfedsdk.model import Model
from enum import Enum


class ApplicationSessionPolicy(Model):
    """Session controls for user facing PingFederate application endpoints, such as the profile management endpoint.

    Attributes
    ----------
    idleTimeoutMins: int
        The idle timeout period, in minutes. If set to -1, the idle timeout will be set to the maximum timeout. The default is 60.

    maxTimeoutMins: int
        The maximum timeout period, in minutes. If set to -1, sessions do not expire. The default is 480.

    """

    def __init__(self, idleTimeoutMins: int = None, maxTimeoutMins: int = None) -> None:
        self.idleTimeoutMins = idleTimeoutMins
        self.maxTimeoutMins = maxTimeoutMins

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ApplicationSessionPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.idleTimeoutMins, self.maxTimeoutMins]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["idleTimeoutMins", "maxTimeoutMins"] and v is not None:
                if k == "idleTimeoutMins":
                    valid_data[k] = int(v)
                if k == "maxTimeoutMins":
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
            if k in ["idleTimeoutMins", "maxTimeoutMins"]:
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
