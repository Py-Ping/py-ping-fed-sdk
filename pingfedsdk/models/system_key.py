from pingfedsdk.model import Model
from enum import Enum


class SystemKey(Model):
    """A system key.

    Attributes
    ----------
    creationDate: str
        Creation time of the key.

    encryptedKeyData: str
        The system key encrypted.

    keyData: str
        The clear text system key base 64 encoded. The system key must be 32 bytes before base 64 encoding.

    """

    def __init__(self, creationDate: str = None, encryptedKeyData: str = None, keyData: str = None) -> None:
        self.creationDate = creationDate
        self.encryptedKeyData = encryptedKeyData
        self.keyData = keyData

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SystemKey):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.creationDate, self.encryptedKeyData, self.keyData]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["creationDate", "encryptedKeyData", "keyData"] and v is not None:
                if k == "creationDate":
                    valid_data[k] = str(v)
                if k == "encryptedKeyData":
                    valid_data[k] = str(v)
                if k == "keyData":
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
            if k in ["creationDate", "encryptedKeyData", "keyData"]:
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
