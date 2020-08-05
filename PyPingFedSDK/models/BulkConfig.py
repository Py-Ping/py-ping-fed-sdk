class BulkConfig():
    """ Model describing a series of configuration operations.

    Attributes
    ----------
    metadata : str
        The metadata detailing how this config was generated.
    operations : array
        A list of configuration operations.

    """

    __slots__ = ["metadata", "operations"]
    def __init__(self, metadata, operations):
            self.metadata = metadata
            self.operations = operations
    
    def _validate(self):
        return any(x for x in ['metadata', 'operations'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, BulkConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((metadata, operations))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
