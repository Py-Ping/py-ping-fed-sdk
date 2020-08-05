class AccessTokenMapping():
    """The Access Token Attribute Mapping.

    Attributes
    ----------
    accessTokenManagerRef : str
        Reference to the access token manager this mapping is associated with. This property cannot be changed after the mapping is created.    attributeContractFulfillment : str
        A list of mappings from attribute names to their fulfillment values.    attributeSources : array
        A list of configured data stores to look up attributes from.    context : str
        The context of the Access Token Mapping. This property cannot be changed after the mapping is created.    id : string
        The id of the Access Token Mapping.    issuanceCriteria : str
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.
    """

    __slots__ = ["accessTokenManagerRef", "attributeContractFulfillment", "attributeSources", "context", "id", "issuanceCriteria"]

    def __init__(self, id, context, accessTokenManagerRef, attributeContractFulfillment, attributeSources=None, issuanceCriteria=None):
        self.accessTokenManagerRef = accessTokenManagerRef
        self.attributeContractFulfillment = attributeContractFulfillment
        self.attributeSources = attributeSources
        self.context = context
        self.id = id
        self.issuanceCriteria = issuanceCriteria

    def _validate(self):
        return any(x for x in ['id', 'context', 'accessTokenManagerRef', 'attributeContractFulfillment'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AccessTokenMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.accessTokenManagerRef, self.attributeContractFulfillment, self.attributeSources, self.context, self.id, self.issuanceCriteria))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["accessTokenManagerRef", "attributeContractFulfillment", "attributeSources", "context", "id", "issuanceCriteria"]}

        return cls(**valid_data)
