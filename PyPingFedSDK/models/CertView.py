class CertView():
    """Certificate details.

    Attributes
    ----------
    cryptoProvider : str
        Cryptographic Provider. This is only applicable if Hybrid HSM mode is true.    expires : string
        The end date up until which the item is valid, in ISO 8601 format (UTC).    id : string
        The persistent, unique ID for the certificate.    issuerDN : string
        The issuer's distinguished name.    keyAlgorithm : string
        The public key algorithm.    keySize : integer
        The public key size.    serialNumber : string
        The serial number assigned by the CA.    sha1Fingerprint : string
        SHA-1 fingerprint in Hex encoding.    sha256Fingerprint : string
        SHA-256 fingerprint in Hex encoding.    signatureAlgorithm : string
        The signature algorithm.    status : str
        Status of the item.    subjectAlternativeNames : array
        The subject alternative names (SAN).    subjectDN : string
        The subject's distinguished name.    validFrom : string
        The start date from which the item is valid, in ISO 8601 format (UTC).    version : integer
        The X.509 version to which the item conforms.
    """

    __slots__ = ["cryptoProvider", "expires", "id", "issuerDN", "keyAlgorithm", "keySize", "serialNumber", "sha1Fingerprint", "sha256Fingerprint", "signatureAlgorithm", "status", "subjectAlternativeNames", "subjectDN", "validFrom", "version"]

    def __init__(self, cryptoProvider=None, expires=None, id=None, issuerDN=None, keyAlgorithm=None, keySize=None, serialNumber=None, sha1Fingerprint=None, sha256Fingerprint=None, signatureAlgorithm=None, status=None, subjectAlternativeNames=None, subjectDN=None, validFrom=None, version=None):
        self.cryptoProvider: str = cryptoProvider
        self.expires: str = expires
        self.id: str = id
        self.issuerDN: str = issuerDN
        self.keyAlgorithm: str = keyAlgorithm
        self.keySize: str = keySize
        self.serialNumber: str = serialNumber
        self.sha1Fingerprint: str = sha1Fingerprint
        self.sha256Fingerprint: str = sha256Fingerprint
        self.signatureAlgorithm: str = signatureAlgorithm
        self.status: str = status
        self.subjectAlternativeNames: list = subjectAlternativeNames
        self.subjectDN: str = subjectDN
        self.validFrom: str = validFrom
        self.version: str = version

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, CertView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.cryptoProvider, self.expires, self.id, self.issuerDN, self.keyAlgorithm, self.keySize, self.serialNumber, self.sha1Fingerprint, self.sha256Fingerprint, self.signatureAlgorithm, self.status, self.subjectAlternativeNames, self.subjectDN, self.validFrom, self.version))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["cryptoProvider", "expires", "id", "issuerDN", "keyAlgorithm", "keySize", "serialNumber", "sha1Fingerprint", "sha256Fingerprint", "signatureAlgorithm", "status", "subjectAlternativeNames", "subjectDN", "validFrom", "version"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__