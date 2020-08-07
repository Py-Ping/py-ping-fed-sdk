class AuthenticationSelectorAttributeContract():
    """A set of attributes exposed by an Authentication Selector.

    Attributes
    ----------
    extendedAttributes : array
 A list of additional attributes that can be returned by the Authentication Selector. The extended attributes are only used if the Authentication Selector supports them.

    """

<<<<<<< HEAD
    def __init__(self, extendedAttributes=None) -> None:
        self.extendedAttributes = extendedAttributes
=======
    def __init__(self, extendedAttributes=None):
        self.extendedAttributes: list = extendedAttributes
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthenticationSelectorAttributeContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.extendedAttributes))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["extendedAttributes"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
