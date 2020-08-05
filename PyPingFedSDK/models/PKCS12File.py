class PKCS12File():
    """Represents the contents of a PKCS12 file.

    Attributes
    ----------
    cryptoProvider : str
        Cryptographic Provider. This is only applicable if Hybrid HSM mode is true.    encryptedPassword : string
        Encrypted password for the PKCS12 file.    fileData : string
        Base64 encoded PKCS12 file data. New line characters should be omitted or encoded in this value.    id : string
        The persistent, unique ID for the certificate. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified.    password : string
        Password for the PKCS12 file.
    """

    __slots__ = ["cryptoProvider", "encryptedPassword", "fileData", "id", "password"]

    def __init__(self, fileData, password, encryptedPassword, cryptoProvider=None, id=None):
        self.cryptoProvider = cryptoProvider
        self.encryptedPassword = encryptedPassword
        self.fileData = fileData
        self.id = id
        self.password = password

    def _validate(self):
        return any(x for x in ['fileData', 'password', 'encryptedPassword'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, PKCS12File):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.cryptoProvider, self.encryptedPassword, self.fileData, self.id, self.password))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["cryptoProvider", "encryptedPassword", "fileData", "id", "password"]}

        return cls(**valid_data)
