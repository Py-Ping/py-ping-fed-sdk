class IdpAdapterMapping():
    """The OAuth IdP Adapter Mapping.

    Attributes
    ----------
    attributeContractFulfillment : str
 A list of mappings from attribute names to their fulfillment values.
    attributeSources : array
 A list of configured data stores to look up attributes from.
    id : string
 The ID of the adapter mapping.
    idpAdapterRef : str
 Read only reference to the associated IdP adapter.
    issuanceCriteria : str
 The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.

    """

    def __init__(self, var_id, attributeContractFulfillment, attributeSources=None, idpAdapterRef=None, issuanceCriteria=None) -> None:
        self.attributeContractFulfillment = attributeContractFulfillment
        self.attributeSources = attributeSources
        self.var_id = var_id
        self.idpAdapterRef = idpAdapterRef
        self.issuanceCriteria = issuanceCriteria

    def _validate(self) -> bool:
        return any(x for x in ["var_id", "attributeContractFulfillment"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpAdapterMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.attributeContractFulfillment, self.attributeSources, self.var_id, self.idpAdapterRef, self.issuanceCriteria))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeContractFulfillment", "attributeSources", "var_id", "idpAdapterRef", "issuanceCriteria"]}

        return cls(**valid_data)