class PersistentGrantContract():
    """

    Attributes
    ----------
    coreAttributes : array
        This is a read-only list of persistent grant attributes and includes USER_KEY and USER_NAME. Changes to this field will be ignored.    extendedAttributes : array
        A list of additional attributes for the persistent grant contract.
    """

    __slots__ = ["coreAttributes", "extendedAttributes"]

    def __init__(self, coreAttributes, extendedAttributes=None):
        self.coreAttributes: list = coreAttributes
        self.extendedAttributes: list = extendedAttributes

    def _validate(self):
        return any(x for x in ['coreAttributes'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, PersistentGrantContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.coreAttributes, self.extendedAttributes))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["coreAttributes", "extendedAttributes"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__