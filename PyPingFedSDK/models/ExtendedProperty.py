class ExtendedProperty():
    """Extended Property definition that allows to store additional information about IdP/SP Connections and OAuth Clients.

    Attributes
    ----------
    description : string
 The property description.
    multiValued : boolean
 Indicates whether the property should allow multiple values.
    name : string
 The property name.

    """

    def __init__(self, description=None, multiValued=None, name=None) -> None:
        self.description = description
        self.multiValued = multiValued
        self.name = name

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ExtendedProperty):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.description, self.multiValued, self.name))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["description", "multiValued", "name"]}

        return cls(**valid_data)