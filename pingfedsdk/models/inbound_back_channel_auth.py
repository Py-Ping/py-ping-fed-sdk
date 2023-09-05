from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.connection_cert import ConnectionCert
from pingfedsdk.models.username_password_credentials import UsernamePasswordCredentials
from pingfedsdk.enums import InboundBackChannelAuthType


class InboundBackChannelAuth(Model):
    """The SOAP authentication methods when sending or receiving a message using SOAP back channel.

    Attributes
    ----------
    type: InboundBackChannelAuthType
        The back channel authentication type.

    httpBasicCredentials: UsernamePasswordCredentials
        The credentials to use when you authenticate with the SOAP endpoint.

    digitalSignature: bool
        If incoming or outgoing messages must be signed.

    verificationSubjectDN: str
        If this property is set, the verification trust model is Anchored. The verification certificate must be signed by a trusted CA and included in the incoming message, and the subject DN of the expected certificate is specified in this property. If this property is not set, then a primary verification certificate must be specified in the certs array.

    verificationIssuerDN: str
        If a verification Subject DN is provided, you can optionally restrict the issuer to a specific trusted CA by specifying its DN in this field.

    certs: list
        The certificate used for signature verification and XML encryption.

    requireSsl: bool
        Incoming HTTP transmissions must use a secure channel.

    """

    def __init__(self, type: InboundBackChannelAuthType, httpBasicCredentials: UsernamePasswordCredentials = None, digitalSignature: bool = None, verificationSubjectDN: str = None, verificationIssuerDN: str = None, certs: list = None, requireSsl: bool = None) -> None:
        self.type = type
        self.httpBasicCredentials = httpBasicCredentials
        self.digitalSignature = digitalSignature
        self.verificationSubjectDN = verificationSubjectDN
        self.verificationIssuerDN = verificationIssuerDN
        self.certs = certs
        self.requireSsl = requireSsl

    def _validate(self) -> bool:
        return any(x for x in ["type"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, InboundBackChannelAuth):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.httpBasicCredentials, self.digitalSignature, self.verificationSubjectDN, self.verificationIssuerDN, self.certs, self.requireSsl]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "httpBasicCredentials", "digitalSignature", "verificationSubjectDN", "verificationIssuerDN", "certs", "requireSsl"] and v is not None:
                if k == "type":
                    valid_data[k] = InboundBackChannelAuthType[v]
                if k == "httpBasicCredentials":
                    valid_data[k] = UsernamePasswordCredentials(**v)
                if k == "digitalSignature":
                    valid_data[k] = bool(v)
                if k == "verificationSubjectDN":
                    valid_data[k] = str(v)
                if k == "verificationIssuerDN":
                    valid_data[k] = str(v)
                if k == "certs":
                    valid_data[k] = [ConnectionCert(**x) for x in v]
                if k == "requireSsl":
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
            if k in ["type", "httpBasicCredentials", "digitalSignature", "verificationSubjectDN", "verificationIssuerDN", "certs", "requireSsl"]:
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
