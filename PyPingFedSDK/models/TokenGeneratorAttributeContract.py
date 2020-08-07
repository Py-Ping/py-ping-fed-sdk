class TokenGeneratorAttributeContract():
    """A set of attributes exposed by a token generator.

    Attributes
    ----------
    coreAttributes : array
 A list of token generator attributes that correspond to the attributes exposed by the token generator type.
    extendedAttributes : array
 A list of additional attributes that can be returned by the token processor. The extended attributes are only used if the token generator supports them.
    inherited : boolean
 Whether this attribute contract is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false.

    """

    def __init__(self, coreAttributes, extendedAttributes=None, inherited=None) -> None:
        self.coreAttributes = coreAttributes
        self.extendedAttributes = extendedAttributes
        self.inherited = inherited

    def _validate(self) -> bool:
        return any(x for x in ["coreAttributes"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, TokenGeneratorAttributeContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.coreAttributes, self.extendedAttributes, self.inherited))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["coreAttributes", "extendedAttributes", "inherited"]}

        return cls(**valid_data)