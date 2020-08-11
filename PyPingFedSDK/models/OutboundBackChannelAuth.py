class OutboundBackChannelAuth():
    """

    Attributes
    ----------
    digitalSignature : boolean
        If incoming or outgoing messages must be signed.
    httpBasicCredentials : str
        The credentials to use when you authenticate with the SOAP endpoint.
    sslAuthKeyPairRef : str
        The ID of the key pair used to authenticate with your partner's SOAP endpoint. The ID of the key pair is also known as the alias and can be found by viewing the corresponding certificate under 'SSL Server Certificates' in the PingFederate Administrative Console.
    type : str
    validatePartnerCert : boolean
        Validate the partner server certificate. Default is true.

    """

    def __init__(self, digitalSignature:bool=None, httpBasicCredentials=None, sslAuthKeyPairRef=None, var_type=None, validatePartnerCert:bool=None) -> None:
        self.digitalSignature = digitalSignature
        self.httpBasicCredentials = httpBasicCredentials
        self.sslAuthKeyPairRef = sslAuthKeyPairRef
        self.var_type = var_type
        self.validatePartnerCert = validatePartnerCert

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, OutboundBackChannelAuth):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.digitalSignature, self.httpBasicCredentials, self.sslAuthKeyPairRef, self.var_type, self.validatePartnerCert))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["digitalSignature", "httpBasicCredentials", "sslAuthKeyPairRef", "var_type", "validatePartnerCert"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__