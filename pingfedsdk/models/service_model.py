from enum import Enum

from pingfedsdk.model import Model


class ServiceModel(Model):
    """Service Model.

    Attributes
    ----------
    id: str
        Id of the service.

    sharedSecret: str
        Shared secret for the service.

    encryptedSharedSecret: str
        Encrypted shared secret for the service.

    """
    def __init__(self, id: str = None, sharedSecret: str = None, encryptedSharedSecret: str = None) -> None:
        self.id = id
        self.sharedSecret = sharedSecret
        self.encryptedSharedSecret = encryptedSharedSecret

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ServiceModel):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.sharedSecret, self.encryptedSharedSecret]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "sharedSecret", "encryptedSharedSecret"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "sharedSecret":
                    valid_data[k] = str(v)
                if k == "encryptedSharedSecret":
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
            if k in ["id", "sharedSecret", "encryptedSharedSecret"]:
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
