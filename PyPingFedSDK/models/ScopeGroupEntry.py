class ScopeGroupEntry():
    """A scope group name and its description.

    Attributes
    ----------
    description : string
 The description of the scope group.
    name : string
 The name of the scope group.
    scopes : str
 The set of scopes for this scope group.

    """

    def __init__(self, name:str, description:str, scopes) -> None:
        self.description = description
        self.name = name
        self.scopes = scopes

    def _validate(self) -> bool:
        return any(x for x in ["name", "description", "scopes"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ScopeGroupEntry):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.description, self.name, self.scopes))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["description", "name", "scopes"]}

        return cls(**valid_data)