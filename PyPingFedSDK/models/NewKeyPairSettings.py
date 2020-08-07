class NewKeyPairSettings():
    """Settings for creating a new key pair.

    Attributes
    ----------
    city : string
        City.    commonName : string
        Common name for key pair subject.    country : string
        Country.    cryptoProvider : str
        Cryptographic Provider.  This is only applicable if Hybrid HSM mode is true.    id : string
        The persistent, unique ID for the certificate. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified.    keyAlgorithm : string
        Key generation algorithm. Supported algorithms are available through the /keyPairs/keyAlgorithms endpoint.    keySize : integer
        Key size, in bits. If this property is unset, the default size for the key algorithm will be used. Supported key sizes are available through the /keyPairs/keyAlgorithms endpoint.    organization : string
        Organization.    organizationUnit : string
        Organization unit.    signatureAlgorithm : string
        Signature algorithm. If this property is unset, the default signature algorithm for the key algorithm will be used. Supported signature algorithms are available through the /keyPairs/keyAlgorithms endpoint.    state : string
        State.    subjectAlternativeNames : array
        The subject alternative names (SAN).    validDays : integer
        Number of days the key pair will be valid for.
    """

    __slots__ = ["city", "commonName", "country", "cryptoProvider", "id", "keyAlgorithm", "keySize", "organization", "organizationUnit", "signatureAlgorithm", "state", "subjectAlternativeNames", "validDays"]

    def __init__(self, commonName, organization, country, validDays, keyAlgorithm, city=None, cryptoProvider=None, id=None, keySize=None, organizationUnit=None, signatureAlgorithm=None, state=None, subjectAlternativeNames=None):
        self.city: str = city
        self.commonName: str = commonName
        self.country: str = country
        self.cryptoProvider: str = cryptoProvider
        self.id: str = id
        self.keyAlgorithm: str = keyAlgorithm
        self.keySize: str = keySize
        self.organization: str = organization
        self.organizationUnit: str = organizationUnit
        self.signatureAlgorithm: str = signatureAlgorithm
        self.state: str = state
        self.subjectAlternativeNames: list = subjectAlternativeNames
        self.validDays: str = validDays

    def _validate(self):
        return any(x for x in ['commonName', 'organization', 'country', 'validDays', 'keyAlgorithm'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, NewKeyPairSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.city, self.commonName, self.country, self.cryptoProvider, self.id, self.keyAlgorithm, self.keySize, self.organization, self.organizationUnit, self.signatureAlgorithm, self.state, self.subjectAlternativeNames, self.validDays))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["city", "commonName", "country", "cryptoProvider", "id", "keyAlgorithm", "keySize", "organization", "organizationUnit", "signatureAlgorithm", "state", "subjectAlternativeNames", "validDays"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__