class OAuthOidcKeysSettings():
    """Setting for OAuth/OpenID Connect signing and decryption key settings.

    Attributes
    ----------
    p256ActiveCertRef : str
 Reference to the P-256 key currently active.
    p256DecryptionActiveCertRef : str
 Reference to the P-256 decryption key currently active.
    p256DecryptionPreviousCertRef : str
 Reference to the P-256 decryption key previously active.
    p256DecryptionPublishX5cParameter : boolean
 Enable publishing of the P-256 certificate chain associated with the active key.
    p256PreviousCertRef : str
 Reference to the P-256 key previously active.
    p256PublishX5cParameter : boolean
 Enable publishing of the P-256 certificate chain associated with the active key.
    p384ActiveCertRef : str
 Reference to the P-384 key currently active.
    p384DecryptionActiveCertRef : str
 Reference to the P-384 decryption key currently active.
    p384DecryptionPreviousCertRef : str
 Reference to the P-384 decryption key previously active.
    p384DecryptionPublishX5cParameter : boolean
 Enable publishing of the P-384 certificate chain associated with the active key.
    p384PreviousCertRef : str
 Reference to the P-384 key previously active.
    p384PublishX5cParameter : boolean
 Enable publishing of the P-384 certificate chain associated with the active key.
    p521ActiveCertRef : str
 Reference to the P-521 key currently active.
    p521DecryptionActiveCertRef : str
 Reference to the P-521 decryption key currently active.
    p521DecryptionPreviousCertRef : str
 Reference to the P-521 decryption key previously active.
    p521DecryptionPublishX5cParameter : boolean
 Enable publishing of the P-521 certificate chain associated with the active key.
    p521PreviousCertRef : str
 Reference to the P-521 key previously active.
    p521PublishX5cParameter : boolean
 Enable publishing of the P-521 certificate chain associated with the active key.
    rsaActiveCertRef : str
 Reference to the RSA key currently active.
    rsaDecryptionActiveCertRef : str
 Reference to the RSA decryption key currently active.
    rsaDecryptionPreviousCertRef : str
 Reference to the RSA decryption key previously active.
    rsaDecryptionPublishX5cParameter : boolean
 Enable publishing of the RSA certificate chain associated with the active key.
    rsaPreviousCertRef : str
 Reference to the RSA key previously active.
    rsaPublishX5cParameter : boolean
 Enable publishing of the RSA certificate chain associated with the active key.
    staticJwksEnabled : boolean
 Enable static keys.

    """

<<<<<<< HEAD
    def __init__(self, staticJwksEnabled, p256ActiveCertRef=None, p256DecryptionActiveCertRef=None, p256DecryptionPreviousCertRef=None, p256DecryptionPublishX5cParameter=None, p256PreviousCertRef=None, p256PublishX5cParameter=None, p384ActiveCertRef=None, p384DecryptionActiveCertRef=None, p384DecryptionPreviousCertRef=None, p384DecryptionPublishX5cParameter=None, p384PreviousCertRef=None, p384PublishX5cParameter=None, p521ActiveCertRef=None, p521DecryptionActiveCertRef=None, p521DecryptionPreviousCertRef=None, p521DecryptionPublishX5cParameter=None, p521PreviousCertRef=None, p521PublishX5cParameter=None, rsaActiveCertRef=None, rsaDecryptionActiveCertRef=None, rsaDecryptionPreviousCertRef=None, rsaDecryptionPublishX5cParameter=None, rsaPreviousCertRef=None, rsaPublishX5cParameter=None) -> None:
        self.p256ActiveCertRef = p256ActiveCertRef
        self.p256DecryptionActiveCertRef = p256DecryptionActiveCertRef
        self.p256DecryptionPreviousCertRef = p256DecryptionPreviousCertRef
        self.p256DecryptionPublishX5cParameter = p256DecryptionPublishX5cParameter
        self.p256PreviousCertRef = p256PreviousCertRef
        self.p256PublishX5cParameter = p256PublishX5cParameter
        self.p384ActiveCertRef = p384ActiveCertRef
        self.p384DecryptionActiveCertRef = p384DecryptionActiveCertRef
        self.p384DecryptionPreviousCertRef = p384DecryptionPreviousCertRef
        self.p384DecryptionPublishX5cParameter = p384DecryptionPublishX5cParameter
        self.p384PreviousCertRef = p384PreviousCertRef
        self.p384PublishX5cParameter = p384PublishX5cParameter
        self.p521ActiveCertRef = p521ActiveCertRef
        self.p521DecryptionActiveCertRef = p521DecryptionActiveCertRef
        self.p521DecryptionPreviousCertRef = p521DecryptionPreviousCertRef
        self.p521DecryptionPublishX5cParameter = p521DecryptionPublishX5cParameter
        self.p521PreviousCertRef = p521PreviousCertRef
        self.p521PublishX5cParameter = p521PublishX5cParameter
        self.rsaActiveCertRef = rsaActiveCertRef
        self.rsaDecryptionActiveCertRef = rsaDecryptionActiveCertRef
        self.rsaDecryptionPreviousCertRef = rsaDecryptionPreviousCertRef
        self.rsaDecryptionPublishX5cParameter = rsaDecryptionPublishX5cParameter
        self.rsaPreviousCertRef = rsaPreviousCertRef
        self.rsaPublishX5cParameter = rsaPublishX5cParameter
        self.staticJwksEnabled = staticJwksEnabled
