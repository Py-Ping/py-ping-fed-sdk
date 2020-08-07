class AttributeRules():
    """A collection of attribute rules

    Attributes
    ----------
    fallbackToSuccess : boolean
 When all the rules fail, you may choose to default to the general success action or fail. Default to success.
    items : array
 The actual list of attribute rules.

    """

<<<<<<< HEAD
    def __init__(self, fallbackToSuccess=None, items=None) -> None:
        self.fallbackToSuccess = fallbackToSuccess
        self.items = items
=======
    def __init__(self, fallbackToSuccess=None, items=None):
        self.fallbackToSuccess: bool = fallbackToSuccess
        self.items: list = items
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AttributeRules):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.fallbackToSuccess, self.items))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["fallbackToSuccess", "items"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
