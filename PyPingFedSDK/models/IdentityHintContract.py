class IdentityHintContract():
    """A set of attributes exposed by request policy contract.

    Attributes
    ----------
    coreAttributes : array
 A list of required identity hint contract attributes.
    extendedAttributes : array
 A list of additional identity hint contract attributes.

    """

    def __init__(self, coreAttributes:list, extendedAttributes:list=None) -> None:
        self.coreAttributes = coreAttributes
        self.extendedAttributes = extendedAttributes

    def _validate(self) -> bool:
        return any(x for x in ["coreAttributes"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, IdentityHintContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.coreAttributes, self.extendedAttributes))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["coreAttributes", "extendedAttributes"]}

        return cls(**valid_data)