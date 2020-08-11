class AssertionLifetime():
    """The timeframe of validity before and after the issuance of the assertion.

    Attributes
    ----------
    minutesAfter : integer
        Assertion validity in minutes after the assertion issuance.
    minutesBefore : integer
        Assertion validity in minutes before the assertion issuance.

    """

    def __init__(self, minutesBefore:int, minutesAfter:int) -> None:
        self.minutesAfter = minutesAfter
        self.minutesBefore = minutesBefore

    def _validate(self) -> bool:
        return any(x for x in ["minutesBefore", "minutesAfter"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AssertionLifetime):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.minutesAfter, self.minutesBefore))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["minutesAfter", "minutesBefore"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__