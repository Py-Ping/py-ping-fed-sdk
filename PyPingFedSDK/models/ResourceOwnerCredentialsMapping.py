class ResourceOwnerCredentialsMapping():
    """The OAuth Resource Owner Credentials Mapping.

    Attributes
    ----------
    attributeContractFulfillment : str
        A list of mappings from attribute names to their fulfillment values.    attributeSources : array
        A list of configured data stores to look up attributes from.    id : string
        The ID of the Resource Owner Credentials Mapping.    issuanceCriteria : str
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.    passwordValidatorRef : str
        Read only reference to the associated Source Password Validator Instance.
    """

    __slots__ = ["attributeContractFulfillment", "attributeSources", "id", "issuanceCriteria", "passwordValidatorRef"]

    def __init__(self, id, attributeContractFulfillment, attributeSources=None, issuanceCriteria=None, passwordValidatorRef=None):
        self.attributeContractFulfillment: str = attributeContractFulfillment
        self.attributeSources: list = attributeSources
        self.id: str = id
        self.issuanceCriteria: str = issuanceCriteria
        self.passwordValidatorRef: str = passwordValidatorRef

    def _validate(self):
        return any(x for x in ['id', 'attributeContractFulfillment'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ResourceOwnerCredentialsMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.attributeContractFulfillment, self.attributeSources, self.id, self.issuanceCriteria, self.passwordValidatorRef))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeContractFulfillment", "attributeSources", "id", "issuanceCriteria", "passwordValidatorRef"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__