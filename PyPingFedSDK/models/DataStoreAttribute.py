class DataStoreAttribute():
    """ The data store attribute.

    Attributes
    ----------
    metadata : str
        The data store attribute metadata.
    name : string
        The data store attribute name.
    type : str
        The data store attribute type.

    """

    __slots__ = ["metadata", "name", "type"]
    def __init__(self, type, name, metadata=None):
            self.metadata = metadata
            self.name = name
            self.type = type
    
    def _validate(self):
        return any(x for x in ['type', 'name'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, DataStoreAttribute):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((metadata, name, type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
