class AuthnSelectorPolicyAction():
    """An authentication selector selection action.

    Attributes
    ----------
    authenticationSelectorRef : str
        Reference to the associated authentication selector.    context : string
        The result context.    type : str
        The authentication selection type.
    """

    __slots__ = ["authenticationSelectorRef", "context", "type"]

    def __init__(self, type, authenticationSelectorRef, context=None):
        self.authenticationSelectorRef = authenticationSelectorRef
        self.context = context
        self.type = type

    def _validate(self):
        return any(x for x in ['type', 'authenticationSelectorRef'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AuthnSelectorPolicyAction):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.authenticationSelectorRef, self.context, self.type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["authenticationSelectorRef", "context", "type"]}

        return cls(**valid_data)
