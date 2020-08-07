class AuthenticationSelectorAttributeContract():
    """A set of attributes exposed by an Authentication Selector.

    Attributes
    ----------
    extendedAttributes : array
        A list of additional attributes that can be returned by the Authentication Selector. The extended attributes are only used if the Authentication Selector supports them.
    """

    __slots__ = ["extendedAttributes"]

    def __init__(self, extendedAttributes=None):
        self.extendedAttributes: list = extendedAttributes

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AuthenticationSelectorAttributeContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.extendedAttributes))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["extendedAttributes"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__