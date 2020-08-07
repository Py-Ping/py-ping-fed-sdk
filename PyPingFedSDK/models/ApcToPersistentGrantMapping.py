class ApcToPersistentGrantMapping():
    """An authentication policy contract mapping into an OAuth persistent grant.

    Attributes
    ----------
    attributeContractFulfillment : str
        A list of mappings from attribute names to their fulfillment values.    attributeSources : array
        A list of configured data stores to look up attributes from.    authenticationPolicyContractRef : str
        Reference to the associated authentication policy contract. The reference cannot be changed after the mapping has been created.    id : string
        The ID of the authentication policy contract to persistent grant mapping.    issuanceCriteria : str
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.
    """

    __slots__ = ["attributeContractFulfillment", "attributeSources", "authenticationPolicyContractRef", "id", "issuanceCriteria"]

    def __init__(self, id, authenticationPolicyContractRef, attributeContractFulfillment, attributeSources=None, issuanceCriteria=None):
        self.attributeContractFulfillment: str = attributeContractFulfillment
        self.attributeSources: list = attributeSources
        self.authenticationPolicyContractRef: str = authenticationPolicyContractRef
        self.id: str = id
        self.issuanceCriteria: str = issuanceCriteria

    def _validate(self):
        return any(x for x in ['id', 'authenticationPolicyContractRef', 'attributeContractFulfillment'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ApcToPersistentGrantMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.attributeContractFulfillment, self.attributeSources, self.authenticationPolicyContractRef, self.id, self.issuanceCriteria))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeContractFulfillment", "attributeSources", "authenticationPolicyContractRef", "id", "issuanceCriteria"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__