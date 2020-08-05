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

    __slots__ = ["digitalSignature", "httpBasicCredentials", "sslAuthKeyPairRef", "type", "validatePartnerCert"]
    def __init__(self, digitalSignature=None, httpBasicCredentials=None, sslAuthKeyPairRef=None, type=None, validatePartnerCert=None):
            self.digitalSignature = digitalSignature
            self.httpBasicCredentials = httpBasicCredentials
            self.sslAuthKeyPairRef = sslAuthKeyPairRef
            self.type = type
            self.validatePartnerCert = validatePartnerCert
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, OutboundBackChannelAuth):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((digitalSignature, httpBasicCredentials, sslAuthKeyPairRef, type, validatePartnerCert))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
