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

<<<<<<< HEAD
    def __init__(self, developerMessage=None, errorId=None, fieldPath=None, message=None) -> None:
        self.developerMessage = developerMessage
        self.errorId = errorId
        self.fieldPath = fieldPath
        self.message = message
=======
    def __init__(self, developerMessage=None, errorId=None, fieldPath=None, message=None):
        self.developerMessage: str = developerMessage
        self.errorId: str = errorId
        self.fieldPath: str = fieldPath
        self.message: str = message
>>>>>>> Baseline Sphinx generation

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
        return hash((self.developerMessage, self.errorId, self.fieldPath, self.message))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["developerMessage", "errorId", "fieldPath", "message"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
