class TokenExchangeProcessorPolicy():
    """ The set of attributes used to configure a OAuth 2.0 Token Exchange processor policy.

    Attributes
    ----------
    actorTokenRequired : boolean
        Require an Actor token on a OAuth 2.0 Token Exchange request.
    attributeContract : str
        A set of attributes exposed by an OAuth 2.0 Token Exchange Processor policy.
    id : string
        The Token Exchange processor policy ID. ID is unique.
    name : string
        The Token Exchange processor policy name. Name is unique.
    processorMappings : array
        A list of Token Processor(s) mappings into an OAuth 2.0 Token Exchange Processor policy.

    """

    __slots__ = ["actorTokenRequired", "attributeContract", "id", "name", "processorMappings"]
    def __init__(self, id, name, processorMappings, attributeContract, actorTokenRequired=None):
            self.actorTokenRequired = actorTokenRequired
            self.attributeContract = attributeContract
            self.id = id
            self.name = name
            self.processorMappings = processorMappings
    
    def _validate(self):
        return any(x for x in ['id', 'name', 'processorMappings', 'attributeContract'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, TokenExchangeProcessorPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((actorTokenRequired, attributeContract, id, name, processorMappings))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
