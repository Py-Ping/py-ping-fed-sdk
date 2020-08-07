class AuthenticationPolicyContractMapping():
    """An Authentication Policy Contract mapping into IdP Connection.

    Attributes
    ----------
    attributeContractFulfillment : str
        A list of mappings from attribute names to their fulfillment values.    attributeSources : array
        A list of configured data stores to look up attributes from.    authenticationPolicyContractRef : str
        Reference to the associated Authentication Policy Contract.    issuanceCriteria : str
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.    restrictVirtualServerIds : boolean
        Restricts this mapping to specific virtual entity IDs.    restrictedVirtualServerIds : array
        The list of virtual server IDs that this mapping is restricted to.
    """

    __slots__ = ["attributeContractFulfillment", "attributeSources", "authenticationPolicyContractRef", "issuanceCriteria", "restrictVirtualServerIds", "restrictedVirtualServerIds"]

    def __init__(self, authenticationPolicyContractRef, attributeContractFulfillment, attributeSources=None, issuanceCriteria=None, restrictVirtualServerIds=None, restrictedVirtualServerIds=None):
        self.attributeContractFulfillment: str = attributeContractFulfillment
        self.attributeSources: list = attributeSources
        self.authenticationPolicyContractRef: str = authenticationPolicyContractRef
        self.issuanceCriteria: str = issuanceCriteria
        self.restrictVirtualServerIds: bool = restrictVirtualServerIds
        self.restrictedVirtualServerIds: list = restrictedVirtualServerIds

    def _validate(self):
        return any(x for x in ['authenticationPolicyContractRef', 'attributeContractFulfillment'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AuthenticationPolicyContractMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.attributeContractFulfillment, self.attributeSources, self.authenticationPolicyContractRef, self.issuanceCriteria, self.restrictVirtualServerIds, self.restrictedVirtualServerIds))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeContractFulfillment", "attributeSources", "authenticationPolicyContractRef", "issuanceCriteria", "restrictVirtualServerIds", "restrictedVirtualServerIds"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__