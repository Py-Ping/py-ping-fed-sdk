class TokenProcessorAttributeContract():
    """A set of attributes exposed by a token processor.

    Attributes
    ----------
    coreAttributes : array
        A list of token processor attributes that correspond to the attributes exposed by the token processor type.
    extendedAttributes : array
        A list of additional attributes that can be returned by the token processor. The extended attributes are only used if the token processor supports them.
    inherited : boolean
        Whether this attribute contract is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false.
    maskOgnlValues : boolean
        Whether or not all OGNL expressions used to fulfill an outgoing assertion contract should be masked in the logs. Defaults to false.

    """

    def __init__(self, coreAttributes:list, extendedAttributes:list=None, inherited:bool=None, maskOgnlValues:bool=None) -> None:
        self.coreAttributes = coreAttributes
        self.extendedAttributes = extendedAttributes
        self.inherited = inherited
        self.maskOgnlValues = maskOgnlValues

    def _validate(self) -> bool:
        return any(x for x in ["coreAttributes"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, TokenProcessorAttributeContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.coreAttributes, self.extendedAttributes, self.inherited, self.maskOgnlValues]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["coreAttributes", "extendedAttributes", "inherited", "maskOgnlValues"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__