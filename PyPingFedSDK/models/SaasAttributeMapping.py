class SaasAttributeMapping():
    """ Settings to map the source record attributes to target attributes.

    Attributes
    ----------
    fieldName : string
        The name of target field.
    saasFieldInfo : str
        The settings that represent how attribute values from source data store will be mapped into Fields specified by the service provider.

    """

    __slots__ = ["fieldName", "saasFieldInfo"]
    def __init__(self, fieldName, saasFieldInfo):
            self.fieldName = fieldName
            self.saasFieldInfo = saasFieldInfo
    
    def _validate(self):
        return any(x for x in ['fieldName', 'saasFieldInfo'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, SaasAttributeMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((fieldName, saasFieldInfo))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
