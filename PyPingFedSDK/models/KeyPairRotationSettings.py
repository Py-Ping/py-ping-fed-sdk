class KeyPairRotationSettings():
    """Key Pair Rotation Details

    Attributes
    ----------
    activationBufferDays : integer
 Buffer days before key pair expiration for activation of the new key pair.
    creationBufferDays : integer
 Buffer days before key pair expiration for creation of a new key pair.
    id : string
    keyAlgorithm : string
 Key algorithm to be used while creating a new key pair. If this property is unset, the key algorithm of the original key pair will be used. Supported algorithms are available through the /keyPairs/keyAlgorithms endpoint.
    keySize : integer
 Key size, in bits. If this property is unset, the key size of the original key pair will be used. Supported key sizes are available through the /keyPairs/keyAlgorithms endpoint.
    signatureAlgorithm : string
 Required if the original key pair used SHA1 algorithm. If this property is unset, the default signature algorithm of the original key pair will be used. Supported signature algorithms are available through the /keyPairs/keyAlgorithms endpoint.
    validDays : integer
 Valid days for the new key pair to be created. If this property is unset, the validity days of the original key pair will be used.

    """

<<<<<<< HEAD
    def __init__(self, creationBufferDays, activationBufferDays, var_id=None, keyAlgorithm=None, keySize=None, signatureAlgorithm=None, validDays=None) -> None:
        self.activationBufferDays = activationBufferDays
        self.creationBufferDays = creationBufferDays
        self.var_id = var_id
        self.keyAlgorithm = keyAlgorithm
        self.keySize = keySize
        self.signatureAlgorithm = signatureAlgorithm
        self.validDays = validDays
=======
    def __init__(self, creationBufferDays, activationBufferDays, id=None, keyAlgorithm=None, keySize=None, signatureAlgorithm=None, validDays=None):
        self.activationBufferDays: str = activationBufferDays
        self.creationBufferDays: str = creationBufferDays
        self.id: str = id
        self.keyAlgorithm: str = keyAlgorithm
        self.keySize: str = keySize
        self.signatureAlgorithm: str = signatureAlgorithm
        self.validDays: str = validDays
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["creationBufferDays", "activationBufferDays"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, KeyPairRotationSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.activationBufferDays, self.creationBufferDays, self.var_id, self.keyAlgorithm, self.keySize, self.signatureAlgorithm, self.validDays))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["activationBufferDays", "creationBufferDays", "var_id", "keyAlgorithm", "keySize", "signatureAlgorithm", "validDays"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
