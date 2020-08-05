class IdpAdapterAttribute():
    """ An attribute for the IdP adapter attribute contract.

    Attributes
    ----------
    masked : boolean
        Specifies whether this attribute is masked in PingFederate logs. Defaults to false.
    name : string
        The name of this attribute.
    pseudonym : boolean
        Specifies whether this attribute is used to construct a pseudonym for the SP. Defaults to false.

    """

    __slots__ = ["masked", "name", "pseudonym"]
    def __init__(self, name, masked=None, pseudonym=None):
            self.masked = masked
            self.name = name
            self.pseudonym = pseudonym
    
    def _validate(self):
        return any(x for x in ['name'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, IdpAdapterAttribute):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((masked, name, pseudonym))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
