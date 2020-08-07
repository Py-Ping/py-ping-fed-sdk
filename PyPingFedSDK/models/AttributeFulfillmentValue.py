class AttributeFulfillmentValue():
    """Defines how an attribute in an attribute contract should be populated.

    Attributes
    ----------
    source : str
        The attribute value source.    value : string
        The value for this attribute.
    """

    __slots__ = ["source", "value"]

    def __init__(self, source, value):
        self.source: str = source
        self.value: str = value

    def _validate(self):
        return any(x for x in ['source', 'value'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AttributeFulfillmentValue):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.source, self.value))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["source", "value"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__