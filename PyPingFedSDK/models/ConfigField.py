class ConfigField():
    """A plugin configuration field value.

    Attributes
    ----------
    encryptedValue : string
        For encrypted or hashed fields, this attribute contains the encrypted representation of the field's value, if a value is defined. If you do not want to update the stored value, this attribute should be passed back unchanged.    inherited : boolean
        Whether this field is inherited from its parent instance. If true, the value/encrypted value properties become read-only. The default value is false.    name : string
        The name of the configuration field.    value : string
        The value for the configuration field. For encrypted or hashed fields, GETs will not return this attribute. To update an encrypted or hashed field, specify the new value in this attribute.
    """

    __slots__ = ["encryptedValue", "inherited", "name", "value"]

    def __init__(self, name, encryptedValue=None, inherited=None, value=None):
        self.encryptedValue: str = encryptedValue
        self.inherited: bool = inherited
        self.name: str = name
        self.value: str = value

    def _validate(self):
        return any(x for x in ['name'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ConfigField):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.encryptedValue, self.inherited, self.name, self.value))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["encryptedValue", "inherited", "name", "value"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__