class Entity():
    """

    Attributes
    ----------
    entityDescription : string
 Entity description.
    entityId : string
 Unique entity identifier.

    """

    def __init__(self, entityDescription=None, entityId=None) -> None:
        self.entityDescription = entityDescription
        self.entityId = entityId

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Entity):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.entityDescription, self.entityId))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["entityDescription", "entityId"]}

        return cls(**valid_data)