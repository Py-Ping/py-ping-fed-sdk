class TokenExchangeGeneratorGroup():
    """The set of attributes used to configure a OAuth 2.0 Token Exchange Generator group.

    Attributes
    ----------
    generatorMappings : array
 A list of Token Generator mapping into an OAuth 2.0 Token Exchange requested token type.
    id : string
 The Token Exchange Generator group ID. ID is unique.
    name : string
 The Token Exchange Generator group name. Name is unique.
    resourceUris : array
 The list of  resource URI's which map to this Token Exchange Generator group.

    """

<<<<<<< HEAD
    def __init__(self, var_id, name, generatorMappings, resourceUris=None) -> None:
        self.generatorMappings = generatorMappings
        self.var_id = var_id
        self.name = name
        self.resourceUris = resourceUris
=======
    def __init__(self, id, name, generatorMappings, resourceUris=None):
        self.generatorMappings: list = generatorMappings
        self.id: str = id
        self.name: str = name
        self.resourceUris: list = resourceUris
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["var_id", "name", "generatorMappings"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, TokenExchangeGeneratorGroup):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.generatorMappings, self.var_id, self.name, self.resourceUris))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["generatorMappings", "var_id", "name", "resourceUris"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
