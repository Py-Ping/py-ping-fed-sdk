class AttributeFulfillmentValue():
    """ Defines how an attribute in an attribute contract should be populated.

    Attributes
    ----------
    source : str
        The attribute value source.
    value : string
        The value for this attribute.

    """

    __slots__ = ["source", "value"]
    def __init__(self, source, value):
            self.source = source
            self.value = value
    
    def _validate(self):
        return any(x for x in ['source', 'value'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AttributeFulfillmentValue):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((source, value))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
