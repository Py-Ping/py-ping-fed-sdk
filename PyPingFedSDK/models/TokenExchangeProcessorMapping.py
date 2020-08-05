class TokenExchangeProcessorMapping():
    """ A Token Processor(s) mapping into an OAuth 2.0 Token Exchange Processor policy.

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

    __slots__ = ["actorTokenProcessor", "actorTokenType", "attributeContractFulfillment", "attributeSources", "issuanceCriteria", "subjectTokenProcessor", "subjectTokenType"]
    def __init__(self, attributeContractFulfillment, subjectTokenType, subjectTokenProcessor, actorTokenProcessor=None, actorTokenType=None, attributeSources=None, issuanceCriteria=None):
            self.actorTokenProcessor = actorTokenProcessor
            self.actorTokenType = actorTokenType
            self.attributeContractFulfillment = attributeContractFulfillment
            self.attributeSources = attributeSources
            self.issuanceCriteria = issuanceCriteria
            self.subjectTokenProcessor = subjectTokenProcessor
            self.subjectTokenType = subjectTokenType
    
    def _validate(self):
        return any(x for x in ['attributeContractFulfillment', 'subjectTokenType', 'subjectTokenProcessor'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, TokenExchangeProcessorMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((actorTokenProcessor, actorTokenType, attributeContractFulfillment, attributeSources, issuanceCriteria, subjectTokenProcessor, subjectTokenType))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
