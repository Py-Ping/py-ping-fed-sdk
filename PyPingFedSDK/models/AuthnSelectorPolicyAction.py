class AuthnSelectorPolicyAction():
    """An authentication selector selection action.

    Attributes
    ----------
    authenticationSelectorRef : str
 Reference to the associated authentication selector.
    context : string
 The result context.
    type : str
 The authentication selection type.

    """

<<<<<<< HEAD
    def __init__(self, var_type, authenticationSelectorRef, context=None) -> None:
        self.authenticationSelectorRef = authenticationSelectorRef
        self.context = context
        self.var_type = var_type
=======
    def __init__(self, type, authenticationSelectorRef, context=None):
        self.authenticationSelectorRef: str = authenticationSelectorRef
        self.context: str = context
        self.type: str = type
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["var_type", "authenticationSelectorRef"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthnSelectorPolicyAction):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.authenticationSelectorRef, self.context, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["authenticationSelectorRef", "context", "var_type"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
