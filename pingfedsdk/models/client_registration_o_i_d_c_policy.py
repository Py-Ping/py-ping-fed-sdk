from enum import Enum

from pingfedsdk.enums import ContentEncryptionAlgorithm
from pingfedsdk.enums import EncryptionAlgorithm
from pingfedsdk.enums import SigningAlgorithm
from pingfedsdk.model import Model
from pingfedsdk.models.resource_link import ResourceLink


class ClientRegistrationOIDCPolicy(Model):
    """Client Registration Open ID Connect Policy settings.

    Attributes
    ----------
    idTokenSigningAlgorithm: SigningAlgorithm
        The JSON Web Signature [JWS] algorithm required for the ID Token.
        NONE - No signing algorithm
        HS256 - HMAC using SHA-256
        HS384 - HMAC using SHA-384
        HS512 - HMAC using SHA-512
        RS256 - RSA using SHA-256
        RS384 - RSA using SHA-384
        RS512 - RSA using SHA-512
        ES256 - ECDSA using P256 Curve and SHA-256
        ES384 - ECDSA using P384 Curve and SHA-384
        ES512 - ECDSA using P521 Curve and SHA-512
        PS256 - RSASSA-PSS using SHA-256 and MGF1 padding with SHA-256
        PS384 - RSASSA-PSS using SHA-384 and MGF1 padding with SHA-384
        PS512 - RSASSA-PSS using SHA-512 and MGF1 padding with SHA-512
        A null value will represent the default algorithm which is RS256.
        RSASSA-PSS is only supported with SafeNet Luna, Thales nCipher or Java 11

    idTokenEncryptionAlgorithm: EncryptionAlgorithm
        The JSON Web Encryption [JWE] encryption algorithm used to encrypt the content encryption key for the ID Token.
        DIR - Direct Encryption with symmetric key
        A128KW - AES-128 Key Wrap
        A192KW - AES-192 Key Wrap
        A256KW - AES-256 Key Wrap
        A128GCMKW - AES-GCM-128 key encryption
        A192GCMKW - AES-GCM-192 key encryption
        A256GCMKW - AES-GCM-256 key encryption
        ECDH_ES - ECDH-ES
        ECDH_ES_A128KW - ECDH-ES with AES-128 Key Wrap
        ECDH_ES_A192KW - ECDH-ES with AES-192 Key Wrap
        ECDH_ES_A256KW - ECDH-ES with AES-256 Key Wrap
        RSA_OAEP - RSAES OAEP
        RSA_OAEP_256 - RSAES OAEP using SHA-256 and MGF1 with SHA-256

    idTokenContentEncryptionAlgorithm: ContentEncryptionAlgorithm
        The JSON Web Encryption [JWE] content encryption algorithm for the ID Token.
        AES_128_CBC_HMAC_SHA_256 - Composite AES-CBC-128 HMAC-SHA-256
        AES_192_CBC_HMAC_SHA_384 - Composite AES-CBC-192 HMAC-SHA-384
        AES_256_CBC_HMAC_SHA_512 - Composite AES-CBC-256 HMAC-SHA-512
        AES_128_GCM - AES-GCM-128
        AES_192_GCM - AES-GCM-192
        AES_256_GCM - AES-GCM-256

    policyGroup: ResourceLink
        The Open ID Connect policy. A null value will represent the default policy group.

    """
    def __init__(self, idTokenSigningAlgorithm: SigningAlgorithm = None, idTokenEncryptionAlgorithm: EncryptionAlgorithm = None, idTokenContentEncryptionAlgorithm: ContentEncryptionAlgorithm = None, policyGroup: ResourceLink = None) -> None:
        self.idTokenSigningAlgorithm = idTokenSigningAlgorithm
        self.idTokenEncryptionAlgorithm = idTokenEncryptionAlgorithm
        self.idTokenContentEncryptionAlgorithm = idTokenContentEncryptionAlgorithm
        self.policyGroup = policyGroup

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ClientRegistrationOIDCPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.idTokenSigningAlgorithm, self.idTokenEncryptionAlgorithm, self.idTokenContentEncryptionAlgorithm, self.policyGroup]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["idTokenSigningAlgorithm", "idTokenEncryptionAlgorithm", "idTokenContentEncryptionAlgorithm", "policyGroup"] and v is not None:
                if k == "idTokenSigningAlgorithm":
                    valid_data[k] = SigningAlgorithm[v]
                if k == "idTokenEncryptionAlgorithm":
                    valid_data[k] = EncryptionAlgorithm[v]
                if k == "idTokenContentEncryptionAlgorithm":
                    valid_data[k] = ContentEncryptionAlgorithm[v]
                if k == "policyGroup":
                    valid_data[k] = ResourceLink.from_dict(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["idTokenSigningAlgorithm", "idTokenEncryptionAlgorithm", "idTokenContentEncryptionAlgorithm", "policyGroup"]:
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
