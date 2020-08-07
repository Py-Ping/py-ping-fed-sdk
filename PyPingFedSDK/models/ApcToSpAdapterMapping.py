class ApcToSpAdapterMapping():
    """The Authentication Policy Contract (APC) to SP Adapter Mapping.

    Attributes
    ----------
    attributeContractFulfillment : str
        A list of mappings from attribute names to their fulfillment values.    attributeSources : array
        A list of configured data stores to look up attributes from.    defaultTargetResource : string
        Default target URL for this APC-to-adapter mapping configuration.    id : string
        The id of the APC-to-SP Adapter mapping. This field is read-only and is ignored when passed in with the payload.    issuanceCriteria : str
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.    licenseConnectionGroupAssignment : string
        The license connection group.    sourceId : string
        The id of the Authentication Policy Contract.    targetId : string
        The id of the SP Adapter.
    """

    __slots__ = ["attributeContractFulfillment", "attributeSources", "defaultTargetResource", "id", "issuanceCriteria", "licenseConnectionGroupAssignment", "sourceId", "targetId"]

    def __init__(self, attributeContractFulfillment, sourceId, targetId, attributeSources=None, defaultTargetResource=None, id=None, issuanceCriteria=None, licenseConnectionGroupAssignment=None):
        self.attributeContractFulfillment: str = attributeContractFulfillment
        self.attributeSources: list = attributeSources
        self.defaultTargetResource: str = defaultTargetResource
        self.id: str = id
        self.issuanceCriteria: str = issuanceCriteria
        self.licenseConnectionGroupAssignment: str = licenseConnectionGroupAssignment
        self.sourceId: str = sourceId
        self.targetId: str = targetId

    def _validate(self):
        return any(x for x in ['attributeContractFulfillment', 'sourceId', 'targetId'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ApcToSpAdapterMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.attributeContractFulfillment, self.attributeSources, self.defaultTargetResource, self.id, self.issuanceCriteria, self.licenseConnectionGroupAssignment, self.sourceId, self.targetId))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeContractFulfillment", "attributeSources", "defaultTargetResource", "id", "issuanceCriteria", "licenseConnectionGroupAssignment", "sourceId", "targetId"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__