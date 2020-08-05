class FieldConfig():
    """ A local identity profile field configuration.

    Attributes
    ----------
    fields : array
        The field configuration for the local identity profile.

    """

    __slots__ = ["fields"]
    def __init__(self, fields=None):
            self.fields = fields
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, FieldConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((fields))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
