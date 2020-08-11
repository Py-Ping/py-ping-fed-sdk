class TokenGeneratorAttribute():
    """An attribute for the token generator attribute contract.

    Attributes
    ----------
    name : string
 The name of this attribute.

    """

    def __init__(self, name:str) -> None:
        self.name = name

    def _validate(self) -> bool:
        return any(x for x in ["name"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, TokenGeneratorAttribute):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.name))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["name"]}

        return cls(**valid_data)