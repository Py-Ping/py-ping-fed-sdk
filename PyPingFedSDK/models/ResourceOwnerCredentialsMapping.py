class ResourceOwnerCredentialsMapping():
    """ The OAuth Resource Owner Credentials Mapping.

    Attributes
    ----------
    attributeContractFulfillment : str
        A list of mappings from attribute names to their fulfillment values.
    attributeSources : array
        A list of configured data stores to look up attributes from.
    id : string
        The ID of the Resource Owner Credentials Mapping.
    issuanceCriteria : str
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.
    passwordValidatorRef : str
        Read only reference to the associated Source Password Validator Instance.

    """

    __slots__ = ["attributeContractFulfillment", "attributeSources", "id", "issuanceCriteria", "passwordValidatorRef"]
    def __init__(self, id, attributeContractFulfillment, attributeSources=None, issuanceCriteria=None, passwordValidatorRef=None):
            self.attributeContractFulfillment = attributeContractFulfillment
            self.attributeSources = attributeSources
            self.id = id
            self.issuanceCriteria = issuanceCriteria
            self.passwordValidatorRef = passwordValidatorRef
    
    def _validate(self):
        return any(x for x in ['id', 'attributeContractFulfillment'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ResourceOwnerCredentialsMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((attributeContractFulfillment, attributeSources, id, issuanceCriteria, passwordValidatorRef))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
