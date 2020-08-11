class JwksSettings():
    """JSON Web Key Set Settings.

    Attributes
    ----------
    jwks : string
 JSON Web Key Set (JWKS) document of the OAuth client. Either 'jwks' or 'jwksUrl' must be provided if private key JWT client authentication or signed requests is enabled.  If the client signs its JWTs using an RSASSA-PSS signing algorithm, PingFederate must either use Java 11 or be integrated with a hardware security module (HSM) to process the digital signatures.
    jwksUrl : string
 JSON Web Key Set (JWKS) URL of the OAuth client. Either 'jwks' or 'jwksUrl' must be provided if private key JWT client authentication or signed requests is enabled.  If the client signs its JWTs using an RSASSA-PSS signing algorithm, PingFederate must either use Java 11 or be integrated with a hardware security module (HSM) to process the digital signatures.

    """

    def __init__(self, jwks:str=None, jwksUrl:str=None) -> None:
        self.jwks = jwks
        self.jwksUrl = jwksUrl

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, JwksSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.jwks, self.jwksUrl))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["jwks", "jwksUrl"]}

        return cls(**valid_data)