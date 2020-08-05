class AssertionLifetime():
    """ The timeframe of validity before and after the issuance of the assertion.

    Attributes
    ----------
    minutesAfter : integer
        Assertion validity in minutes after the assertion issuance.
    minutesBefore : integer
        Assertion validity in minutes before the assertion issuance.

    """

    __slots__ = ["minutesAfter", "minutesBefore"]
    def __init__(self, minutesBefore, minutesAfter):
            self.minutesAfter = minutesAfter
            self.minutesBefore = minutesBefore
    
    def _validate(self):
        return any(x for x in ['minutesBefore', 'minutesAfter'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AssertionLifetime):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((minutesAfter, minutesBefore))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
