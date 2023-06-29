from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.key_pair_rotation_settings import KeyPairRotationSettings
from pingfedsdk.enums import CryptoProvider
from pingfedsdk.enums import Status


class KeyPairView(Model):
    """Key pair details.

    Attributes
    ----------
    id: str
        The persistent, unique ID for the certificate.

    serialNumber: str
        The serial number assigned by the CA.

    subjectDN: str
        The subject's distinguished name.

    subjectAlternativeNames: list
        The subject alternative names (SAN).

    issuerDN: str
        The issuer's distinguished name.

    validFrom: str
        The start date from which the item is valid, in ISO 8601 format (UTC).

    expires: str
        The end date up until which the item is valid, in ISO 8601 format (UTC).

    keyAlgorithm: str
        The public key algorithm.

    keySize: int
        The public key size.

    signatureAlgorithm: str
        The signature algorithm.

    version: int
        The X.509 version to which the item conforms.

    sha1Fingerprint: str
        SHA-1 fingerprint in Hex encoding.

    sha256Fingerprint: str
        SHA-256 fingerprint in Hex encoding.

    status: Status
        Status of the item.

    cryptoProvider: CryptoProvider
        Cryptographic Provider. This is only applicable if Hybrid HSM mode is true.

    rotationSettings: KeyPairRotationSettings
        Key pair rotation settings. Only applicable to self-signed signing key pairs. Automatic key rotation is not currently available for SSL client or SSL server key pairs.

    """

    def __init__(self, id: str = None, serialNumber: str = None, subjectDN: str = None, subjectAlternativeNames: list = None, issuerDN: str = None, validFrom: str = None, expires: str = None, keyAlgorithm: str = None, keySize: int = None, signatureAlgorithm: str = None, version: int = None, sha1Fingerprint: str = None, sha256Fingerprint: str = None, status: Status = None, cryptoProvider: CryptoProvider = None, rotationSettings: KeyPairRotationSettings = None) -> None:
        self.id = id
        self.serialNumber = serialNumber
        self.subjectDN = subjectDN
        self.subjectAlternativeNames = subjectAlternativeNames
        self.issuerDN = issuerDN
        self.validFrom = validFrom
        self.expires = expires
        self.keyAlgorithm = keyAlgorithm
        self.keySize = keySize
        self.signatureAlgorithm = signatureAlgorithm
        self.version = version
        self.sha1Fingerprint = sha1Fingerprint
        self.sha256Fingerprint = sha256Fingerprint
        self.status = status
        self.cryptoProvider = cryptoProvider
        self.rotationSettings = rotationSettings

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, KeyPairView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.serialNumber, self.subjectDN, self.subjectAlternativeNames, self.issuerDN, self.validFrom, self.expires, self.keyAlgorithm, self.keySize, self.signatureAlgorithm, self.version, self.sha1Fingerprint, self.sha256Fingerprint, self.status, self.cryptoProvider, self.rotationSettings]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "serialNumber", "subjectDN", "subjectAlternativeNames", "issuerDN", "validFrom", "expires", "keyAlgorithm", "keySize", "signatureAlgorithm", "version", "sha1Fingerprint", "sha256Fingerprint", "status", "cryptoProvider", "rotationSettings"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "serialNumber":
                    valid_data[k] = str(v)
                if k == "subjectDN":
                    valid_data[k] = str(v)
                if k == "subjectAlternativeNames":
                    valid_data[k] = [str(x) for x in v]
                if k == "issuerDN":
                    valid_data[k] = str(v)
                if k == "validFrom":
                    valid_data[k] = str(v)
                if k == "expires":
                    valid_data[k] = str(v)
                if k == "keyAlgorithm":
                    valid_data[k] = str(v)
                if k == "keySize":
                    valid_data[k] = int(v)
                if k == "signatureAlgorithm":
                    valid_data[k] = str(v)
                if k == "version":
                    valid_data[k] = int(v)
                if k == "sha1Fingerprint":
                    valid_data[k] = str(v)
                if k == "sha256Fingerprint":
                    valid_data[k] = str(v)
                if k == "status":
                    valid_data[k] = Status[v]
                if k == "cryptoProvider":
                    valid_data[k] = CryptoProvider[v]
                if k == "rotationSettings":
                    valid_data[k] = KeyPairRotationSettings(**v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "serialNumber", "subjectDN", "subjectAlternativeNames", "issuerDN", "validFrom", "expires", "keyAlgorithm", "keySize", "signatureAlgorithm", "version", "sha1Fingerprint", "sha256Fingerprint", "status", "cryptoProvider", "rotationSettings"]:
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
