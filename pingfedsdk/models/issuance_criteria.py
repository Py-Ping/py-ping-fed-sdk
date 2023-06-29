from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.conditional_issuance_criteria_entry import ConditionalIssuanceCriteriaEntry
from pingfedsdk.models.expression_issuance_criteria_entry import ExpressionIssuanceCriteriaEntry


class IssuanceCriteria(Model):
    """A list of criteria that determines whether a transaction (usually a SSO transaction) is continued. All criteria must pass in order for the transaction to continue.

    Attributes
    ----------
    conditionalCriteria: list
        A list of conditional issuance criteria where existing attributes must satisfy their conditions against expected values in order for the transaction to continue.

    expressionCriteria: list
        A list of expression issuance criteria where the OGNL expressions must evaluate to true in order for the transaction to continue.

    """

    def __init__(self, conditionalCriteria: list = None, expressionCriteria: list = None) -> None:
        self.conditionalCriteria = conditionalCriteria
        self.expressionCriteria = expressionCriteria

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, IssuanceCriteria):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.conditionalCriteria, self.expressionCriteria]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["conditionalCriteria", "expressionCriteria"] and v is not None:
                if k == "conditionalCriteria":
                    valid_data[k] = [ConditionalIssuanceCriteriaEntry(**x) for x in v]
                if k == "expressionCriteria":
                    valid_data[k] = [ExpressionIssuanceCriteriaEntry(**x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["conditionalCriteria", "expressionCriteria"]:
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
