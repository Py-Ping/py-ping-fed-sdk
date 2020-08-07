class CibaServerPolicySettings():
    """Settings for the CIBA request policy configuration.

    Attributes
    ----------
    defaultRequestPolicyRef : str
 Reference to the default request policy, if one is defined.

    """

    def __init__(self, defaultRequestPolicyRef=None) -> None:
        self.defaultRequestPolicyRef = defaultRequestPolicyRef

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, CibaServerPolicySettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.defaultRequestPolicyRef))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["defaultRequestPolicyRef"]}

        return cls(**valid_data)