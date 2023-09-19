from enum import Enum

from pingfedsdk.model import Model


class KeyPairRotationSettings(Model):
    """Key Pair Rotation Details

    Attributes
    ----------
    id: str
    creationBufferDays: int
        Buffer days before key pair expiration for creation of a new key pair.

    activationBufferDays: int
        Buffer days before key pair expiration for activation of the new key pair.

    validDays: int
        Valid days for the new key pair to be created. If this property is unset, the validity days of the original key pair will be used.

    keyAlgorithm: str
        Key algorithm to be used while creating a new key pair. If this property is unset, the key algorithm of the original key pair will be used. Supported algorithms are available through the /keyPairs/keyAlgorithms endpoint.

    keySize: int
        Key size, in bits. If this property is unset, the key size of the original key pair will be used. Supported key sizes are available through the /keyPairs/keyAlgorithms endpoint.

    signatureAlgorithm: str
        Required if the original key pair used SHA1 algorithm. If this property is unset, the default signature algorithm of the original key pair will be used. Supported signature algorithms are available through the /keyPairs/keyAlgorithms endpoint.

    """
    def __init__(self, creationBufferDays: int, activationBufferDays: int, validDays: int = None, keyAlgorithm: str = None, keySize: int = None, signatureAlgorithm: str = None, id: str = None) -> None:
        self.id = id
        self.creationBufferDays = creationBufferDays
        self.activationBufferDays = activationBufferDays
        self.validDays = validDays
        self.keyAlgorithm = keyAlgorithm
        self.keySize = keySize
        self.signatureAlgorithm = signatureAlgorithm

    def _validate(self) -> bool:
        return any(x for x in ["activationBufferDays", "creationBufferDays"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, KeyPairRotationSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.creationBufferDays, self.activationBufferDays, self.validDays, self.keyAlgorithm, self.keySize, self.signatureAlgorithm]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "creationBufferDays", "activationBufferDays", "validDays", "keyAlgorithm", "keySize", "signatureAlgorithm"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "creationBufferDays":
                    valid_data[k] = int(v)
                if k == "activationBufferDays":
                    valid_data[k] = int(v)
                if k == "validDays":
                    valid_data[k] = int(v)
                if k == "keyAlgorithm":
                    valid_data[k] = str(v)
                if k == "keySize":
                    valid_data[k] = int(v)
                if k == "signatureAlgorithm":
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
            if k in ["id", "creationBufferDays", "activationBufferDays", "validDays", "keyAlgorithm", "keySize", "signatureAlgorithm"]:
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
