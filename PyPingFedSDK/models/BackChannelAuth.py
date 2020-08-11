class BackChannelAuth():
    """The SOAP authentication methods when sending or receiving a message using SOAP back channel.

    Attributes
    ----------
    digitalSignature : boolean
        If incoming or outgoing messages must be signed.
    httpBasicCredentials : str
        The credentials to use when you authenticate with the SOAP endpoint.
    type : str
        The back channel authentication type.

    """

    def __init__(self, var_type, digitalSignature:bool=None, httpBasicCredentials=None) -> None:
        self.digitalSignature = digitalSignature
        self.httpBasicCredentials = httpBasicCredentials
        self.var_type = var_type

    def _validate(self) -> bool:
        return any(x for x in ["var_type"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, BackChannelAuth):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.digitalSignature, self.httpBasicCredentials, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["digitalSignature", "httpBasicCredentials", "var_type"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__