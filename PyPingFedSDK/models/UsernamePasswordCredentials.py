class UsernamePasswordCredentials():
    """ Username and password credentials.

    Attributes
    ----------
    encryptedPassword : string
        For GET requests, this field contains the encrypted password, if one exists.  For POST and PUT requests, if you wish to reuse the existing password, this field should be passed back unchanged.
    password : string
        User password.  To update the password, specify the plaintext value in this field.  This field will not be populated for GET requests.
    username : string
        The username.

    """

    __slots__ = ["encryptedPassword", "password", "username"]
    def __init__(self, encryptedPassword=None, password=None, username=None):
            self.encryptedPassword = encryptedPassword
            self.password = password
            self.username = username
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, UsernamePasswordCredentials):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((encryptedPassword, password, username))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
