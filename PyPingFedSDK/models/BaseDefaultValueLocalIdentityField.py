class BaseDefaultValueLocalIdentityField():
    """Holds fields that are shared by all default value type fields.

    Attributes
    ----------
    attributes : str
 Attributes of the local identity field.
    defaultValue : string
 The default value for this field.
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

<<<<<<< HEAD
    def __init__(self, var_type, var_id, label, attributes=None, defaultValue=None, profilePageField=None, registrationPageField=None) -> None:
        self.attributes = attributes
        self.defaultValue = defaultValue
        self.var_id = var_id
        self.label = label
        self.profilePageField = profilePageField
        self.registrationPageField = registrationPageField
        self.var_type = var_type
=======
    def __init__(self, type, id, label, attributes=None, defaultValue=None, profilePageField=None, registrationPageField=None):
        self.attributes: str = attributes
        self.defaultValue: str = defaultValue
        self.id: str = id
        self.label: str = label
        self.profilePageField: bool = profilePageField
        self.registrationPageField: bool = registrationPageField
        self.type: str = type
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["var_type", "var_id", "label"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, BaseDefaultValueLocalIdentityField):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.attributes, self.defaultValue, self.var_id, self.label, self.profilePageField, self.registrationPageField, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributes", "defaultValue", "var_id", "label", "profilePageField", "registrationPageField", "var_type"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
