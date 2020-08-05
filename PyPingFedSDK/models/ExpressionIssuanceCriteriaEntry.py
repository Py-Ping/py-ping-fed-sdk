class ExpressionIssuanceCriteriaEntry():
    """An issuance criterion that uses a Boolean return value from an OGNL expression to determine whether or not it passes.

    Attributes
    ----------
    errorResult : string
        The error result to return if this issuance criterion fails. This error result will show up in the PingFederate server logs.    expression : string
        The OGNL expression to evaluate.
    """

    __slots__ = ["errorResult", "expression"]

    def __init__(self, expression, errorResult=None):
        self.errorResult = errorResult
        self.expression = expression

    def _validate(self):
        return any(x for x in ['expression'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ExpressionIssuanceCriteriaEntry):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.errorResult, self.expression))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["errorResult", "expression"]}

        return cls(**valid_data)
