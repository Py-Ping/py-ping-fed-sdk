class FieldEntry():
    """A simple name value pair to represent a field entry.

    Attributes
    ----------
    name : string
 The name of this field.
    value : string
 The value of this field. Whether or not the value is required will be determined by plugin validation checks.

    """

<<<<<<< HEAD
    def __init__(self, name, value=None) -> None:
        self.name = name
        self.value = value
=======
    def __init__(self, name, value=None):
        self.name: str = name
        self.value: str = value
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["name"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, FieldEntry):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.name, self.value))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["name", "value"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
