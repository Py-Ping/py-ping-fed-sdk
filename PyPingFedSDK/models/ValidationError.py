class ValidationError():
    """A data input validation error.

    Attributes
    ----------
    developerMessage : string
        Developer-oriented error message, if available.
    errorId : string
        Error identifier.
    fieldPath : string
        The path to the model field to which the error relates, if one exists.
    message : string
        User-friendly error description.

    """

    def __init__(self, developerMessage:str=None, errorId:str=None, fieldPath:str=None, message:str=None) -> None:
        self.developerMessage = developerMessage
        self.errorId = errorId
        self.fieldPath = fieldPath
        self.message = message

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ValidationError):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.developerMessage, self.errorId, self.fieldPath, self.message]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["developerMessage", "errorId", "fieldPath", "message"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__