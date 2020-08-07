class ActionResult():
    """The result for non-download plugin actions.

    Attributes
    ----------
    message : string
        The message from the completed action.
    """

    __slots__ = ["message"]

    def __init__(self, message=None):
        self.message: str = message

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ActionResult):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.message))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["message"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__