class SaasPluginFieldOption():
    """A plugin configuration field value.

    Attributes
    ----------
    code : string
 The code that represents the field.
    label : string
 The label for the field.

    """

<<<<<<< HEAD
    def __init__(self, code, label) -> None:
        self.code = code
        self.label = label
=======
    def __init__(self, code, label):
        self.code: str = code
        self.label: str = label
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["code", "label"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SaasPluginFieldOption):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.code, self.label))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["code", "label"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
