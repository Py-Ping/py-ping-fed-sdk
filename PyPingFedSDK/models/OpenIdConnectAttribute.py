class OpenIdConnectAttribute():
    """An attribute for the OpenID Connect returned to OAuth clients.

    Attributes
    ----------
    includeInIdToken : boolean
 Attribute is included in the ID Token.
    includeInUserInfo : boolean
 Attribute is included in the User Info
    name : string
 The name of this attribute.

    """

<<<<<<< HEAD
    def __init__(self, name, includeInIdToken=None, includeInUserInfo=None) -> None:
        self.includeInIdToken = includeInIdToken
        self.includeInUserInfo = includeInUserInfo
        self.name = name
=======
    def __init__(self, name, includeInIdToken=None, includeInUserInfo=None):
        self.includeInIdToken: bool = includeInIdToken
        self.includeInUserInfo: bool = includeInUserInfo
        self.name: str = name
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["name"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, OpenIdConnectAttribute):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.includeInIdToken, self.includeInUserInfo, self.name))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["includeInIdToken", "includeInUserInfo", "name"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
