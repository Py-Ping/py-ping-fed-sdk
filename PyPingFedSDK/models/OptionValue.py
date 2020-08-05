class OptionValue():
    """An option name and value associated with a selection field.

    Attributes
    ----------
    name : string
        The name of the option.    value : string
        The value associated with this option.
    """

    __slots__ = ["name", "value"]

    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, OptionValue):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.name, self.value))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["name", "value"]}

        return cls(**valid_data)
