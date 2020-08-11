class AuthenticationPolicyContractMapping():
    """An Authentication Policy Contract mapping into IdP Connection.

    Attributes
    ----------
    attributeContractFulfillment : str
 A list of mappings from attribute names to their fulfillment values.
    attributeSources : array
 A list of configured data stores to look up attributes from.
    authenticationPolicyContractRef : str
 Reference to the associated Authentication Policy Contract.
    issuanceCriteria : str
 The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.
    restrictVirtualServerIds : boolean
 Restricts this mapping to specific virtual entity IDs.
    restrictedVirtualServerIds : array
 The list of virtual server IDs that this mapping is restricted to.

    """

    def __init__(self, authenticationPolicyContractRef, attributeContractFulfillment, attributeSources:list=None, issuanceCriteria=None, restrictVirtualServerIds:bool=None, restrictedVirtualServerIds:list=None) -> None:
        self.attributeContractFulfillment = attributeContractFulfillment
        self.attributeSources = attributeSources
        self.authenticationPolicyContractRef = authenticationPolicyContractRef
        self.issuanceCriteria = issuanceCriteria
        self.restrictVirtualServerIds = restrictVirtualServerIds
        self.restrictedVirtualServerIds = restrictedVirtualServerIds

    def _validate(self) -> bool:
        return any(x for x in ["authenticationPolicyContractRef", "attributeContractFulfillment"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthenticationPolicyContractMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.attributeContractFulfillment, self.attributeSources, self.authenticationPolicyContractRef, self.issuanceCriteria, self.restrictVirtualServerIds, self.restrictedVirtualServerIds))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeContractFulfillment", "attributeSources", "authenticationPolicyContractRef", "issuanceCriteria", "restrictVirtualServerIds", "restrictedVirtualServerIds"]}

        return cls(**valid_data)