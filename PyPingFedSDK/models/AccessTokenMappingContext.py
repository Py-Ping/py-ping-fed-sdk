class AccessTokenMappingContext():
    """ The Access Token Attribute Mapping.

    Attributes
    ----------
    contextRef : str
        Reference to the associated Access Token Mapping Context instance.
    type : str
        The Access Token Mapping Context type.

    """

    __slots__ = ["contextRef", "type"]
    def __init__(self, type, contextRef):
            self.contextRef = contextRef
            self.type = type
    
    def _validate(self):
        return any(x for x in ['type', 'contextRef'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AccessTokenMappingContext):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((contextRef, type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
