class ClientSecret():
    """Client Secret.

    Attributes
    ----------
    encryptedSecret : string
 For GET requests, this field contains the encrypted client secret, if one exists.  For POST and PUT requests, if you wish to reuse the existing secret, this field should be passed back unchanged.
    secret : string
 Client secret for Basic Authentication.  To update the client secret, specify the plaintext value in this field.  This field will not be populated for GET requests.

    """

    def __init__(self, encryptedSecret=None, secret=None) -> None:
        self.encryptedSecret = encryptedSecret
        self.secret = secret

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ClientSecret):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.encryptedSecret, self.secret))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["encryptedSecret", "secret"]}

        return cls(**valid_data)