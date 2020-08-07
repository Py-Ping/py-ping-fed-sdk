class SchemaAttribute():
    """A custom SCIM attribute.

    Attributes
    ----------
    multiValued : boolean
 Indicates whether the attribute is multi-valued.
    name : string
 Name of the attribute.
    subAttributes : array
 List of sub-attributes for an attribute.
    types : array
 Represents the name of each attribute type in case of multi-valued attribute.

    """

    def __init__(self, multiValued=None, name=None, subAttributes=None, types=None) -> None:
        self.multiValued = multiValued
        self.name = name
        self.subAttributes = subAttributes
        self.types = types

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SchemaAttribute):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.multiValued, self.name, self.subAttributes, self.types))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["multiValued", "name", "subAttributes", "types"]}

        return cls(**valid_data)