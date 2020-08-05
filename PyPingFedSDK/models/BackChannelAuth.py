class BackChannelAuth():
    """The SOAP authentication methods when sending or receiving a message using SOAP back channel.

    Attributes
    ----------
    digitalSignature : boolean
        If incoming or outgoing messages must be signed.    httpBasicCredentials : str
        The credentials to use when you authenticate with the SOAP endpoint.    type : str
        The back channel authentication type.
    """

    __slots__ = ["digitalSignature", "httpBasicCredentials", "type"]

    def __init__(self, type, digitalSignature=None, httpBasicCredentials=None):
        self.digitalSignature = digitalSignature
        self.httpBasicCredentials = httpBasicCredentials
        self.type = type

    def _validate(self):
        return any(x for x in ['type'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, BackChannelAuth):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.digitalSignature, self.httpBasicCredentials, self.type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["digitalSignature", "httpBasicCredentials", "type"]}

        return cls(**valid_data)
