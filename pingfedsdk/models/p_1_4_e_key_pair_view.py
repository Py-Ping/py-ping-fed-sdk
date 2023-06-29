from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.cert_view import CertView


class P14EKeyPairView(Model):
    """PingOne for Enterprise connection key pair details.

    Attributes
    ----------
    currentAuthenticationKey: bool
        Indicates whether this is the current key used to authenticate with PingOne.

    previousAuthenticationKey: bool
        Indicates whether this is the previous key used to authenticate with PingOne.

    keyPairView: CertView
        The PingOne for Enterprise key pair details.

    creationTime: str
        The creation time of the key.

    """

    def __init__(self, currentAuthenticationKey: bool = None, previousAuthenticationKey: bool = None, keyPairView: CertView = None, creationTime: str = None) -> None:
        self.currentAuthenticationKey = currentAuthenticationKey
        self.previousAuthenticationKey = previousAuthenticationKey
        self.keyPairView = keyPairView
        self.creationTime = creationTime

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, P14EKeyPairView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.currentAuthenticationKey, self.previousAuthenticationKey, self.keyPairView, self.creationTime]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["currentAuthenticationKey", "previousAuthenticationKey", "keyPairView", "creationTime"] and v is not None:
                if k == "currentAuthenticationKey":
                    valid_data[k] = bool(v)
                if k == "previousAuthenticationKey":
                    valid_data[k] = bool(v)
                if k == "keyPairView":
                    valid_data[k] = CertView(**v)
                if k == "creationTime":
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
            if k in ["currentAuthenticationKey", "previousAuthenticationKey", "keyPairView", "creationTime"]:
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
