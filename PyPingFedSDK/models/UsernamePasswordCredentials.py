class UsernamePasswordCredentials():
    """Username and password credentials.

    Attributes
    ----------
    encryptedPassword : string
        For GET requests, this field contains the encrypted password, if one exists.  For POST and PUT requests, if you wish to reuse the existing password, this field should be passed back unchanged.
    password : string
        User password.  To update the password, specify the plaintext value in this field.  This field will not be populated for GET requests.
    username : string
        The username.

    """

    def __init__(self, encryptedPassword:str=None, password:str=None, username:str=None) -> None:
        self.encryptedPassword = encryptedPassword
        self.password = password
        self.username = username

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, UsernamePasswordCredentials):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.encryptedPassword, self.password, self.username]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["encryptedPassword", "password", "username"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__