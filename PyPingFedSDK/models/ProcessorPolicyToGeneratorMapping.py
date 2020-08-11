class ProcessorPolicyToGeneratorMapping():
    """A Token Exchange Processor policy to Token Generator Mapping.

    Attributes
    ----------
    attributeContractFulfillment : str
        A list of mappings from attribute names to their fulfillment values.
    attributeSources : array
        A list of configured data stores to look up attributes from.
    id : string
        The id of the Token Exchange Processor policy to Token Generator mapping. This field is read-only and is ignored when passed in with the payload.
    issuanceCriteria : str
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.
    licenseConnectionGroupAssignment : string
        The license connection group.
    sourceId : string
        The id of the Token Exchange Processor policy.
    targetId : string
        The id of the Token Generator.

    """

    def __init__(self, attributeContractFulfillment, sourceId:str, targetId:str, attributeSources:list=None, var_id:str=None, issuanceCriteria=None, licenseConnectionGroupAssignment:str=None) -> None:
        self.attributeContractFulfillment = attributeContractFulfillment
        self.attributeSources = attributeSources
        self.var_id = var_id
        self.issuanceCriteria = issuanceCriteria
        self.licenseConnectionGroupAssignment = licenseConnectionGroupAssignment
        self.sourceId = sourceId
        self.targetId = targetId

    def _validate(self) -> bool:
        return any(x for x in ["attributeContractFulfillment", "sourceId", "targetId"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ProcessorPolicyToGeneratorMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.attributeContractFulfillment, self.attributeSources, self.var_id, self.issuanceCriteria, self.licenseConnectionGroupAssignment, self.sourceId, self.targetId]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeContractFulfillment", "attributeSources", "var_id", "issuanceCriteria", "licenseConnectionGroupAssignment", "sourceId", "targetId"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__