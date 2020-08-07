class PolicyAction():
    """An authentication policy selection action.

    Attributes
    ----------
    context : string
        The result context.    type : str
        The authentication selection type.
    """

    __slots__ = ["context", "type"]

    def __init__(self, type, context=None):
        self.context: str = context
        self.type: str = type

    def _validate(self):
        return any(x for x in ['type'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, PolicyAction):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.context, self.type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["context", "type"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__