class KeyAlgorithm():
    """ Details for a key algorithm.

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

    __slots__ = ["defaultKeySize", "defaultSignatureAlgorithm", "keySizes", "name", "signatureAlgorithms"]
    def __init__(self, defaultKeySize=None, defaultSignatureAlgorithm=None, keySizes=None, name=None, signatureAlgorithms=None):
            self.defaultKeySize = defaultKeySize
            self.defaultSignatureAlgorithm = defaultSignatureAlgorithm
            self.keySizes = keySizes
            self.name = name
            self.signatureAlgorithms = signatureAlgorithms
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, KeyAlgorithm):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((defaultKeySize, defaultSignatureAlgorithm, keySizes, name, signatureAlgorithms))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
