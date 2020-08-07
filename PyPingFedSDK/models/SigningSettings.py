class SigningSettings():
    """Settings related to signing messages sent to this partner.

    Attributes
    ----------
    algorithm : string
        The algorithm used to sign messages sent to this partner. The default is SHA1withDSA for DSA certs, SHA256withRSA for RSA certs, and SHA256withECDSA for EC certs. For RSA certs, SHA1withRSA, SHA384withRSA, and SHA512withRSA are also supported. For EC certs, SHA384withECDSA and SHA512withECDSA are also supported. If the connection is WS-Federation with JWT token type, then the possible values are RSA SHA256, RSA SHA384, RSA SHA512, ECDSA SHA256, ECDSA SHA384, ECDSA SHA512    includeCertInSignature : boolean
        Determines whether the signing certificate is included in the signature <KeyInfo> element.    includeRawKeyInSignature : boolean
        Determines whether the <KeyValue> element with the raw public key is included in the signature <KeyInfo> element.    signingKeyPairRef : str
        The ID of the key pair used to sign messages sent to this partner. The ID of the key pair is also known as the alias and can be found by viewing the corresponding certificate under 'Signing & Decryption Keys & Certificates' in the PingFederate admin console.
    """

    __slots__ = ["algorithm", "includeCertInSignature", "includeRawKeyInSignature", "signingKeyPairRef"]

    def __init__(self, signingKeyPairRef, algorithm=None, includeCertInSignature=None, includeRawKeyInSignature=None):
        self.algorithm: str = algorithm
        self.includeCertInSignature: bool = includeCertInSignature
        self.includeRawKeyInSignature: bool = includeRawKeyInSignature
        self.signingKeyPairRef: str = signingKeyPairRef

    def _validate(self):
        return any(x for x in ['signingKeyPairRef'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, SigningSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.algorithm, self.includeCertInSignature, self.includeRawKeyInSignature, self.signingKeyPairRef))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["algorithm", "includeCertInSignature", "includeRawKeyInSignature", "signingKeyPairRef"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__