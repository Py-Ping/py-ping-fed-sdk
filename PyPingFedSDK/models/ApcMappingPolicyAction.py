class ApcMappingPolicyAction():
    """An authentication policy contract selection action.

    Attributes
    ----------
    attributeMapping : str
        Contract fulfillment with the authentication policy contract's default values, and additional attributes retrieved from local data stores.    authenticationPolicyContractRef : str
        Reference to the associated authentication policy contract.    context : string
        The result context.    type : str
        The authentication selection type.
    """

    __slots__ = ["attributeMapping", "authenticationPolicyContractRef", "context", "type"]

    def __init__(self, type, authenticationPolicyContractRef, attributeMapping, context=None):
        self.attributeMapping: str = attributeMapping
        self.authenticationPolicyContractRef: str = authenticationPolicyContractRef
        self.context: str = context
        self.type: str = type

    def _validate(self):
        return any(x for x in ['type', 'authenticationPolicyContractRef', 'attributeMapping'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ApcMappingPolicyAction):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.attributeMapping, self.authenticationPolicyContractRef, self.context, self.type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeMapping", "authenticationPolicyContractRef", "context", "type"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__