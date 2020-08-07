class AttributeRule():
    """Authentication policy rules using attributes from the previous authentication source. Each rule is evaluated to determine the next action in the policy.

    Attributes
    ----------
    attributeName : string
 The name of the attribute to use in this attribute rule.
    condition : str
 The condition that will be applied to the attribute's expected value.
    expectedValue : string
 The expected value of this attribute rule.
    result : string
 The result of this attribute rule.

    """

<<<<<<< HEAD
    def __init__(self, attributeName, condition, expectedValue, result) -> None:
        self.attributeName = attributeName
        self.condition = condition
        self.expectedValue = expectedValue
        self.result = result
=======
    def __init__(self, attributeName, condition, expectedValue, result):
        self.attributeName: str = attributeName
        self.condition: str = condition
        self.expectedValue: str = expectedValue
        self.result: str = result
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["attributeName", "condition", "expectedValue", "result"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AttributeRule):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.attributeName, self.condition, self.expectedValue, self.result))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeName", "condition", "expectedValue", "result"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
