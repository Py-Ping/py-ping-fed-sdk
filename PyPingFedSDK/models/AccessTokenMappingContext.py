class AccessTokenMappingContext():
    """The Access Token Attribute Mapping.

    Attributes
    ----------
    contextRef : str
 Reference to the associated Access Token Mapping Context instance.
    type : str
 The Access Token Mapping Context type.

    """

    def __init__(self, var_type, contextRef) -> None:
        self.contextRef = contextRef
        self.var_type = var_type

    def _validate(self) -> bool:
        return any(x for x in ["var_type", "contextRef"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AccessTokenMappingContext):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.contextRef, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["contextRef", "var_type"]}

        return cls(**valid_data)