class CibaServerPolicySettings():
    """Settings for the CIBA request policy configuration.

    Attributes
    ----------
    defaultRequestPolicyRef : str
        Reference to the default request policy, if one is defined.
    """

    __slots__ = ["defaultRequestPolicyRef"]

    def __init__(self, defaultRequestPolicyRef=None):
        self.defaultRequestPolicyRef = defaultRequestPolicyRef

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, CibaServerPolicySettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.defaultRequestPolicyRef))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["defaultRequestPolicyRef"]}

        return cls(**valid_data)
