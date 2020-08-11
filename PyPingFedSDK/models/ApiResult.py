class ApiResult():
    """Details on the result of the operation.

    Attributes
    ----------
    developerMessage : string
        Developer-oriented error message, if available.
    message : string
        Success or error message.
    resultId : string
        Result identifier.
    validationErrors : array
        List of validation errors, if any.

    """

    def __init__(self, developerMessage:str=None, message:str=None, resultId:str=None, validationErrors:list=None) -> None:
        self.developerMessage = developerMessage
        self.message = message
        self.resultId = resultId
        self.validationErrors = validationErrors

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ApiResult):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.developerMessage, self.message, self.resultId, self.validationErrors))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["developerMessage", "message", "resultId", "validationErrors"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__