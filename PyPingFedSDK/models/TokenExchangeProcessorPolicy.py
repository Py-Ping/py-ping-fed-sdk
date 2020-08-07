class TokenExchangeProcessorPolicy():
    """The set of attributes used to configure a OAuth 2.0 Token Exchange processor policy.

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

<<<<<<< HEAD
    def __init__(self, var_id, name, processorMappings, attributeContract, actorTokenRequired=None) -> None:
        self.actorTokenRequired = actorTokenRequired
        self.attributeContract = attributeContract
        self.var_id = var_id
        self.name = name
        self.processorMappings = processorMappings
=======
    def __init__(self, id, name, processorMappings, attributeContract, actorTokenRequired=None):
        self.actorTokenRequired: bool = actorTokenRequired
        self.attributeContract: str = attributeContract
        self.id: str = id
        self.name: str = name
        self.processorMappings: list = processorMappings
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["var_id", "name", "processorMappings", "attributeContract"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, TokenExchangeProcessorPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.actorTokenRequired, self.attributeContract, self.var_id, self.name, self.processorMappings))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["actorTokenRequired", "attributeContract", "var_id", "name", "processorMappings"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
