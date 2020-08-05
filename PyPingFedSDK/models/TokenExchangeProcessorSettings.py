class TokenExchangeProcessorSettings():
    """ Settings for the OAuth Token Exchange Processor Policy configuration.

    Attributes
    ----------
    defaultProcessorPolicyRef : str
        Reference to the default Token Exchange Processor policy, if one is defined.

    """

    __slots__ = ["defaultProcessorPolicyRef"]
    def __init__(self, defaultProcessorPolicyRef=None):
            self.defaultProcessorPolicyRef = defaultProcessorPolicyRef
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, TokenExchangeProcessorSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((defaultProcessorPolicyRef))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
