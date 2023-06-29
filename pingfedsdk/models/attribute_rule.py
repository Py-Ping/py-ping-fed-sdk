from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.enums import Condition


class AttributeRule(Model):
    """Authentication policy rules using attributes from the previous authentication source. Each rule is evaluated to determine the next action in the policy.

    Attributes
    ----------
    attributeName: str
        The name of the attribute to use in this attribute rule.

    condition: Condition
        The condition that will be applied to the attribute's expected value.

    expectedValue: str
        The expected value of this attribute rule.

    result: str
        The result of this attribute rule.

    """

    def __init__(self, attributeName: str, condition: Condition, expectedValue: str, result: str) -> None:
        self.attributeName = attributeName
        self.condition = condition
        self.expectedValue = expectedValue
        self.result = result

    def _validate(self) -> bool:
        return any(x for x in ["attributeName", "condition", "expectedValue", "result"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AttributeRule):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.attributeName, self.condition, self.expectedValue, self.result]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["attributeName", "condition", "expectedValue", "result"] and v is not None:
                if k == "attributeName":
                    valid_data[k] = str(v)
                if k == "condition":
                    valid_data[k] = Condition[v]
                if k == "expectedValue":
                    valid_data[k] = str(v)
                if k == "result":
                    valid_data[k] = str(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["attributeName", "condition", "expectedValue", "result"]:
                if isinstance(v, Model):
                    body[k] = v.to_dict(remove_nonetypes)
                elif isinstance(v, list):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, dict):
                    vals = {}
                    for x, y in v.items():
                        if isinstance(y, Model):
                            vals[x] = y.to_dict(remove_nonetypes)
                        elif not remove_nonetypes or (remove_nonetypes and y is not None):
                            vals[x] = y
                    body[k] = vals
                elif isinstance(v, set):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, Enum):
                    body[k] = str(v).split('.')[-1]
                elif not remove_nonetypes or (remove_nonetypes and v is not None):
                    body[k] = v
        return body
