class ClientMetadata():
    """The client metadata.

    Attributes
    ----------
    description : string
 The metadata description.
    multiValued : boolean
 If the field should allow multiple values.
    parameter : string
 The metadata name.

    """

    def __init__(self, description=None, multiValued=None, parameter=None) -> None:
        self.description = description
        self.multiValued = multiValued
        self.parameter = parameter

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ClientMetadata):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.description, self.multiValued, self.parameter))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["description", "multiValued", "parameter"]}

        return cls(**valid_data)