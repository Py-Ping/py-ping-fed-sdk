class AccessTokenMappingContext():
    """The Access Token Attribute Mapping.

    Attributes
    ----------
    contextRef : str
        Reference to the associated Access Token Mapping Context instance.    type : str
        The Access Token Mapping Context type.
    """

    __slots__ = ["contextRef", "type"]

    def __init__(self, type, contextRef):
        self.contextRef: str = contextRef
        self.type: str = type

    def _validate(self):
        return any(x for x in ['type', 'contextRef'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AccessTokenMappingContext):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.contextRef, self.type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["contextRef", "type"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__