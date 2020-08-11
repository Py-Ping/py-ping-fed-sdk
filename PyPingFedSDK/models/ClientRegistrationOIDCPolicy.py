class ClientRegistrationOIDCPolicy():
    """Client Registration Open ID Connect Policy settings.

    Attributes
    ----------
    idTokenContentEncryptionAlgorithm : str
        The JSON Web Encryption [JWE] content encryption algorithm for the ID Token.<br>AES_128_CBC_HMAC_SHA_256 - Composite AES-CBC-128 HMAC-SHA-256<br>AES_192_CBC_HMAC_SHA_384 - Composite AES-CBC-192 HMAC-SHA-384<br>AES_256_CBC_HMAC_SHA_512 - Composite AES-CBC-256 HMAC-SHA-512<br>AES-GCM-128 - AES_128_GCM<br>AES_192_GCM - AES-GCM-192<br>AES_256_GCM - AES-GCM-256
    idTokenEncryptionAlgorithm : str
        The JSON Web Encryption [JWE] encryption algorithm used to encrypt the content encryption key for the ID Token.<br>DIR - Direct Encryption with symmetric key<br>A128KW - AES-128 Key Wrap<br>A192KW - AES-192 Key Wrap<br>A256KW - AES-256 Key Wrap<br>A128GCMKW - AES-GCM-128 key encryption<br>A192GCMKW - AES-GCM-192 key encryption<br>A256GCMKW - AES-GCM-256 key encryption<br>ECDH_ES - ECDH-ES<br>ECDH_ES_A128KW - ECDH-ES with AES-128 Key Wrap<br>ECDH_ES_A192KW - ECDH-ES with AES-192 Key Wrap<br>ECDH_ES_A256KW - ECDH-ES with AES-256 Key Wrap<br>RSA_OAEP - RSAES OAEP<br>
    idTokenSigningAlgorithm : str
        The JSON Web Signature [JWS] algorithm required for the ID Token.<br>NONE - No signing algorithm<br>HS256 - HMAC using SHA-256<br>HS384 - HMAC using SHA-384<br>HS512 - HMAC using SHA-512<br>RS256 - RSA using SHA-256<br>RS384 - RSA using SHA-384<br>RS512 - RSA using SHA-512<br>ES256 - ECDSA using P256 Curve and SHA-256<br>ES384 - ECDSA using P384 Curve and SHA-384<br>ES512 - ECDSA using P521 Curve and SHA-512<br>PS256 - RSASSA-PSS using SHA-256 and MGF1 padding with SHA-256<br>PS384 - RSASSA-PSS using SHA-384 and MGF1 padding with SHA-384<br>PS512 - RSASSA-PSS using SHA-512 and MGF1 padding with SHA-512<br>A null value will represent the default algorithm which is RS256.<br>RSASSA-PSS is only supported with SafeNet Luna, Thales nCipher or Java 11
    policyGroup : str
        The Open ID Connect policy. A null value will represent the default policy group.

    """

    def __init__(self, idTokenContentEncryptionAlgorithm=None, idTokenEncryptionAlgorithm=None, idTokenSigningAlgorithm=None, policyGroup=None) -> None:
        self.idTokenContentEncryptionAlgorithm = idTokenContentEncryptionAlgorithm
        self.idTokenEncryptionAlgorithm = idTokenEncryptionAlgorithm
        self.idTokenSigningAlgorithm = idTokenSigningAlgorithm
        self.policyGroup = policyGroup

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ClientRegistrationOIDCPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.idTokenContentEncryptionAlgorithm, self.idTokenEncryptionAlgorithm, self.idTokenSigningAlgorithm, self.policyGroup))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["idTokenContentEncryptionAlgorithm", "idTokenEncryptionAlgorithm", "idTokenSigningAlgorithm", "policyGroup"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__