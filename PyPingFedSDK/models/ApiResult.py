class ApiResult():
    """Details on the result of the operation.

    Attributes
    ----------
    developerMessage : string
        Developer-oriented error message, if available.    message : string
        Success or error message.    resultId : string
        Result identifier.    validationErrors : array
        List of validation errors, if any.
    """

    __slots__ = ["developerMessage", "message", "resultId", "validationErrors"]

    def __init__(self, developerMessage=None, message=None, resultId=None, validationErrors=None):
        self.developerMessage: str = developerMessage
        self.message: str = message
        self.resultId: str = resultId
        self.validationErrors: list = validationErrors

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ApiResult):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.developerMessage, self.message, self.resultId, self.validationErrors))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["developerMessage", "message", "resultId", "validationErrors"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__