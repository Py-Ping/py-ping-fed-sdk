class IdpAdapterAttributeContract():
    """ A set of attributes exposed by an IdP adapter.

    Attributes
    ----------
    coreAttributes : array
        A list of IdP adapter attributes that correspond to the attributes exposed by the IdP adapter type.
    extendedAttributes : array
        A list of additional attributes that can be returned by the IdP adapter. The extended attributes are only used if the adapter supports them.
    inherited : boolean
        Whether this attribute contract is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false.
    maskOgnlValues : boolean
        Whether or not all OGNL expressions used to fulfill an outgoing assertion contract should be masked in the logs. Defaults to false.

    """

    __slots__ = ["coreAttributes", "extendedAttributes", "inherited", "maskOgnlValues"]
    def __init__(self, coreAttributes, extendedAttributes=None, inherited=None, maskOgnlValues=None):
            self.coreAttributes = coreAttributes
            self.extendedAttributes = extendedAttributes
            self.inherited = inherited
            self.maskOgnlValues = maskOgnlValues
    
    def _validate(self):
        return any(x for x in ['coreAttributes'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, IdpAdapterAttributeContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((coreAttributes, extendedAttributes, inherited, maskOgnlValues))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
