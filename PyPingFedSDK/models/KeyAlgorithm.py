class KeyAlgorithm():
    """Details for a key algorithm.

    Attributes
    ----------
    defaultKeySize : integer
 Default key size for this algorithm.
    defaultSignatureAlgorithm : string
 Default signature algorithm for this key algorithm.
    keySizes : array
 Possible key sizes for this algorithm, in bits.
    name : string
 Name of the key algorithm.
    signatureAlgorithms : array
 Possible signature algorithms for this key algorithm.

    """

    def __init__(self, defaultKeySize:int=None, defaultSignatureAlgorithm:str=None, keySizes:list=None, name:str=None, signatureAlgorithms:list=None) -> None:
        self.defaultKeySize = defaultKeySize
        self.defaultSignatureAlgorithm = defaultSignatureAlgorithm
        self.keySizes = keySizes
        self.name = name
        self.signatureAlgorithms = signatureAlgorithms

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, KeyAlgorithm):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.defaultKeySize, self.defaultSignatureAlgorithm, self.keySizes, self.name, self.signatureAlgorithms))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["defaultKeySize", "defaultSignatureAlgorithm", "keySizes", "name", "signatureAlgorithms"]}

        return cls(**valid_data)