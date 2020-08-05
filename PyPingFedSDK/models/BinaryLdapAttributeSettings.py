class BinaryLdapAttributeSettings():
    """ Binary settings for a LDAP attribute.

    Attributes
    ----------
    binaryEncoding : str
        Get the encoding type for this attribute. If not specified, the default is BASE64.

    """

    __slots__ = ["binaryEncoding"]
    def __init__(self, binaryEncoding=None):
            self.binaryEncoding = binaryEncoding
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, BinaryLdapAttributeSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((binaryEncoding))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
