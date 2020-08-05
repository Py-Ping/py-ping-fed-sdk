class NewKeyPairSettings():
    """ Settings for creating a new key pair.

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

    __slots__ = ["city", "commonName", "country", "cryptoProvider", "id", "keyAlgorithm", "keySize", "organization", "organizationUnit", "signatureAlgorithm", "state", "subjectAlternativeNames", "validDays"]
    def __init__(self, commonName, organization, country, validDays, keyAlgorithm, city=None, cryptoProvider=None, id=None, keySize=None, organizationUnit=None, signatureAlgorithm=None, state=None, subjectAlternativeNames=None):
            self.city = city
            self.commonName = commonName
            self.country = country
            self.cryptoProvider = cryptoProvider
            self.id = id
            self.keyAlgorithm = keyAlgorithm
            self.keySize = keySize
            self.organization = organization
            self.organizationUnit = organizationUnit
            self.signatureAlgorithm = signatureAlgorithm
            self.state = state
            self.subjectAlternativeNames = subjectAlternativeNames
            self.validDays = validDays
    
    def _validate(self):
        return any(x for x in ['commonName', 'organization', 'country', 'validDays', 'keyAlgorithm'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, NewKeyPairSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((city, commonName, country, cryptoProvider, id, keyAlgorithm, keySize, organization, organizationUnit, signatureAlgorithm, state, subjectAlternativeNames, validDays))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
