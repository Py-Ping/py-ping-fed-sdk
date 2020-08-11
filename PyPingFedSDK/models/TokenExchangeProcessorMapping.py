class TokenExchangeProcessorMapping():
    """A Token Processor(s) mapping into an OAuth 2.0 Token Exchange Processor policy.

    Attributes
    ----------
    actorTokenProcessor : str
        The Token processor used to process the actor token
    actorTokenType : string
        The Actor token type
    attributeContractFulfillment : str
        A list of mappings from attribute names to their fulfillment values.
    attributeSources : array
        A list of configured data stores to look up attributes from.
    issuanceCriteria : str
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.
    subjectTokenProcessor : str
        The Token processor used to process the subject token
    subjectTokenType : string
        The Subject token type

    """

    def __init__(self, attributeContractFulfillment, subjectTokenType:str, subjectTokenProcessor, actorTokenProcessor=None, actorTokenType:str=None, attributeSources:list=None, issuanceCriteria=None) -> None:
        self.actorTokenProcessor = actorTokenProcessor
        self.actorTokenType = actorTokenType
        self.attributeContractFulfillment = attributeContractFulfillment
        self.attributeSources = attributeSources
        self.issuanceCriteria = issuanceCriteria
        self.subjectTokenProcessor = subjectTokenProcessor
        self.subjectTokenType = subjectTokenType

    def _validate(self) -> bool:
        return any(x for x in ["attributeContractFulfillment", "subjectTokenType", "subjectTokenProcessor"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, TokenExchangeProcessorMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.actorTokenProcessor, self.actorTokenType, self.attributeContractFulfillment, self.attributeSources, self.issuanceCriteria, self.subjectTokenProcessor, self.subjectTokenType))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["actorTokenProcessor", "actorTokenType", "attributeContractFulfillment", "attributeSources", "issuanceCriteria", "subjectTokenProcessor", "subjectTokenType"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__