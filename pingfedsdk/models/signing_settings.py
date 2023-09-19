from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.resource_link import ResourceLink


class SigningSettings(Model):
    """Settings related to signing messages sent to this partner.

    Attributes
    ----------
    signingKeyPairRef: ResourceLink
        The ID of the key pair used to sign messages sent to this partner. The ID of the key pair is also known as the alias and can be found by viewing the corresponding certificate under 'Signing & Decryption Keys & Certificates' in the PingFederate admin console.

    alternativeSigningKeyPairRefs: list
        The list of IDs of alternative key pairs used to sign messages sent to this partner. The ID of the key pair is also known as the alias and can be found by viewing the corresponding certificate under 'Signing & Decryption Keys & Certificates' in the PingFederate admin console.

    algorithm: str
        The algorithm used to sign messages sent to this partner. The default is SHA1withDSA for DSA certs, SHA256withRSA for RSA certs, and SHA256withECDSA for EC certs. For RSA certs, SHA1withRSA, SHA384withRSA, and SHA512withRSA are also supported. For EC certs, SHA384withECDSA and SHA512withECDSA are also supported. If the connection is WS-Federation with JWT token type, then the possible values are RSA SHA256, RSA SHA384, RSA SHA512, ECDSA SHA256, ECDSA SHA384, ECDSA SHA512

    includeCertInSignature: bool
        Determines whether the signing certificate is included in the signature <KeyInfo> element.

    includeRawKeyInSignature: bool
        Determines whether the <KeyValue> element with the raw public key is included in the signature <KeyInfo> element.

    """
    def __init__(self, signingKeyPairRef: ResourceLink, alternativeSigningKeyPairRefs: list = None, algorithm: str = None, includeCertInSignature: bool = None, includeRawKeyInSignature: bool = None) -> None:
        self.signingKeyPairRef = signingKeyPairRef
        self.alternativeSigningKeyPairRefs = alternativeSigningKeyPairRefs
        self.algorithm = algorithm
        self.includeCertInSignature = includeCertInSignature
        self.includeRawKeyInSignature = includeRawKeyInSignature

    def _validate(self) -> bool:
        return any(x for x in ["signingKeyPairRef"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SigningSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.signingKeyPairRef, self.alternativeSigningKeyPairRefs, self.algorithm, self.includeCertInSignature, self.includeRawKeyInSignature]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["signingKeyPairRef", "alternativeSigningKeyPairRefs", "algorithm", "includeCertInSignature", "includeRawKeyInSignature"] and v is not None:
                if k == "signingKeyPairRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "alternativeSigningKeyPairRefs":
                    valid_data[k] = [ResourceLink.from_dict(x) for x in v]
                if k == "algorithm":
                    valid_data[k] = str(v)
                if k == "includeCertInSignature":
                    valid_data[k] = bool(v)
                if k == "includeRawKeyInSignature":
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
            if k in ["signingKeyPairRef", "alternativeSigningKeyPairRefs", "algorithm", "includeCertInSignature", "includeRawKeyInSignature"]:
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
