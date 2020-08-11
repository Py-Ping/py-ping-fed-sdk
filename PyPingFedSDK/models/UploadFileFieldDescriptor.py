class UploadFileFieldDescriptor():
    """A field which allows the user to upload a file.

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

    def __init__(self, advanced:bool=None, defaultValue:str=None, description:str=None, label:str=None, name:str=None, required:bool=None, var_type=None) -> None:
        self.advanced = advanced
        self.defaultValue = defaultValue
        self.description = description
        self.label = label
        self.name = name
        self.required = required
        self.var_type = var_type

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, UploadFileFieldDescriptor):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.advanced, self.defaultValue, self.description, self.label, self.name, self.required, self.var_type]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["advanced", "defaultValue", "description", "label", "name", "required", "var_type"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__