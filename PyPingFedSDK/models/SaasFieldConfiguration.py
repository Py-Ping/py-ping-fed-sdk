class SaasFieldConfiguration():
    """The settings that represent how attribute values from source data store will be mapped into Fields specified by the service provider.

    Attributes
    ----------
    attributeNames : str
 The list of source attribute names used to generate or map to a target field
    characterCase : str
 The character case of the field value.
    createOnly : boolean
 Indicates whether this field is a create only field and cannot be updated.
    defaultValue : string
 The default value for the target field
    expression : string
 An OGNL expression to obtain a value.
    masked : boolean
 Indicates whether the attribute should be masked in server logs.
    parser : str
 Indicates how the field shall be parsed.
    trim : boolean
 Indicates whether field should be trimmed before provisioning.

    """

<<<<<<< HEAD
    def __init__(self, attributeNames=None, characterCase=None, createOnly=None, defaultValue=None, expression=None, masked=None, parser=None, trim=None) -> None:
        self.attributeNames = attributeNames
        self.characterCase = characterCase
        self.createOnly = createOnly
        self.defaultValue = defaultValue
        self.expression = expression
        self.masked = masked
        self.parser = parser
        self.trim = trim
=======
    def __init__(self, attributeNames=None, characterCase=None, createOnly=None, defaultValue=None, expression=None, masked=None, parser=None, trim=None):
        self.attributeNames: str = attributeNames
        self.characterCase: str = characterCase
        self.createOnly: bool = createOnly
        self.defaultValue: str = defaultValue
        self.expression: str = expression
        self.masked: bool = masked
        self.parser: str = parser
        self.trim: bool = trim
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SaasFieldConfiguration):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.attributeNames, self.characterCase, self.createOnly, self.defaultValue, self.expression, self.masked, self.parser, self.trim))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeNames", "characterCase", "createOnly", "defaultValue", "expression", "masked", "parser", "trim"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
