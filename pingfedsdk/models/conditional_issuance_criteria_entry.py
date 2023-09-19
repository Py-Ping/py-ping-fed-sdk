from enum import Enum

from pingfedsdk.enums import Condition
from pingfedsdk.model import Model
from pingfedsdk.models.source_type_id_key import SourceTypeIdKey


class ConditionalIssuanceCriteriaEntry(Model):
    """An issuance criterion that checks a source attribute against a particular condition and the expected value. If the condition is true then this issuance criterion passes, otherwise the criterion fails.

    Attributes
    ----------
    source: SourceTypeIdKey
        The source of the attribute.

    attributeName: str
        The name of the attribute to use in this issuance criterion.

    condition: Condition
        The condition that will be applied to the source attribute's value and the expected value.

    value: str
        The expected value of this issuance criterion.

    errorResult: str
        The error result to return if this issuance criterion fails. This error result will show up in the PingFederate server logs.

    """
    def __init__(self, source: SourceTypeIdKey, attributeName: str, condition: Condition, value: str, errorResult: str = None) -> None:
        self.source = source
        self.attributeName = attributeName
        self.condition = condition
        self.value = value
        self.errorResult = errorResult

    def _validate(self) -> bool:
        return any(x for x in ["attributeName", "condition", "source", "value"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ConditionalIssuanceCriteriaEntry):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.source, self.attributeName, self.condition, self.value, self.errorResult]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["source", "attributeName", "condition", "value", "errorResult"] and v is not None:
                if k == "source":
                    valid_data[k] = SourceTypeIdKey.from_dict(v)
                if k == "attributeName":
                    valid_data[k] = str(v)
                if k == "condition":
                    valid_data[k] = Condition[v]
                if k == "value":
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
            if k in ["source", "attributeName", "condition", "value", "errorResult"]:
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
