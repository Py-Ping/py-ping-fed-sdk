class ParameterValues():
    """Parameter Values.

    Attributes
    ----------
    values : array
        A List of values
    """

    __slots__ = ["values"]

    def __init__(self, values=None):
        self.values = values

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ParameterValues):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.values))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["values"]}

        return cls(**valid_data)
