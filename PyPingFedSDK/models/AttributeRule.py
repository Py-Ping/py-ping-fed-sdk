class AttributeRule():
    """Authentication policy rules using attributes from the previous authentication source. Each rule is evaluated to determine the next action in the policy.

    Attributes
    ----------
    attributeName : string
        The name of the attribute to use in this attribute rule.    condition : str
        The condition that will be applied to the attribute's expected value.    expectedValue : string
        The expected value of this attribute rule.    result : string
        The result of this attribute rule.
    """

    __slots__ = ["attributeName", "condition", "expectedValue", "result"]

    def __init__(self, attributeName, condition, expectedValue, result):
        self.attributeName: str = attributeName
        self.condition: str = condition
        self.expectedValue: str = expectedValue
        self.result: str = result

    def _validate(self):
        return any(x for x in ['attributeName', 'condition', 'expectedValue', 'result'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AttributeRule):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.attributeName, self.condition, self.expectedValue, self.result))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeName", "condition", "expectedValue", "result"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__