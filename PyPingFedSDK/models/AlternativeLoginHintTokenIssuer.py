class AlternativeLoginHintTokenIssuer():
    """ JSON Web Key Set Settings.

    Attributes
    ----------
    issuer : string
        The issuer. Issuer is unique.
    jwks : string
        The JWKS.
    jwksURL : string
        The JWKS URL.

    """

    __slots__ = ["issuer", "jwks", "jwksURL"]
    def __init__(self, issuer, jwks=None, jwksURL=None):
            self.issuer = issuer
            self.jwks = jwks
            self.jwksURL = jwksURL
    
    def _validate(self):
        return any(x for x in ['issuer'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AlternativeLoginHintTokenIssuer):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((issuer, jwks, jwksURL))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
