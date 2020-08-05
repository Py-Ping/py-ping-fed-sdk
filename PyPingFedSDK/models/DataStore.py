class DataStore():
    """ The set of attributes used to configure a data store.

    Attributes
    ----------
    id : string
        The persistent, unique ID for the data store. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.
    maskAttributeValues : boolean
        Whether attribute values should be masked in the log.
    type : str
        The data store type.

    """

    __slots__ = ["id", "maskAttributeValues", "type"]
    def __init__(self, type, id=None, maskAttributeValues=None):
            self.id = id
            self.maskAttributeValues = maskAttributeValues
            self.type = type
    
    def _validate(self):
        return any(x for x in ['type'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, DataStore):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((id, maskAttributeValues, type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
