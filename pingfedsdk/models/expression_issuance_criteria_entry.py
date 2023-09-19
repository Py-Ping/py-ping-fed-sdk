from enum import Enum

from pingfedsdk.model import Model


class ExpressionIssuanceCriteriaEntry(Model):
    """An issuance criterion that uses a Boolean return value from an OGNL expression to determine whether or not it passes.

    Attributes
    ----------
    expression: str
        The OGNL expression to evaluate.

    errorResult: str
        The error result to return if this issuance criterion fails. This error result will show up in the PingFederate server logs.

    """
    def __init__(self, expression: str, errorResult: str = None) -> None:
        self.expression = expression
        self.errorResult = errorResult

    def _validate(self) -> bool:
        return any(x for x in ["expression"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ExpressionIssuanceCriteriaEntry):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.expression, self.errorResult]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["expression", "errorResult"] and v is not None:
                if k == "expression":
                    valid_data[k] = str(v)
                if k == "errorResult":
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
            if k in ["expression", "errorResult"]:
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
