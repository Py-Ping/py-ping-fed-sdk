class SaasAttributeMapping():
    """Settings to map the source record attributes to target attributes.

    Attributes
    ----------
    fieldName : string
 The name of target field.
    saasFieldInfo : str
 The settings that represent how attribute values from source data store will be mapped into Fields specified by the service provider.

    """

<<<<<<< HEAD
    def __init__(self, fieldName, saasFieldInfo) -> None:
        self.fieldName = fieldName
        self.saasFieldInfo = saasFieldInfo
=======
    def __init__(self, fieldName, saasFieldInfo):
        self.fieldName: str = fieldName
        self.saasFieldInfo: str = saasFieldInfo
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["fieldName", "saasFieldInfo"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SaasAttributeMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.fieldName, self.saasFieldInfo))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["fieldName", "saasFieldInfo"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
