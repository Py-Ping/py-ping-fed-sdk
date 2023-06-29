from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.validation_error import ValidationError


class ApiResult(Model):
    """Details on the result of the operation.

    Attributes
    ----------
    resultId: str
        Result identifier.

    message: str
        Success or error message.

    developerMessage: str
        Developer-oriented error message, if available.

    validationErrors: list
        List of validation errors, if any.

    """

    def __init__(self, resultId: str = None, message: str = None, developerMessage: str = None, validationErrors: list = None) -> None:
        self.resultId = resultId
        self.message = message
        self.developerMessage = developerMessage
        self.validationErrors = validationErrors

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ApiResult):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.resultId, self.message, self.developerMessage, self.validationErrors]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["resultId", "message", "developerMessage", "validationErrors"] and v is not None:
                if k == "resultId":
                    valid_data[k] = str(v)
                if k == "message":
                    valid_data[k] = str(v)
                if k == "developerMessage":
                    valid_data[k] = str(v)
                if k == "validationErrors":
                    valid_data[k] = [ValidationError(**x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["resultId", "message", "developerMessage", "validationErrors"]:
                if isinstance(v, Model):
                    body[k] = v.to_dict(remove_nonetypes)
                elif isinstance(v, list):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, dict):
                    vals = {}
                    for x, y in v.items():
                        if isinstance(y, Model):
                            vals[x] = y.to_dict(remove_nonetypes)
                        elif not remove_nonetypes or (remove_nonetypes and y is not None):
                            vals[x] = y
                    body[k] = vals
                elif isinstance(v, set):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, Enum):
                    body[k] = str(v).split('.')[-1]
                elif not remove_nonetypes or (remove_nonetypes and v is not None):
                    body[k] = v
        return body
