class DecryptionKeys():
    """Decryption keys used to decrypt message content received from the partner.

    Attributes
    ----------
    primaryKeyRef : str
 The ID of the primary decryption key pair. It is also known as the alias and can be found by viewing the corresponding certificate under 'Signing & Decryption Keys & Certificates' in the PingFederate Administrative Console.
    secondaryKeyPairRef : str
 The ID of the secondary key pair used to decrypt message content received from the partner.

    """

    def __init__(self, primaryKeyRef=None, secondaryKeyPairRef=None) -> None:
        self.primaryKeyRef = primaryKeyRef
        self.secondaryKeyPairRef = secondaryKeyPairRef

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, DecryptionKeys):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.primaryKeyRef, self.secondaryKeyPairRef))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["primaryKeyRef", "secondaryKeyPairRef"]}

        return cls(**valid_data)