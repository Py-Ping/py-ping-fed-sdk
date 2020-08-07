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

<<<<<<< HEAD
    def __init__(self, var_type, digitalSignature=None, httpBasicCredentials=None) -> None:
        self.digitalSignature = digitalSignature
        self.httpBasicCredentials = httpBasicCredentials
        self.var_type = var_type
=======
    def __init__(self, type, digitalSignature=None, httpBasicCredentials=None):
        self.digitalSignature: bool = digitalSignature
        self.httpBasicCredentials: str = httpBasicCredentials
        self.type: str = type
>>>>>>> Baseline Sphinx generation

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
        return hash((self.digitalSignature, self.httpBasicCredentials, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["digitalSignature", "httpBasicCredentials", "var_type"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
