from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.secondary_secret import SecondarySecret


class ClientSecret(Model):
    """Client Secret.

    Attributes
    ----------
    secret: str
        Client secret for Basic Authentication.  To update the client secret, specify the plaintext value in this field.  This field will not be populated for GET requests.

    encryptedSecret: str
        For GET requests, this field contains the encrypted client secret, if one exists.  For POST and PUT requests, if you wish to reuse the existing secret, this field should be passed back unchanged.

    secondarySecrets: list
        The list of secondary client secrets that are temporarily retained.

    """
    def __init__(self, secret: str = None, encryptedSecret: str = None, secondarySecrets: list = None) -> None:
        self.secret = secret
        self.encryptedSecret = encryptedSecret
        self.secondarySecrets = secondarySecrets

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ClientSecret):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.secret, self.encryptedSecret, self.secondarySecrets]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["secret", "encryptedSecret", "secondarySecrets"] and v is not None:
                if k == "secret":
                    valid_data[k] = str(v)
                if k == "encryptedSecret":
                    valid_data[k] = str(v)
                if k == "secondarySecrets":
                    valid_data[k] = [SecondarySecret.from_dict(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["secret", "encryptedSecret", "secondarySecrets"]:
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
