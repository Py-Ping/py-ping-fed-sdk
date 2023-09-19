from enum import Enum

from pingfedsdk.model import Model


class OIDCClientCredentials(Model):
    """The OpenID Connect Client Credentials settings. This is required for an OIDC Connection.

    Attributes
    ----------
    clientId: str
        The OpenID Connect client identitification.

    clientSecret: str
        The OpenID Connect client secret. To update the client secret, specify the plaintext value in this field.  This field will not be populated for GET requests.

    encryptedSecret: str
        For GET requests, this field contains the encrypted client secret, if one exists.  For POST and PUT requests, if you wish to reuse the existing secret, this field should be passed back unchanged.

    """
    def __init__(self, clientId: str, clientSecret: str = None, encryptedSecret: str = None) -> None:
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.encryptedSecret = encryptedSecret

    def _validate(self) -> bool:
        return any(x for x in ["clientId"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OIDCClientCredentials):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.clientId, self.clientSecret, self.encryptedSecret]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["clientId", "clientSecret", "encryptedSecret"] and v is not None:
                if k == "clientId":
                    valid_data[k] = str(v)
                if k == "clientSecret":
                    valid_data[k] = str(v)
                if k == "encryptedSecret":
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
            if k in ["clientId", "clientSecret", "encryptedSecret"]:
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
