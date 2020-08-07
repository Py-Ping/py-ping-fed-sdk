class IssuanceCriteria():
    """A list of criteria that determines whether a transaction (usually a SSO transaction) is continued. All criteria must pass in order for the transaction to continue.

    Attributes
    ----------
    conditionalCriteria : array
        A list of conditional issuance criteria where existing attributes must satisfy their conditions against expected values in order for the transaction to continue.    expressionCriteria : array
        A list of expression issuance criteria where the OGNL expressions must evaluate to true in order for the transaction to continue.
    """

    __slots__ = ["conditionalCriteria", "expressionCriteria"]

    def __init__(self, conditionalCriteria=None, expressionCriteria=None):
        self.conditionalCriteria: list = conditionalCriteria
        self.expressionCriteria: list = expressionCriteria

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, IssuanceCriteria):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.conditionalCriteria, self.expressionCriteria))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["conditionalCriteria", "expressionCriteria"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__