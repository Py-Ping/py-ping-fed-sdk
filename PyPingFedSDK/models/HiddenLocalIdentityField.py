class HiddenLocalIdentityField():
    """A hidden selection type field.

    Attributes
    ----------
    attributes : str
 Attributes of the local identity field.
    id : string
 Id of the local identity field.
    label : string
 Label of the local identity field.
    profilePageField : boolean
 Whether this is a profile page field or not.
    registrationPageField : boolean
 Whether this is a registration page field or not.
    type : str
 The type of the local identity field.

    """

    def __init__(self, var_type, var_id, label, attributes=None, profilePageField=None, registrationPageField=None) -> None:
        self.attributes = attributes
        self.var_id = var_id
        self.label = label
        self.profilePageField = profilePageField
        self.registrationPageField = registrationPageField
        self.var_type = var_type

    def _validate(self) -> bool:
        return any(x for x in ["var_type", "var_id", "label"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, HiddenLocalIdentityField):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.attributes, self.var_id, self.label, self.profilePageField, self.registrationPageField, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributes", "var_id", "label", "profilePageField", "registrationPageField", "var_type"]}

        return cls(**valid_data)