class AuthenticationPolicyContractAssertionMapping():
    """The Authentication Policy Contract Assertion Mapping.

    Attributes
    ----------
    abortSsoTransactionAsFailSafe : boolean
        If set to true, SSO transaction will be aborted as a fail-safe when the data-store's attribute mappings fail to complete the attribute contract. Otherwise, the attribute contract with default values is used. By default, this value is false.    attributeContractFulfillment : str
        A list of mappings from attribute names to their fulfillment values.    attributeSources : array
        A list of configured data stores to look up attributes from.    authenticationPolicyContractRef : str
        Reference to the associated Authentication Policy Contract.    issuanceCriteria : str
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.    restrictVirtualEntityIds : boolean
        Restricts this mapping to specific virtual entity IDs.    restrictedVirtualEntityIds : array
        The list of virtual server IDs that this mapping is restricted to.
    """

    __slots__ = ["abortSsoTransactionAsFailSafe", "attributeContractFulfillment", "attributeSources", "authenticationPolicyContractRef", "issuanceCriteria", "restrictVirtualEntityIds", "restrictedVirtualEntityIds"]

    def __init__(self, authenticationPolicyContractRef, attributeContractFulfillment, abortSsoTransactionAsFailSafe=None, attributeSources=None, issuanceCriteria=None, restrictVirtualEntityIds=None, restrictedVirtualEntityIds=None):
        self.abortSsoTransactionAsFailSafe = abortSsoTransactionAsFailSafe
        self.attributeContractFulfillment = attributeContractFulfillment
        self.attributeSources = attributeSources
        self.authenticationPolicyContractRef = authenticationPolicyContractRef
        self.issuanceCriteria = issuanceCriteria
        self.restrictVirtualEntityIds = restrictVirtualEntityIds
        self.restrictedVirtualEntityIds = restrictedVirtualEntityIds

    def _validate(self):
        return any(x for x in ['authenticationPolicyContractRef', 'attributeContractFulfillment'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AuthenticationPolicyContractAssertionMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.abortSsoTransactionAsFailSafe, self.attributeContractFulfillment, self.attributeSources, self.authenticationPolicyContractRef, self.issuanceCriteria, self.restrictVirtualEntityIds, self.restrictedVirtualEntityIds))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["abortSsoTransactionAsFailSafe", "attributeContractFulfillment", "attributeSources", "authenticationPolicyContractRef", "issuanceCriteria", "restrictVirtualEntityIds", "restrictedVirtualEntityIds"]}

        return cls(**valid_data)
