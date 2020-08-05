class ValidationError():
    """ A data input validation error.

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

    __slots__ = ["developerMessage", "errorId", "fieldPath", "message"]
    def __init__(self, developerMessage=None, errorId=None, fieldPath=None, message=None):
            self.developerMessage = developerMessage
            self.errorId = errorId
            self.fieldPath = fieldPath
            self.message = message
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ValidationError):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((developerMessage, errorId, fieldPath, message))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
