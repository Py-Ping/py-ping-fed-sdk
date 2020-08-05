class FieldEntry():
    """ A simple name value pair to represent a field entry.

    Attributes
    ----------
    name : string
        The name of this field.
    value : string
        The value of this field. Whether or not the value is required will be determined by plugin validation checks.

    """

    __slots__ = ["name", "value"]
    def __init__(self, name, value=None):
            self.name = name
            self.value = value
    
    def _validate(self):
        return any(x for x in ['name'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, FieldEntry):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((name, value))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
