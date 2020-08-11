class SpTokenGeneratorMapping():
    """The SP Token Generator Mapping.

    Attributes
    ----------
    attributeContractFulfillment : str
        A list of mappings from attribute names to their fulfillment values.
    attributeSources : array
        A list of configured data stores to look up attributes from.
    defaultMapping : boolean
        Indicates whether the token generator mapping is the default mapping. The default value is false.
    issuanceCriteria : str
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.
    restrictedVirtualEntityIds : array
        The list of virtual server IDs that this mapping is restricted to.
    spTokenGeneratorRef : str
        Reference to the associated token generator.

    """

    def __init__(self, spTokenGeneratorRef, attributeContractFulfillment, attributeSources:list=None, defaultMapping:bool=None, issuanceCriteria=None, restrictedVirtualEntityIds:list=None) -> None:
        self.attributeContractFulfillment = attributeContractFulfillment
        self.attributeSources = attributeSources
        self.defaultMapping = defaultMapping
        self.issuanceCriteria = issuanceCriteria
        self.restrictedVirtualEntityIds = restrictedVirtualEntityIds
        self.spTokenGeneratorRef = spTokenGeneratorRef

    def _validate(self) -> bool:
        return any(x for x in ["spTokenGeneratorRef", "attributeContractFulfillment"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SpTokenGeneratorMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.attributeContractFulfillment, self.attributeSources, self.defaultMapping, self.issuanceCriteria, self.restrictedVirtualEntityIds, self.spTokenGeneratorRef))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeContractFulfillment", "attributeSources", "defaultMapping", "issuanceCriteria", "restrictedVirtualEntityIds", "spTokenGeneratorRef"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__