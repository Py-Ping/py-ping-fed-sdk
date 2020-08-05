class OAuthRole():
    """OAuth role settings.

    Attributes
    ----------
    enableOauth : boolean
        Enable OAuth 2.0 Authorization Server (AS) Role.    enableOpenIdConnect : boolean
        Enable Open ID Connect.
    """

    __slots__ = ["enableOauth", "enableOpenIdConnect"]

    def __init__(self, enableOauth=None, enableOpenIdConnect=None):
        self.enableOauth = enableOauth
        self.enableOpenIdConnect = enableOpenIdConnect

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, OAuthRole):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.enableOauth, self.enableOpenIdConnect))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["enableOauth", "enableOpenIdConnect"]}

        return cls(**valid_data)
