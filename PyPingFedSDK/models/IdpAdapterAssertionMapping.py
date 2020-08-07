class IdpAdapterAssertionMapping():
    """The IdP Adapter Assertion Mapping.

    Attributes
    ----------
    abortSsoTransactionAsFailSafe : boolean
 If set to true, SSO transaction will be aborted as a fail-safe when the data-store's attribute mappings fail to complete the attribute contract. Otherwise, the attribute contract with default values is used. By default, this value is false.
    adapterOverrideSettings : str
 Connection specific configuration overrides for the mapped adapter instance.
    attributeContractFulfillment : str
 A list of mappings from attribute names to their fulfillment values.
    attributeSources : array
 A list of configured data stores to look up attributes from.
    idpAdapterRef : str
 Reference to the associated IdP adapter.<br>Note: This is ignored if adapter overrides for this mapping exists. In this case, the override's parent adapter reference is used.
    issuanceCriteria : str
 The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.
    restrictVirtualEntityIds : boolean
 Restricts this mapping to specific virtual entity IDs.
    restrictedVirtualEntityIds : array
 The list of virtual server IDs that this mapping is restricted to.

    """

    def __init__(self, idpAdapterRef, attributeContractFulfillment, abortSsoTransactionAsFailSafe=None, adapterOverrideSettings=None, attributeSources=None, issuanceCriteria=None, restrictVirtualEntityIds=None, restrictedVirtualEntityIds=None) -> None:
        self.abortSsoTransactionAsFailSafe = abortSsoTransactionAsFailSafe
        self.adapterOverrideSettings = adapterOverrideSettings
        self.attributeContractFulfillment = attributeContractFulfillment
        self.attributeSources = attributeSources
        self.idpAdapterRef = idpAdapterRef
        self.issuanceCriteria = issuanceCriteria
        self.restrictVirtualEntityIds = restrictVirtualEntityIds
        self.restrictedVirtualEntityIds = restrictedVirtualEntityIds

    def _validate(self) -> bool:
        return any(x for x in ["idpAdapterRef", "attributeContractFulfillment"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpAdapterAssertionMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.abortSsoTransactionAsFailSafe, self.adapterOverrideSettings, self.attributeContractFulfillment, self.attributeSources, self.idpAdapterRef, self.issuanceCriteria, self.restrictVirtualEntityIds, self.restrictedVirtualEntityIds))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["abortSsoTransactionAsFailSafe", "adapterOverrideSettings", "attributeContractFulfillment", "attributeSources", "idpAdapterRef", "issuanceCriteria", "restrictVirtualEntityIds", "restrictedVirtualEntityIds"]}

        return cls(**valid_data)