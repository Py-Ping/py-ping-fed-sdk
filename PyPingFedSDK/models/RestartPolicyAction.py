class RestartPolicyAction():
    """ The restart selection action.

    Attributes
    ----------
    context : string
        The result context.
    type : str
        The authentication selection type.

    """

    __slots__ = ["context", "type"]
    def __init__(self, type, context=None):
            self.context = context
            self.type = type
    
    def _validate(self):
        return any(x for x in ['type'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, RestartPolicyAction):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((context, type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
