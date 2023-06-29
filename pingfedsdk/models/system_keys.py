from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.system_key import SystemKey


class SystemKeys(Model):
    """Secrets that are used in cryptographic operations to generate and consume internal tokens

    Attributes
    ----------
    current: SystemKey
        The current secret.

    previous: SystemKey
        Previously used secret.

    pending: SystemKey
        The next secret.

    """

    def __init__(self, current: SystemKey, pending: SystemKey, previous: SystemKey = None) -> None:
        self.current = current
        self.previous = previous
        self.pending = pending

    def _validate(self) -> bool:
        return any(x for x in ["current", "pending"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SystemKeys):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.current, self.previous, self.pending]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["current", "previous", "pending"] and v is not None:
                if k == "current":
                    valid_data[k] = SystemKey(**v)
                if k == "previous":
                    valid_data[k] = SystemKey(**v)
                if k == "pending":
                    valid_data[k] = SystemKey(**v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["current", "previous", "pending"]:
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
