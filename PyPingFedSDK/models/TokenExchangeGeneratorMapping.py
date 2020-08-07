class TokenExchangeGeneratorMapping():
    """A Token Generator mapping into an OAuth 2.0 Token Exchange requested token type.

    Attributes
    ----------
    defaultMapping : boolean
        Whether this is the default Token Generator Mapping. Defaults to false if not specified.    requestedTokenType : string
        The Requested token type    tokenGenerator : str
        The Token Generator used to generate the requested token
    """

    __slots__ = ["defaultMapping", "requestedTokenType", "tokenGenerator"]

    def __init__(self, requestedTokenType, tokenGenerator, defaultMapping=None):
        self.defaultMapping: bool = defaultMapping
        self.requestedTokenType: str = requestedTokenType
        self.tokenGenerator: str = tokenGenerator

    def _validate(self):
        return any(x for x in ['requestedTokenType', 'tokenGenerator'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, TokenExchangeGeneratorMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.defaultMapping, self.requestedTokenType, self.tokenGenerator))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["defaultMapping", "requestedTokenType", "tokenGenerator"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__