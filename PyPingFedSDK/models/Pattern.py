class Pattern():
    """

    Attributes
    ----------
    flags : integer
    pattern : string

    """

    def __init__(self, flags:int=None, pattern:str=None) -> None:
        self.flags = flags
        self.pattern = pattern

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Pattern):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.flags, self.pattern))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["flags", "pattern"]}

        return cls(**valid_data)