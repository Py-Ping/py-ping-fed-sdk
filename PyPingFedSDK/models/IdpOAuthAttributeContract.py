class IdpOAuthAttributeContract():
    """ A set of user attributes that the IdP sends in the OAuth Assertion Grant.

    Attributes
    ----------
    coreAttributes : array
        A list of read-only assertion attributes that are automatically populated by PingFederate.
    extendedAttributes : array
        A list of additional attributes that are present in the incoming assertion.

    """

    __slots__ = ["coreAttributes", "extendedAttributes"]
    def __init__(self, coreAttributes=None, extendedAttributes=None):
            self.coreAttributes = coreAttributes
            self.extendedAttributes = extendedAttributes
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, IdpOAuthAttributeContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((coreAttributes, extendedAttributes))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
