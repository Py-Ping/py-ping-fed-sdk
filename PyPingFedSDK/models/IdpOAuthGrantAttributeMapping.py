class IdpOAuthGrantAttributeMapping():
    """ The OAuth Assertion Grant settings used to map from your IdP.

    Attributes
    ----------
    accessTokenManagerMappings : array
        A mapping in a connection that defines how access tokens are created.
    idpOAuthAttributeContract : str
        A set of user attributes that the IdP sends in the OAuth Assertion Grant.

    """

    __slots__ = ["accessTokenManagerMappings", "idpOAuthAttributeContract"]
    def __init__(self, accessTokenManagerMappings=None, idpOAuthAttributeContract=None):
            self.accessTokenManagerMappings = accessTokenManagerMappings
            self.idpOAuthAttributeContract = idpOAuthAttributeContract
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, IdpOAuthGrantAttributeMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((accessTokenManagerMappings, idpOAuthAttributeContract))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
