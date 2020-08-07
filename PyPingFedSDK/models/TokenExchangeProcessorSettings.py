class TokenExchangeProcessorSettings():
    """Settings for the OAuth Token Exchange Processor Policy configuration.

    Attributes
    ----------
    defaultProcessorPolicyRef : str
 Reference to the default Token Exchange Processor policy, if one is defined.

    """

    def __init__(self, defaultProcessorPolicyRef=None) -> None:
        self.defaultProcessorPolicyRef = defaultProcessorPolicyRef

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, TokenExchangeProcessorSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.defaultProcessorPolicyRef))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["defaultProcessorPolicyRef"]}

        return cls(**valid_data)