class TokenExchangeProcessorMapping():
    """A Token Processor(s) mapping into an OAuth 2.0 Token Exchange Processor policy.

    Attributes
    ----------
    actorTokenProcessor : str
        The Token processor used to process the actor token    actorTokenType : string
        The Actor token type    attributeContractFulfillment : str
        A list of mappings from attribute names to their fulfillment values.    attributeSources : array
        A list of configured data stores to look up attributes from.    issuanceCriteria : str
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.    subjectTokenProcessor : str
        The Token processor used to process the subject token    subjectTokenType : string
        The Subject token type
    """

    __slots__ = ["actorTokenProcessor", "actorTokenType", "attributeContractFulfillment", "attributeSources", "issuanceCriteria", "subjectTokenProcessor", "subjectTokenType"]

    def __init__(self, attributeContractFulfillment, subjectTokenType, subjectTokenProcessor, actorTokenProcessor=None, actorTokenType=None, attributeSources=None, issuanceCriteria=None):
        self.actorTokenProcessor: str = actorTokenProcessor
        self.actorTokenType: str = actorTokenType
        self.attributeContractFulfillment: str = attributeContractFulfillment
        self.attributeSources: list = attributeSources
        self.issuanceCriteria: str = issuanceCriteria
        self.subjectTokenProcessor: str = subjectTokenProcessor
        self.subjectTokenType: str = subjectTokenType

    def _validate(self):
        return any(x for x in ['attributeContractFulfillment', 'subjectTokenType', 'subjectTokenProcessor'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, TokenExchangeProcessorMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.actorTokenProcessor, self.actorTokenType, self.attributeContractFulfillment, self.attributeSources, self.issuanceCriteria, self.subjectTokenProcessor, self.subjectTokenType))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["actorTokenProcessor", "actorTokenType", "attributeContractFulfillment", "attributeSources", "issuanceCriteria", "subjectTokenProcessor", "subjectTokenType"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__