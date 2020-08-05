class TokenProcessorAttribute():
    """An attribute for the token processor attribute contract.

    Attributes
    ----------
    masked : boolean
        Specifies whether this attribute is masked in PingFederate logs. Defaults to false.    name : string
        The name of this attribute.
    """

    __slots__ = ["masked", "name"]

    def __init__(self, name, masked=None):
        self.masked = masked
        self.name = name

    def _validate(self):
        return any(x for x in ['name'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, TokenProcessorAttribute):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.masked, self.name))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["masked", "name"]}

        return cls(**valid_data)
