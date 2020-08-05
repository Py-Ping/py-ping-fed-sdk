class PersistentGrantContract():
    """ 

    Attributes
    ----------
    coreAttributes : array
        This is a read-only list of persistent grant attributes and includes USER_KEY and USER_NAME. Changes to this field will be ignored.
    extendedAttributes : array
        A list of additional attributes for the persistent grant contract.

    """

    __slots__ = ["coreAttributes", "extendedAttributes"]
    def __init__(self, coreAttributes, extendedAttributes=None):
            self.coreAttributes = coreAttributes
            self.extendedAttributes = extendedAttributes
    
    def _validate(self):
        return any(x for x in ['coreAttributes'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, PersistentGrantContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((coreAttributes, extendedAttributes))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
