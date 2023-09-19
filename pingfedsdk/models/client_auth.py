from enum import Enum

from pingfedsdk.enums import ClientAuthType
from pingfedsdk.enums import TokenEndpointAuthSigningAlgorithm
from pingfedsdk.model import Model
from pingfedsdk.models.secondary_secret import SecondarySecret


class ClientAuth(Model):
    """Client Authentication.

    Attributes
    ----------
    type: ClientAuthType
        Client authentication type.
        The required field for type SECRET is secret.
        The required fields for type CERTIFICATE are clientCertIssuerDn and clientCertSubjectDn.
        The required field for type PRIVATE_KEY_JWT is: either jwks or jwksUrl.

    secret: str
        Client secret for Basic Authentication.  To update the client secret, specify the plaintext value in this field.  This field will not be populated for GET requests.

    encryptedSecret: str
        For GET requests, this field contains the encrypted client secret, if one exists.  For POST and PUT requests, if you wish to reuse the existing secret, this field should be passed back unchanged.

    secondarySecrets: list
        The list of secondary client secrets that are temporarily retained.

    clientCertIssuerDn: str
        Client TLS Certificate Issuer DN.

    clientCertSubjectDn: str
        Client TLS Certificate Subject DN.

    enforceReplayPrevention: bool
        Enforce replay prevention on JSON Web Tokens. This field is applicable only for Private Key JWT Client Authentication.

    tokenEndpointAuthSigningAlgorithm: TokenEndpointAuthSigningAlgorithm
        The JSON Web Signature [JWS] algorithm that must be used to sign the JSON Web Tokens. This field is applicable only for Private Key JWT Client Authentication. All signing algorithms are allowed if value is not present
        RS256 - RSA using SHA-256
        RS384 - RSA using SHA-384
        RS512 - RSA using SHA-512
        ES256 - ECDSA using P256 Curve and SHA-256
        ES384 - ECDSA using P384 Curve and SHA-384
        ES512 - ECDSA using P521 Curve and SHA-512
        PS256 - RSASSA-PSS using SHA-256 and MGF1 padding with SHA-256
        PS384 - RSASSA-PSS using SHA-384 and MGF1 padding with SHA-384
        PS512 - RSASSA-PSS using SHA-512 and MGF1 padding with SHA-512
        RSASSA-PSS is only supported with SafeNet Luna, Thales nCipher or Java 11.

    """
    def __init__(self, type: ClientAuthType = None, secret: str = None, encryptedSecret: str = None, secondarySecrets: list = None, clientCertIssuerDn: str = None, clientCertSubjectDn: str = None, enforceReplayPrevention: bool = None, tokenEndpointAuthSigningAlgorithm: TokenEndpointAuthSigningAlgorithm = None) -> None:
        self.type = type
        self.secret = secret
        self.encryptedSecret = encryptedSecret
        self.secondarySecrets = secondarySecrets
        self.clientCertIssuerDn = clientCertIssuerDn
        self.clientCertSubjectDn = clientCertSubjectDn
        self.enforceReplayPrevention = enforceReplayPrevention
        self.tokenEndpointAuthSigningAlgorithm = tokenEndpointAuthSigningAlgorithm

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ClientAuth):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.secret, self.encryptedSecret, self.secondarySecrets, self.clientCertIssuerDn, self.clientCertSubjectDn, self.enforceReplayPrevention, self.tokenEndpointAuthSigningAlgorithm]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "secret", "encryptedSecret", "secondarySecrets", "clientCertIssuerDn", "clientCertSubjectDn", "enforceReplayPrevention", "tokenEndpointAuthSigningAlgorithm"] and v is not None:
                if k == "type":
                    valid_data[k] = ClientAuthType[v]
                if k == "secret":
                    valid_data[k] = str(v)
                if k == "encryptedSecret":
                    valid_data[k] = str(v)
                if k == "secondarySecrets":
                    valid_data[k] = [SecondarySecret.from_dict(x) for x in v]
                if k == "clientCertIssuerDn":
                    valid_data[k] = str(v)
                if k == "clientCertSubjectDn":
                    valid_data[k] = str(v)
                if k == "enforceReplayPrevention":
                    valid_data[k] = bool(v)
                if k == "tokenEndpointAuthSigningAlgorithm":
                    valid_data[k] = TokenEndpointAuthSigningAlgorithm[v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["type", "secret", "encryptedSecret", "secondarySecrets", "clientCertIssuerDn", "clientCertSubjectDn", "enforceReplayPrevention", "tokenEndpointAuthSigningAlgorithm"]:
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
