class MetadataSigningSettings():
    """Metadata signing settings. If metadata is not signed, this model will be empty.

    Attributes
    ----------
    signatureAlgorithm : string
        Signature algorithm. If this property is unset, the default signature algorithm for the key algorithm will be used. Supported signature algorithms are available through the /keyPairs/keyAlgorithms endpoint.    signingKeyRef : str
        Reference to the key used for metadata signing. Refer to /keyPair/signing to get the list of available signing key pairs.
    """

    __slots__ = ["signatureAlgorithm", "signingKeyRef"]

    def __init__(self, signatureAlgorithm=None, signingKeyRef=None):
        self.signatureAlgorithm = signatureAlgorithm
        self.signingKeyRef = signingKeyRef

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, MetadataSigningSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.signatureAlgorithm, self.signingKeyRef))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["signatureAlgorithm", "signingKeyRef"]}

        return cls(**valid_data)