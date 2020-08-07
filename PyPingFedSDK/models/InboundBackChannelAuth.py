class InboundBackChannelAuth():
    """

    Attributes
    ----------
    certs : array
        The certificate used for signature verification and XML encryption.    digitalSignature : boolean
        If incoming or outgoing messages must be signed.    httpBasicCredentials : str
        The credentials to use when you authenticate with the SOAP endpoint.    requireSsl : boolean
        Incoming HTTP transmissions must use a secure channel.    type : str
    verificationIssuerDN : string
        If a verification Subject DN is provided, you can optionally restrict the issuer to a specific trusted CA by specifying its DN in this field.    verificationSubjectDN : string
        If this property is set, the verification trust model is Anchored. The verification certificate must be signed by a trusted CA and included in the incoming message, and the subject DN of the expected certificate is specified in this property. If this property is not set, then a primary verification certificate must be specified in the certs array.
    """

    __slots__ = ["certs", "digitalSignature", "httpBasicCredentials", "requireSsl", "type", "verificationIssuerDN", "verificationSubjectDN"]

    def __init__(self, certs=None, digitalSignature=None, httpBasicCredentials=None, requireSsl=None, type=None, verificationIssuerDN=None, verificationSubjectDN=None):
        self.certs: list = certs
        self.digitalSignature: bool = digitalSignature
        self.httpBasicCredentials: str = httpBasicCredentials
        self.requireSsl: bool = requireSsl
        self.type: str = type
        self.verificationIssuerDN: str = verificationIssuerDN
        self.verificationSubjectDN: str = verificationSubjectDN

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, InboundBackChannelAuth):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.certs, self.digitalSignature, self.httpBasicCredentials, self.requireSsl, self.type, self.verificationIssuerDN, self.verificationSubjectDN))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["certs", "digitalSignature", "httpBasicCredentials", "requireSsl", "type", "verificationIssuerDN", "verificationSubjectDN"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__