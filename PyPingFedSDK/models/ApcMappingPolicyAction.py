class ApcMappingPolicyAction():
    """An authentication policy contract selection action.

    Attributes
    ----------
    attributeMapping : str
 Contract fulfillment with the authentication policy contract's default values, and additional attributes retrieved from local data stores.
    authenticationPolicyContractRef : str
 Reference to the associated authentication policy contract.
    context : string
 The result context.
    type : str
 The authentication selection type.

    """

    def __init__(self, var_type, authenticationPolicyContractRef, attributeMapping, context:str=None) -> None:
        self.attributeMapping = attributeMapping
        self.authenticationPolicyContractRef = authenticationPolicyContractRef
        self.context = context
        self.var_type = var_type

    def _validate(self) -> bool:
        return any(x for x in ["var_type", "authenticationPolicyContractRef", "attributeMapping"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ApcMappingPolicyAction):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.attributeMapping, self.authenticationPolicyContractRef, self.context, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeMapping", "authenticationPolicyContractRef", "context", "var_type"]}

        return cls(**valid_data)