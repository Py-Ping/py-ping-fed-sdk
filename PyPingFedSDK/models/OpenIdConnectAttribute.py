class OpenIdConnectAttribute():
    """ An attribute for the OpenID Connect returned to OAuth clients.

    Attributes
    ----------
    includeInIdToken : boolean
        Attribute is included in the ID Token.
    includeInUserInfo : boolean
        Attribute is included in the User Info
    name : string
        The name of this attribute.

    """

    __slots__ = ["includeInIdToken", "includeInUserInfo", "name"]
    def __init__(self, name, includeInIdToken=None, includeInUserInfo=None):
            self.includeInIdToken = includeInIdToken
            self.includeInUserInfo = includeInUserInfo
            self.name = name
    
    def _validate(self):
        return any(x for x in ['name'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, OpenIdConnectAttribute):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((includeInIdToken, includeInUserInfo, name))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
