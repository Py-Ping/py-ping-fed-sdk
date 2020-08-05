class AuthnSourcePolicyAction():
    """An authentication source selection action.

    Attributes
    ----------
    attributeRules : str
        The authentication policy rules.    authenticationSource : str
        The associated authentication source.    context : string
        The result context.    inputUserIdMapping : str
        The input user id mapping.    type : str
        The authentication selection type.
    """

    __slots__ = ["attributeRules", "authenticationSource", "context", "inputUserIdMapping", "type"]

    def __init__(self, type, authenticationSource, attributeRules=None, context=None, inputUserIdMapping=None):
        self.attributeRules = attributeRules
        self.authenticationSource = authenticationSource
        self.context = context
        self.inputUserIdMapping = inputUserIdMapping
        self.type = type

    def _validate(self):
        return any(x for x in ['type', 'authenticationSource'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AuthnSourcePolicyAction):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.attributeRules, self.authenticationSource, self.context, self.inputUserIdMapping, self.type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeRules", "authenticationSource", "context", "inputUserIdMapping", "type"]}

        return cls(**valid_data)
