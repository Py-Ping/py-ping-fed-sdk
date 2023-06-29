from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.enums import CryptoProvider
from pingfedsdk.enums import Format


class KeyPairFile(Model):
    """Represents the contents of a PKCS12 or PEM file.

    Attributes
    ----------
    id: str
        The persistent, unique ID for the certificate. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified.

    fileData: str
        Base-64 encoded PKCS12 or PEM file data. In the case of PEM, the raw (non-base-64) data is also accepted. In BCFIPS mode, only PEM with PBES2 and AES or Triple DES encryption is accepted and 128-bit salt is required.

    format: Format
        Key pair file format. If specified, this field will control what file format is expected, otherwise the format will be auto-detected. In BCFIPS mode, only PEM is supported.

    password: str
        Password for the file. In BCFIPS mode, the password must be at least 14 characters.

    encryptedPassword: str
        Encrypted password for the file. Only applicable for bulk export/import operations. For bulk import operation, either password or encrypted password must be set.

    cryptoProvider: CryptoProvider
        Cryptographic Provider. This is only applicable if Hybrid HSM mode is true.

    """

    def __init__(self, fileData: str, password: str, id: str = None, format: Format = None, encryptedPassword: str = None, cryptoProvider: CryptoProvider = None) -> None:
        self.id = id
        self.fileData = fileData
        self.format = format
        self.password = password
        self.encryptedPassword = encryptedPassword
        self.cryptoProvider = cryptoProvider

    def _validate(self) -> bool:
        return any(x for x in ["fileData", "password"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, KeyPairFile):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.fileData, self.format, self.password, self.encryptedPassword, self.cryptoProvider]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "fileData", "format", "password", "encryptedPassword", "cryptoProvider"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "fileData":
                    valid_data[k] = str(v)
                if k == "format":
                    valid_data[k] = Format[v]
                if k == "password":
                    valid_data[k] = str(v)
                if k == "encryptedPassword":
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
            if k in ["id", "fileData", "format", "password", "encryptedPassword", "cryptoProvider"]:
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
