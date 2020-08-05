class SaasPluginFieldOption():
    """ A plugin configuration field value.

    Attributes
    ----------
    code : string
        The code that represents the field.
    label : string
        The label for the field.

    """

    __slots__ = ["code", "label"]
    def __init__(self, code, label):
            self.code = code
            self.label = label
    
    def _validate(self):
        return any(x for x in ['code', 'label'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, SaasPluginFieldOption):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((code, label))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
