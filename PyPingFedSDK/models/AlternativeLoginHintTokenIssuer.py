class AlternativeLoginHintTokenIssuer():
    """JSON Web Key Set Settings.

    Attributes
    ----------
    issuer : string
        The issuer. Issuer is unique.
    jwks : string
        The JWKS.
    jwksURL : string
        The JWKS URL.

    """

    def __init__(self, issuer:str, jwks:str=None, jwksURL:str=None) -> None:
        self.issuer = issuer
        self.jwks = jwks
        self.jwksURL = jwksURL

    def _validate(self) -> bool:
        return any(x for x in ["issuer"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AlternativeLoginHintTokenIssuer):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.issuer, self.jwks, self.jwksURL))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["issuer", "jwks", "jwksURL"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__