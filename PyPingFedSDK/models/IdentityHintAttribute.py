class IdentityHintAttribute():
    """An attribute for the ciba request policy's identity hint attribute contract.

    Attributes
    ----------
    name : string
 The name of this attribute.

    """

<<<<<<< HEAD
    def __init__(self, name) -> None:
        self.name = name
=======
    def __init__(self, name):
        self.name: str = name
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["name"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, IdentityHintAttribute):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.name))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["name"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
