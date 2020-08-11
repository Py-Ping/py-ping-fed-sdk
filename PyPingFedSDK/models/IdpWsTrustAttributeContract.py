class IdpWsTrustAttributeContract():
    """A set of user attributes that this server will receive in the token.

    Attributes
    ----------
    coreAttributes : array
 A list of read-only assertion attributes that are automatically populated by PingFederate.
    extendedAttributes : array
 A list of additional attributes that are receive in the incoming assertion.

    """

    def __init__(self, coreAttributes:list=None, extendedAttributes:list=None) -> None:
        self.coreAttributes = coreAttributes
        self.extendedAttributes = extendedAttributes

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpWsTrustAttributeContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.coreAttributes, self.extendedAttributes))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["coreAttributes", "extendedAttributes"]}

        return cls(**valid_data)