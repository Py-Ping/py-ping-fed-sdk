class NewKeyPairSettings():
    """Settings for creating a new key pair.

    Attributes
    ----------
    city : string
        City.
    commonName : string
        Common name for key pair subject.
    country : string
        Country.
    cryptoProvider : str
        Cryptographic Provider.  This is only applicable if Hybrid HSM mode is true.
    id : string
        The persistent, unique ID for the certificate. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified.
    keyAlgorithm : string
        Key generation algorithm. Supported algorithms are available through the /keyPairs/keyAlgorithms endpoint.
    keySize : integer
        Key size, in bits. If this property is unset, the default size for the key algorithm will be used. Supported key sizes are available through the /keyPairs/keyAlgorithms endpoint.
    organization : string
        Organization.
    organizationUnit : string
        Organization unit.
    signatureAlgorithm : string
        Signature algorithm. If this property is unset, the default signature algorithm for the key algorithm will be used. Supported signature algorithms are available through the /keyPairs/keyAlgorithms endpoint.
    state : string
        State.
    subjectAlternativeNames : array
        The subject alternative names (SAN).
    validDays : integer
        Number of days the key pair will be valid for.

    """

    def __init__(self, commonName:str, organization:str, country:str, validDays:int, keyAlgorithm:str, city:str=None, cryptoProvider=None, var_id:str=None, keySize:int=None, organizationUnit:str=None, signatureAlgorithm:str=None, state:str=None, subjectAlternativeNames:list=None) -> None:
        self.city = city
        self.commonName = commonName
        self.country = country
        self.cryptoProvider = cryptoProvider
        self.var_id = var_id
        self.keyAlgorithm = keyAlgorithm
        self.keySize = keySize
        self.organization = organization
        self.organizationUnit = organizationUnit
        self.signatureAlgorithm = signatureAlgorithm
        self.state = state
        self.subjectAlternativeNames = subjectAlternativeNames
        self.validDays = validDays

    def _validate(self) -> bool:
        return any(x for x in ["commonName", "organization", "country", "validDays", "keyAlgorithm"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, NewKeyPairSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.city, self.commonName, self.country, self.cryptoProvider, self.var_id, self.keyAlgorithm, self.keySize, self.organization, self.organizationUnit, self.signatureAlgorithm, self.state, self.subjectAlternativeNames, self.validDays]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["city", "commonName", "country", "cryptoProvider", "var_id", "keyAlgorithm", "keySize", "organization", "organizationUnit", "signatureAlgorithm", "state", "subjectAlternativeNames", "validDays"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__