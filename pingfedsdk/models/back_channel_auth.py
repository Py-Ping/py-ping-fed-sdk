from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.username_password_credentials import UsernamePasswordCredentials
from pingfedsdk.enums import BackChannelAuthType


class BackChannelAuth(Model):
    """The SOAP authentication methods when sending or receiving a message using SOAP back channel.

    Attributes
    ----------
    type: BackChannelAuthType
        The back channel authentication type.

    httpBasicCredentials: UsernamePasswordCredentials
        The credentials to use when you authenticate with the SOAP endpoint.

    digitalSignature: bool
        If incoming or outgoing messages must be signed.

    """

    def __init__(self, type: BackChannelAuthType, httpBasicCredentials: UsernamePasswordCredentials = None, digitalSignature: bool = None) -> None:
        self.type = type
        self.httpBasicCredentials = httpBasicCredentials
        self.digitalSignature = digitalSignature

    def _validate(self) -> bool:
        return any(x for x in ["type"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, BackChannelAuth):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.httpBasicCredentials, self.digitalSignature]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "httpBasicCredentials", "digitalSignature"] and v is not None:
                if k == "type":
                    valid_data[k] = BackChannelAuthType[v]
                if k == "httpBasicCredentials":
                    valid_data[k] = UsernamePasswordCredentials(**v)
                if k == "digitalSignature":
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
            if k in ["type", "httpBasicCredentials", "digitalSignature"]:
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
