class AccessTokenManagementSettings():
    """ General access token management settings.

    Attributes
    ----------
    defaultAccessTokenManagerRef : str
        Reference to the default access token manager, if one is defined.

    """

    __slots__ = ["defaultAccessTokenManagerRef"]
    def __init__(self, defaultAccessTokenManagerRef=None):
            self.defaultAccessTokenManagerRef = defaultAccessTokenManagerRef
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AccessTokenManagementSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((defaultAccessTokenManagerRef))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
