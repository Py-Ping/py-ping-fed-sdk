from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.models.username_password_credentials import UsernamePasswordCredentials
from pingfedsdk.enums import BackChannelAuthType


class OutboundBackChannelAuth(Model):
    """The SOAP authentication methods when sending or receiving a message using SOAP back channel.

    Attributes
    ----------
    type: BackChannelAuthType
        The back channel authentication type.

    httpBasicCredentials: UsernamePasswordCredentials
        The credentials to use when you authenticate with the SOAP endpoint.

    digitalSignature: bool
        If incoming or outgoing messages must be signed.

    sslAuthKeyPairRef: ResourceLink
        The ID of the key pair used to authenticate with your partner's SOAP endpoint. The ID of the key pair is also known as the alias and can be found by viewing the corresponding certificate under 'SSL Server Certificates' in the PingFederate Administrative Console.

    validatePartnerCert: bool
        Validate the partner server certificate. Default is true.

    """

    def __init__(self, type: BackChannelAuthType, httpBasicCredentials: UsernamePasswordCredentials = None, digitalSignature: bool = None, sslAuthKeyPairRef: ResourceLink = None, validatePartnerCert: bool = None) -> None:
        self.type = type
        self.httpBasicCredentials = httpBasicCredentials
        self.digitalSignature = digitalSignature
        self.sslAuthKeyPairRef = sslAuthKeyPairRef
        self.validatePartnerCert = validatePartnerCert

    def _validate(self) -> bool:
        return any(x for x in ["type"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OutboundBackChannelAuth):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.httpBasicCredentials, self.digitalSignature, self.sslAuthKeyPairRef, self.validatePartnerCert]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "httpBasicCredentials", "digitalSignature", "sslAuthKeyPairRef", "validatePartnerCert"] and v is not None:
                if k == "type":
                    valid_data[k] = BackChannelAuthType[v]
                if k == "httpBasicCredentials":
                    valid_data[k] = UsernamePasswordCredentials(**v)
                if k == "digitalSignature":
                    valid_data[k] = bool(v)
                if k == "sslAuthKeyPairRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "validatePartnerCert":
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
            if k in ["type", "httpBasicCredentials", "digitalSignature", "sslAuthKeyPairRef", "validatePartnerCert"]:
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
