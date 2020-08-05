class TokenExchangeGeneratorGroup():
    """ The set of attributes used to configure a OAuth 2.0 Token Exchange Generator group.

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

    __slots__ = ["generatorMappings", "id", "name", "resourceUris"]
    def __init__(self, id, name, generatorMappings, resourceUris=None):
            self.generatorMappings = generatorMappings
            self.id = id
            self.name = name
            self.resourceUris = resourceUris
    
    def _validate(self):
        return any(x for x in ['id', 'name', 'generatorMappings'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, TokenExchangeGeneratorGroup):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((generatorMappings, id, name, resourceUris))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
