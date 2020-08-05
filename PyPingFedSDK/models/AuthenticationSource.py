class AuthenticationSource():
    """ An authentication source (IdP adapter or IdP connection).

    Attributes
    ----------
    sourceRef : str
        A reference to the authentication source.
    type : str
        The type of this authentication source.

    """

    __slots__ = ["sourceRef", "type"]
    def __init__(self, type, sourceRef):
            self.sourceRef = sourceRef
            self.type = type
    
    def _validate(self):
        return any(x for x in ['type', 'sourceRef'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AuthenticationSource):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((sourceRef, type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
