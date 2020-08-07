class ClientAuth():
    """Client Authentication.

    Attributes
    ----------
    clientCertIssuerDn : string
        Client TLS Certificate Issuer DN.    clientCertSubjectDn : string
        Client TLS Certificate Subject DN.    encryptedSecret : string
        For GET requests, this field contains the encrypted client secret, if one exists.  For POST and PUT requests, if you wish to reuse the existing secret, this field should be passed back unchanged.    enforceReplayPrevention : boolean
        Enforce replay prevention on JSON Web Tokens. This field is applicable only for Private Key JWT Client Authentication.    secret : string
        Client secret for Basic Authentication.  To update the client secret, specify the plaintext value in this field.  This field will not be populated for GET requests.    tokenEndpointAuthSigningAlgorithm : str
        The JSON Web Signature [JWS] algorithm that must be used to sign the JSON Web Tokens. This field is applicable only for Private Key JWT Client Authentication. All signing algorithms are allowed if value is not present <br>RS256 - RSA using SHA-256<br>RS384 - RSA using SHA-384<br>RS512 - RSA using SHA-512<br>ES256 - ECDSA using P256 Curve and SHA-256<br>ES384 - ECDSA using P384 Curve and SHA-384<br>ES512 - ECDSA using P521 Curve and SHA-512<br>PS256 - RSASSA-PSS using SHA-256 and MGF1 padding with SHA-256<br>PS384 - RSASSA-PSS using SHA-384 and MGF1 padding with SHA-384<br>PS512 - RSASSA-PSS using SHA-512 and MGF1 padding with SHA-512<br>RSASSA-PSS is only supported with SafeNet Luna, Thales nCipher or Java 11.    type : str
        Client authentication type.<br>The required field for type SECRET is secret.<br>The required fields for type CERTIFICATE are clientCertIssuerDn and clientCertSubjectDn.<br>The required field for type PRIVATE_KEY_JWT is: either jwks or jwksUrl.
    """

    __slots__ = ["clientCertIssuerDn", "clientCertSubjectDn", "encryptedSecret", "enforceReplayPrevention", "secret", "tokenEndpointAuthSigningAlgorithm", "type"]

    def __init__(self, clientCertIssuerDn=None, clientCertSubjectDn=None, encryptedSecret=None, enforceReplayPrevention=None, secret=None, tokenEndpointAuthSigningAlgorithm=None, type=None):
        self.clientCertIssuerDn: str = clientCertIssuerDn
        self.clientCertSubjectDn: str = clientCertSubjectDn
        self.encryptedSecret: str = encryptedSecret
        self.enforceReplayPrevention: bool = enforceReplayPrevention
        self.secret: str = secret
        self.tokenEndpointAuthSigningAlgorithm: str = tokenEndpointAuthSigningAlgorithm
        self.type: str = type

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ClientAuth):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.clientCertIssuerDn, self.clientCertSubjectDn, self.encryptedSecret, self.enforceReplayPrevention, self.secret, self.tokenEndpointAuthSigningAlgorithm, self.type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["clientCertIssuerDn", "clientCertSubjectDn", "encryptedSecret", "enforceReplayPrevention", "secret", "tokenEndpointAuthSigningAlgorithm", "type"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__