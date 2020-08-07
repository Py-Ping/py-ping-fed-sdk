class ScopeEntry():
    """A scope name and its description.

    Attributes
    ----------
    description : string
 The description of the scope that appears when the user is prompted for authorization.
    dynamic : boolean
 True if the scope is dynamic. (Defaults to false)
    name : string
 The name of the scope.

    """

    def __init__(self, name, description, dynamic=None) -> None:
        self.description = description
        self.dynamic = dynamic
        self.name = name

    def _validate(self) -> bool:
        return any(x for x in ["name", "description"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ScopeEntry):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.description, self.dynamic, self.name))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["description", "dynamic", "name"]}

        return cls(**valid_data)