=======
    def __init__(self, staticJwksEnabled, p256ActiveCertRef=None, p256DecryptionActiveCertRef=None, p256DecryptionPreviousCertRef=None, p256DecryptionPublishX5cParameter=None, p256PreviousCertRef=None, p256PublishX5cParameter=None, p384ActiveCertRef=None, p384DecryptionActiveCertRef=None, p384DecryptionPreviousCertRef=None, p384DecryptionPublishX5cParameter=None, p384PreviousCertRef=None, p384PublishX5cParameter=None, p521ActiveCertRef=None, p521DecryptionActiveCertRef=None, p521DecryptionPreviousCertRef=None, p521DecryptionPublishX5cParameter=None, p521PreviousCertRef=None, p521PublishX5cParameter=None, rsaActiveCertRef=None, rsaDecryptionActiveCertRef=None, rsaDecryptionPreviousCertRef=None, rsaDecryptionPublishX5cParameter=None, rsaPreviousCertRef=None, rsaPublishX5cParameter=None):
        self.p256ActiveCertRef: str = p256ActiveCertRef
        self.p256DecryptionActiveCertRef: str = p256DecryptionActiveCertRef
        self.p256DecryptionPreviousCertRef: str = p256DecryptionPreviousCertRef
        self.p256DecryptionPublishX5cParameter: bool = p256DecryptionPublishX5cParameter
        self.p256PreviousCertRef: str = p256PreviousCertRef
        self.p256PublishX5cParameter: bool = p256PublishX5cParameter
        self.p384ActiveCertRef: str = p384ActiveCertRef
        self.p384DecryptionActiveCertRef: str = p384DecryptionActiveCertRef
        self.p384DecryptionPreviousCertRef: str = p384DecryptionPreviousCertRef
        self.p384DecryptionPublishX5cParameter: bool = p384DecryptionPublishX5cParameter
        self.p384PreviousCertRef: str = p384PreviousCertRef
        self.p384PublishX5cParameter: bool = p384PublishX5cParameter
        self.p521ActiveCertRef: str = p521ActiveCertRef
        self.p521DecryptionActiveCertRef: str = p521DecryptionActiveCertRef
        self.p521DecryptionPreviousCertRef: str = p521DecryptionPreviousCertRef
        self.p521DecryptionPublishX5cParameter: bool = p521DecryptionPublishX5cParameter
        self.p521PreviousCertRef: str = p521PreviousCertRef
        self.p521PublishX5cParameter: bool = p521PublishX5cParameter
        self.rsaActiveCertRef: str = rsaActiveCertRef
        self.rsaDecryptionActiveCertRef: str = rsaDecryptionActiveCertRef
        self.rsaDecryptionPreviousCertRef: str = rsaDecryptionPreviousCertRef
        self.rsaDecryptionPublishX5cParameter: bool = rsaDecryptionPublishX5cParameter
        self.rsaPreviousCertRef: str = rsaPreviousCertRef
        self.rsaPublishX5cParameter: bool = rsaPublishX5cParameter
        self.staticJwksEnabled: bool = staticJwksEnabled
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["staticJwksEnabled"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, OAuthOidcKeysSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.p256ActiveCertRef, self.p256DecryptionActiveCertRef, self.p256DecryptionPreviousCertRef, self.p256DecryptionPublishX5cParameter, self.p256PreviousCertRef, self.p256PublishX5cParameter, self.p384ActiveCertRef, self.p384DecryptionActiveCertRef, self.p384DecryptionPreviousCertRef, self.p384DecryptionPublishX5cParameter, self.p384PreviousCertRef, self.p384PublishX5cParameter, self.p521ActiveCertRef, self.p521DecryptionActiveCertRef, self.p521DecryptionPreviousCertRef, self.p521DecryptionPublishX5cParameter, self.p521PreviousCertRef, self.p521PublishX5cParameter, self.rsaActiveCertRef, self.rsaDecryptionActiveCertRef, self.rsaDecryptionPreviousCertRef, self.rsaDecryptionPublishX5cParameter, self.rsaPreviousCertRef, self.rsaPublishX5cParameter, self.staticJwksEnabled))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["p256ActiveCertRef", "p256DecryptionActiveCertRef", "p256DecryptionPreviousCertRef", "p256DecryptionPublishX5cParameter", "p256PreviousCertRef", "p256PublishX5cParameter", "p384ActiveCertRef", "p384DecryptionActiveCertRef", "p384DecryptionPreviousCertRef", "p384DecryptionPublishX5cParameter", "p384PreviousCertRef", "p384PublishX5cParameter", "p521ActiveCertRef", "p521DecryptionActiveCertRef", "p521DecryptionPreviousCertRef", "p521DecryptionPublishX5cParameter", "p521PreviousCertRef", "p521PublishX5cParameter", "rsaActiveCertRef", "rsaDecryptionActiveCertRef", "rsaDecryptionPreviousCertRef", "rsaDecryptionPublishX5cParameter", "rsaPreviousCertRef", "rsaPublishX5cParameter", "staticJwksEnabled"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
