class X509File():
    """ Encoded certificate data.

    Attributes
    ----------
    cryptoProvider : str
        Cryptographic Provider. This is only applicable if Hybrid HSM mode is true.
    fileData : string
        The certificate data in PEM format. New line characters should be omitted or encoded in this value.
    id : string
        The persistent, unique ID for the certificate. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified.

    """

    __slots__ = ["cryptoProvider", "fileData", "id"]
    def __init__(self, fileData, cryptoProvider=None, id=None):
            self.cryptoProvider = cryptoProvider
            self.fileData = fileData
            self.id = id
    
    def _validate(self):
        return any(x for x in ['fileData'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, X509File):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((cryptoProvider, fileData, id))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
