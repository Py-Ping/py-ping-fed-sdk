class BaseSelectionFieldDescriptor():
    """Holds fields that are shared by all selection-type field descriptors.

    Attributes
    ----------
    advanced : boolean
        Whether this is an advanced field or not.    defaultValue : string
        Default value of the field.    description : string
        Description of the field.    label : string
        Label of the field to be displayed in the administrative console.    name : string
        Name of the field.    optionValues : array
        The list of option values for this selection field.    required : boolean
        Whether a value is required for this field or not.    type : str
        The type of field descriptor.
    """

    __slots__ = ["advanced", "defaultValue", "description", "label", "name", "optionValues", "required", "type"]

    def __init__(self, advanced=None, defaultValue=None, description=None, label=None, name=None, optionValues=None, required=None, type=None):
        self.advanced = advanced
        self.defaultValue = defaultValue
        self.description = description
        self.label = label
        self.name = name
        self.optionValues = optionValues
        self.required = required
        self.type = type

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, BaseSelectionFieldDescriptor):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.advanced, self.defaultValue, self.description, self.label, self.name, self.optionValues, self.required, self.type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["advanced", "defaultValue", "description", "label", "name", "optionValues", "required", "type"]}

        return cls(**valid_data)
