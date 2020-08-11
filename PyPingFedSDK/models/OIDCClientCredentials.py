class OIDCClientCredentials():
    """The OpenID Connect Client Credentials settings. This is required for an OIDC Connection.

    Attributes
    ----------
    clientId : string
 The OpenID Connect client identitification.
    clientSecret : string
 The OpenID Connect client secret. To update the client secret, specify the plaintext value in this field.  This field will not be populated for GET requests.
    encryptedSecret : string
 For GET requests, this field contains the encrypted client secret, if one exists.  For POST and PUT requests, if you wish to reuse the existing secret, this field should be passed back unchanged.

    """

    def __init__(self, clientId:str, clientSecret:str=None, encryptedSecret:str=None) -> None:
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.encryptedSecret = encryptedSecret

    def _validate(self) -> bool:
        return any(x for x in ["clientId"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, OIDCClientCredentials):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.clientId, self.clientSecret, self.encryptedSecret))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["clientId", "clientSecret", "encryptedSecret"]}

        return cls(**valid_data)