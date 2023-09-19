from enum import Enum

from pingfedsdk.model import Model


class ValidationError(Model):
    """A data input validation error.

    Attributes
    ----------
    errorId: str
        Error identifier.

    message: str
        User-friendly error description.

    developerMessage: str
        Developer-oriented error message, if available.

    fieldPath: str
        The path to the model field to which the error relates, if one exists.

    """
    def __init__(self, errorId: str = None, message: str = None, developerMessage: str = None, fieldPath: str = None) -> None:
        self.errorId = errorId
        self.message = message
        self.developerMessage = developerMessage
        self.fieldPath = fieldPath

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ValidationError):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.errorId, self.message, self.developerMessage, self.fieldPath]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["errorId", "message", "developerMessage", "fieldPath"] and v is not None:
                if k == "errorId":
                    valid_data[k] = str(v)
                if k == "message":
                    valid_data[k] = str(v)
                if k == "developerMessage":
                    valid_data[k] = str(v)
                if k == "fieldPath":
                    valid_data[k] = str(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["errorId", "message", "developerMessage", "fieldPath"]:
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
