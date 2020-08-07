class AccessTokenMapping():
    """The Access Token Attribute Mapping.

    Attributes
    ----------
    accessTokenManagerRef : str
 Reference to the access token manager this mapping is associated with. This property cannot be changed after the mapping is created.
    attributeContractFulfillment : str
 A list of mappings from attribute names to their fulfillment values.
    attributeSources : array
 A list of configured data stores to look up attributes from.
    context : str
 The context of the Access Token Mapping. This property cannot be changed after the mapping is created.
    id : string
 The id of the Access Token Mapping.
    issuanceCriteria : str
 The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.

    """

    def __init__(self, var_id, context, accessTokenManagerRef, attributeContractFulfillment, attributeSources=None, issuanceCriteria=None) -> None:
        self.accessTokenManagerRef = accessTokenManagerRef
        self.attributeContractFulfillment = attributeContractFulfillment
        self.attributeSources = attributeSources
        self.context = context
        self.var_id = var_id
        self.issuanceCriteria = issuanceCriteria

    def _validate(self) -> bool:
        return any(x for x in ["var_id", "context", "accessTokenManagerRef", "attributeContractFulfillment"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AccessTokenMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.accessTokenManagerRef, self.attributeContractFulfillment, self.attributeSources, self.context, self.var_id, self.issuanceCriteria))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["accessTokenManagerRef", "attributeContractFulfillment", "attributeSources", "context", "var_id", "issuanceCriteria"]}

        return cls(**valid_data)