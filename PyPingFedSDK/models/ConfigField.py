class ConfigField():
    """A plugin configuration field value.

    Attributes
    ----------
    encryptedValue : string
        For encrypted or hashed fields, this attribute contains the encrypted representation of the field's value, if a value is defined. If you do not want to update the stored value, this attribute should be passed back unchanged.
    inherited : boolean
        Whether this field is inherited from its parent instance. If true, the value/encrypted value properties become read-only. The default value is false.
    name : string
        The name of the configuration field.
    value : string
        The value for the configuration field. For encrypted or hashed fields, GETs will not return this attribute. To update an encrypted or hashed field, specify the new value in this attribute.

    """

    def __init__(self, name:str, encryptedValue:str=None, inherited:bool=None, value:str=None) -> None:
        self.encryptedValue = encryptedValue
        self.inherited = inherited
        self.name = name
        self.value = value

    def _validate(self) -> bool:
        return any(x for x in ["name"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ConfigField):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.encryptedValue, self.inherited, self.name, self.value))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["encryptedValue", "inherited", "name", "value"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__