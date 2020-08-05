class IdpAdapterContractMapping():
    """ 

    Attributes
    ----------
    attributeContractFulfillment : str
        A list of mappings from attribute names to their fulfillment values.
    attributeSources : array
        A list of configured data stores to look up attributes from.
    inherited : boolean
        Whether this attribute mapping is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false.
    issuanceCriteria : str
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.

    """

    __slots__ = ["attributeContractFulfillment", "attributeSources", "inherited", "issuanceCriteria"]
    def __init__(self, attributeContractFulfillment, attributeSources=None, inherited=None, issuanceCriteria=None):
            self.attributeContractFulfillment = attributeContractFulfillment
            self.attributeSources = attributeSources
            self.inherited = inherited
            self.issuanceCriteria = issuanceCriteria
    
    def _validate(self):
        return any(x for x in ['attributeContractFulfillment'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, IdpAdapterContractMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((attributeContractFulfillment, attributeSources, inherited, issuanceCriteria))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
