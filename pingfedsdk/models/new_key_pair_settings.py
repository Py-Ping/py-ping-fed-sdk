from enum import Enum

from pingfedsdk.enums import CryptoProvider
from pingfedsdk.model import Model


class NewKeyPairSettings(Model):
    """Settings for creating a new key pair.

    Attributes
    ----------
    id: str
        The persistent, unique ID for the certificate. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified.

    commonName: str
        Common name for key pair subject.

    subjectAlternativeNames: list
        The subject alternative names (SAN).

    organization: str
        Organization.

    organizationUnit: str
        Organization unit.

    city: str
        City.

    state: str
        State.

    country: str
        Country.

    validDays: int
        Number of days the key pair will be valid for.

    keyAlgorithm: str
        Key generation algorithm. Supported algorithms are available through the /keyPairs/keyAlgorithms endpoint.

    keySize: int
        Key size, in bits. If this property is unset, the default size for the key algorithm will be used. Supported key sizes are available through the /keyPairs/keyAlgorithms endpoint.

    signatureAlgorithm: str
        Signature algorithm. If this property is unset, the default signature algorithm for the key algorithm will be used. Supported signature algorithms are available through the /keyPairs/keyAlgorithms endpoint.

    cryptoProvider: CryptoProvider
        Cryptographic Provider.  This is only applicable if Hybrid HSM mode is true.

    """
    def __init__(self, commonName: str, organization: str, country: str, validDays: int, keyAlgorithm: str, id: str = None, subjectAlternativeNames: list = None, organizationUnit: str = None, city: str = None, state: str = None, keySize: int = None, signatureAlgorithm: str = None, cryptoProvider: CryptoProvider = None) -> None:
        self.id = id
        self.commonName = commonName
        self.subjectAlternativeNames = subjectAlternativeNames
        self.organization = organization
        self.organizationUnit = organizationUnit
        self.city = city
        self.state = state
        self.country = country
        self.validDays = validDays
        self.keyAlgorithm = keyAlgorithm
        self.keySize = keySize
        self.signatureAlgorithm = signatureAlgorithm
        self.cryptoProvider = cryptoProvider

    def _validate(self) -> bool:
        return any(x for x in ["commonName", "country", "keyAlgorithm", "organization", "validDays"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, NewKeyPairSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.commonName, self.subjectAlternativeNames, self.organization, self.organizationUnit, self.city, self.state, self.country, self.validDays, self.keyAlgorithm, self.keySize, self.signatureAlgorithm, self.cryptoProvider]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "commonName", "subjectAlternativeNames", "organization", "organizationUnit", "city", "state", "country", "validDays", "keyAlgorithm", "keySize", "signatureAlgorithm", "cryptoProvider"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "commonName":
                    valid_data[k] = str(v)
                if k == "subjectAlternativeNames":
                    valid_data[k] = [str(x) for x in v]
                if k == "organization":
                    valid_data[k] = str(v)
                if k == "organizationUnit":
                    valid_data[k] = str(v)
                if k == "city":
                    valid_data[k] = str(v)
                if k == "state":
                    valid_data[k] = str(v)
                if k == "country":
                    valid_data[k] = str(v)
                if k == "validDays":
                    valid_data[k] = int(v)
                if k == "keyAlgorithm":
                    valid_data[k] = str(v)
                if k == "keySize":
                    valid_data[k] = int(v)
                if k == "signatureAlgorithm":
                    valid_data[k] = str(v)
                if k == "cryptoProvider":
                    valid_data[k] = CryptoProvider[v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "commonName", "subjectAlternativeNames", "organization", "organizationUnit", "city", "state", "country", "validDays", "keyAlgorithm", "keySize", "signatureAlgorithm", "cryptoProvider"]:
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
