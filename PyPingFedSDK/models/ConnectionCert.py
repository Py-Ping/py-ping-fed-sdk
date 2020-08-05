class ConnectionCert():
    """A certificate used for signature verification or XML encryption.

    Attributes
    ----------
    activeVerificationCert : boolean
        Indicates whether this is an active signature verification certificate.    certView : str
        Certificate details. This property is read-only and is always ignored on a POST or PUT.    encryptionCert : boolean
        Indicates whether to use this cert to encrypt outgoing assertions. Only one certificate in the collection can have this flag set.    primaryVerificationCert : boolean
        Indicates whether this is the primary signature verification certificate. Only one certificate in the collection can have this flag set.    secondaryVerificationCert : boolean
        Indicates whether this is the secondary signature verification certificate. Only one certificate in the collection can have this flag set.    x509File : str
        The certificate data. This property must always be supplied on a POST or PUT.
    """

    __slots__ = ["activeVerificationCert", "certView", "encryptionCert", "primaryVerificationCert", "secondaryVerificationCert", "x509File"]

    def __init__(self, x509File, activeVerificationCert=None, certView=None, encryptionCert=None, primaryVerificationCert=None, secondaryVerificationCert=None):
        self.activeVerificationCert = activeVerificationCert
        self.certView = certView
        self.encryptionCert = encryptionCert
        self.primaryVerificationCert = primaryVerificationCert
        self.secondaryVerificationCert = secondaryVerificationCert
        self.x509File = x509File

    def _validate(self):
        return any(x for x in ['x509File'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ConnectionCert):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.activeVerificationCert, self.certView, self.encryptionCert, self.primaryVerificationCert, self.secondaryVerificationCert, self.x509File))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["activeVerificationCert", "certView", "encryptionCert", "primaryVerificationCert", "secondaryVerificationCert", "x509File"]}

        return cls(**valid_data)
