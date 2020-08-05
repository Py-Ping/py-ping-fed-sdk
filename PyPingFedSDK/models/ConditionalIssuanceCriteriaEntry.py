class ConditionalIssuanceCriteriaEntry():
    """ An issuance criterion that checks a source attribute against a particular condition and the expected value. If the condition is true then this issuance criterion passes, otherwise the criterion fails.

    Attributes
    ----------
    attributeName : string
        The name of the attribute to use in this issuance criterion.
    condition : str
        The condition that will be applied to the source attribute's value and the expected value.
    errorResult : string
        The error result to return if this issuance criterion fails. This error result will show up in the PingFederate server logs.
    source : str
        The source of the attribute.
    value : string
        The expected value of this issuance criterion.

    """

    __slots__ = ["attributeName", "condition", "errorResult", "source", "value"]
    def __init__(self, source, attributeName, condition, value, errorResult=None):
            self.attributeName = attributeName
            self.condition = condition
            self.errorResult = errorResult
            self.source = source
            self.value = value
    
    def _validate(self):
        return any(x for x in ['source', 'attributeName', 'condition', 'value'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ConditionalIssuanceCriteriaEntry):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((attributeName, condition, errorResult, source, value))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
