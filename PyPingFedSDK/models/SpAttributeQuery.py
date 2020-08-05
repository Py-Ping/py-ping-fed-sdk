class SpAttributeQuery():
    """ The attribute query profile supports SPs in requesting user attributes.

    Attributes
    ----------
    attributeContractFulfillment : str
        A list of mappings from attribute names to their fulfillment values.
    attributeSources : array
        A list of configured data stores to look up attributes from.
    attributes : str
        The list of attributes that may be returned to the SP in the response to an attribute request.
    issuanceCriteria : str
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.
    policy : str
        The attribute query profile's security policy.

    """

    __slots__ = ["attributeContractFulfillment", "attributeSources", "attributes", "issuanceCriteria", "policy"]
    def __init__(self, attributes, attributeSources, attributeContractFulfillment, issuanceCriteria=None, policy=None):
            self.attributeContractFulfillment = attributeContractFulfillment
            self.attributeSources = attributeSources
            self.attributes = attributes
            self.issuanceCriteria = issuanceCriteria
            self.policy = policy
    
    def _validate(self):
        return any(x for x in ['attributes', 'attributeSources', 'attributeContractFulfillment'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, SpAttributeQuery):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((attributeContractFulfillment, attributeSources, attributes, issuanceCriteria, policy))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
