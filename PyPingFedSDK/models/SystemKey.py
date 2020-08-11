class SystemKey():
    """A system key.

    Attributes
    ----------
    creationDate : string
        Creation time of the key.
    encryptedKeyData : string
        The system key encrypted.
    keyData : string
        The clear text system key base 64 encoded. The system key must be 32 bytes before base 64 encoding.

    """

    def __init__(self, creationDate:str=None, encryptedKeyData:str=None, keyData:str=None) -> None:
        self.creationDate = creationDate
        self.encryptedKeyData = encryptedKeyData
        self.keyData = keyData

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SystemKey):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.creationDate, self.encryptedKeyData, self.keyData]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["creationDate", "encryptedKeyData", "keyData"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__