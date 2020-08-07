class TokenExchangeGeneratorSettings():
    """Settings for the OAuth Token Exchange Generator Groups.

    Attributes
    ----------
    defaultGeneratorGroupRef : str
        Reference to the default Token Exchange Generator group, if one is defined.
    """

    __slots__ = ["defaultGeneratorGroupRef"]

    def __init__(self, defaultGeneratorGroupRef=None):
        self.defaultGeneratorGroupRef: str = defaultGeneratorGroupRef

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, TokenExchangeGeneratorSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.defaultGeneratorGroupRef))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["defaultGeneratorGroupRef"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__