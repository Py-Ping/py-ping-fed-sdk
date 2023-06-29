from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.enums import CryptoProvider


class X509File(Model):
    """Encoded certificate data.

    Attributes
    ----------
    id: str
        The persistent, unique ID for the certificate. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified.

    fileData: str
        The certificate data in PEM format. New line characters should be omitted or encoded in this value.

    cryptoProvider: CryptoProvider
        Cryptographic Provider. This is only applicable if Hybrid HSM mode is true.

    """

    def __init__(self, fileData: str, id: str = None, cryptoProvider: CryptoProvider = None) -> None:
        self.id = id
        self.fileData = fileData
        self.cryptoProvider = cryptoProvider

    def _validate(self) -> bool:
        return any(x for x in ["fileData"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, X509File):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.fileData, self.cryptoProvider]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "fileData", "cryptoProvider"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "fileData":
                    valid_data[k] = str(v)
                if k == "cryptoProvider":
                    valid_data[k] = CryptoProvider[v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "fileData", "cryptoProvider"]:
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
