class ActionResult():
    """The result for non-download plugin actions.

    Attributes
    ----------
    message : string
        The message from the completed action.

    """

    def __init__(self, message:str=None) -> None:
        self.message = message

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ActionResult):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.message]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["message"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__