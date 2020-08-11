class AttributeFulfillmentValue():
    """Defines how an attribute in an attribute contract should be populated.

    Attributes
    ----------
    source : str
        The attribute value source.
    value : string
        The value for this attribute.

    """

    def __init__(self, source, value:str) -> None:
        self.source = source
        self.value = value

    def _validate(self) -> bool:
        return any(x for x in ["source", "value"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AttributeFulfillmentValue):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.source, self.value))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["source", "value"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__