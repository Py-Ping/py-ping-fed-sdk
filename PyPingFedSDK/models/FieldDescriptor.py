class FieldDescriptor():
    """Describes a plugin configuration field.

    Attributes
    ----------
    advanced : boolean
 Whether this is an advanced field or not.
    defaultValue : string
 Default value of the field.
    description : string
 Description of the field.
    label : string
 Label of the field to be displayed in the administrative console.
    name : string
 Name of the field.
    required : boolean
 Whether a value is required for this field or not.
    type : str
 The type of field descriptor.

    """

<<<<<<< HEAD
    def __init__(self, advanced=None, defaultValue=None, description=None, label=None, name=None, required=None, var_type=None) -> None:
        self.advanced = advanced
        self.defaultValue = defaultValue
        self.description = description
        self.label = label
        self.name = name
        self.required = required
        self.var_type = var_type
=======
    def __init__(self, advanced=None, defaultValue=None, description=None, label=None, name=None, required=None, type=None):
        self.advanced: bool = advanced
        self.defaultValue: str = defaultValue
        self.description: str = description
        self.label: str = label
        self.name: str = name
        self.required: bool = required
        self.type: str = type
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, FieldDescriptor):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.advanced, self.defaultValue, self.description, self.label, self.name, self.required, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["advanced", "defaultValue", "description", "label", "name", "required", "var_type"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
