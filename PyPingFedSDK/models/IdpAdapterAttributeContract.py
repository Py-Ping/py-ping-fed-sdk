class IdpAdapterAttributeContract():
    """A set of attributes exposed by an IdP adapter.

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

<<<<<<< HEAD
    def __init__(self, coreAttributes, extendedAttributes=None, inherited=None, maskOgnlValues=None) -> None:
        self.coreAttributes = coreAttributes
        self.extendedAttributes = extendedAttributes
        self.inherited = inherited
        self.maskOgnlValues = maskOgnlValues
=======
    def __init__(self, coreAttributes, extendedAttributes=None, inherited=None, maskOgnlValues=None):
        self.coreAttributes: list = coreAttributes
        self.extendedAttributes: list = extendedAttributes
        self.inherited: bool = inherited
        self.maskOgnlValues: bool = maskOgnlValues
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["coreAttributes"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpAdapterAttributeContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.coreAttributes, self.extendedAttributes, self.inherited, self.maskOgnlValues))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["coreAttributes", "extendedAttributes", "inherited", "maskOgnlValues"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
