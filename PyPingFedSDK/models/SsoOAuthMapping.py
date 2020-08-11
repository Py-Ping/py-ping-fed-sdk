class SsoOAuthMapping():
    """IdP Browser SSO OAuth Attribute Mapping

    Attributes
    ----------
    attributeContractFulfillment : str
        A list of mappings from attribute names to their fulfillment values.
    attributeSources : array
        A list of configured data stores to look up attributes from.
    issuanceCriteria : str
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.

    """

    def __init__(self, attributeContractFulfillment, attributeSources:list=None, issuanceCriteria=None) -> None:
        self.attributeContractFulfillment = attributeContractFulfillment
        self.attributeSources = attributeSources
        self.issuanceCriteria = issuanceCriteria

    def _validate(self) -> bool:
        return any(x for x in ["attributeContractFulfillment"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SsoOAuthMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.attributeContractFulfillment, self.attributeSources, self.issuanceCriteria))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeContractFulfillment", "attributeSources", "issuanceCriteria"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__