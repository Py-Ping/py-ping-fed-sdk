class TokenExchangeProcessorAttributeContract():
    """A set of attributes exposed by an OAuth 2.0 Token Exchange Processor policy.

    Attributes
    ----------
    coreAttributes : array
 A list of read-only attributes (for example, subject) that are automatically populated by PingFederate.
    extendedAttributes : array
 A list of additional attributes.

    """

<<<<<<< HEAD
    def __init__(self, coreAttributes=None, extendedAttributes=None) -> None:
        self.coreAttributes = coreAttributes
        self.extendedAttributes = extendedAttributes
=======
    def __init__(self, coreAttributes=None, extendedAttributes=None):
        self.coreAttributes: list = coreAttributes
        self.extendedAttributes: list = extendedAttributes
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, TokenExchangeProcessorAttributeContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.coreAttributes, self.extendedAttributes))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["coreAttributes", "extendedAttributes"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
