class X509File():
    """Encoded certificate data.

    Attributes
    ----------
    cryptoProvider : str
        Cryptographic Provider. This is only applicable if Hybrid HSM mode is true.
    fileData : string
        The certificate data in PEM format. New line characters should be omitted or encoded in this value.
    id : string
        The persistent, unique ID for the certificate. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified.

    """

    def __init__(self, fileData:str, cryptoProvider=None, var_id:str=None) -> None:
        self.cryptoProvider = cryptoProvider
        self.fileData = fileData
        self.var_id = var_id

    def _validate(self) -> bool:
        return any(x for x in ["fileData"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, X509File):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.cryptoProvider, self.fileData, self.var_id))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["cryptoProvider", "fileData", "var_id"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__