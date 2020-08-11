class TokenExchangeGeneratorMapping():
    """A Token Generator mapping into an OAuth 2.0 Token Exchange requested token type.

    Attributes
    ----------
    defaultMapping : boolean
 Whether this is the default Token Generator Mapping. Defaults to false if not specified.
    requestedTokenType : string
 The Requested token type
    tokenGenerator : str
 The Token Generator used to generate the requested token

    """

    def __init__(self, requestedTokenType:str, tokenGenerator, defaultMapping:bool=None) -> None:
        self.defaultMapping = defaultMapping
        self.requestedTokenType = requestedTokenType
        self.tokenGenerator = tokenGenerator

    def _validate(self) -> bool:
        return any(x for x in ["requestedTokenType", "tokenGenerator"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, TokenExchangeGeneratorMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.defaultMapping, self.requestedTokenType, self.tokenGenerator))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["defaultMapping", "requestedTokenType", "tokenGenerator"]}

        return cls(**valid_data)