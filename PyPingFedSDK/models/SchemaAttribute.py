class SchemaAttribute():
    """ A custom SCIM attribute.

    Attributes
    ----------
    multiValued : boolean
        Indicates whether the attribute is multi-valued.
    name : string
        Name of the attribute.
    subAttributes : array
        List of sub-attributes for an attribute.
    types : array
        Represents the name of each attribute type in case of multi-valued attribute.

    """

    __slots__ = ["multiValued", "name", "subAttributes", "types"]
    def __init__(self, multiValued=None, name=None, subAttributes=None, types=None):
            self.multiValued = multiValued
            self.name = name
            self.subAttributes = subAttributes
            self.types = types
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, SchemaAttribute):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((multiValued, name, subAttributes, types))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
