from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.issuance_criteria import IssuanceCriteria
from pingfedsdk.models.sp_attribute_query_policy import SpAttributeQueryPolicy
from pingfedsdk.models.attribute_source import AttributeSource


class SpAttributeQuery(Model):
    """The attribute query profile supports SPs in requesting user attributes.

    Attributes
    ----------
    attributes: list
        The list of attributes that may be returned to the SP in the response to an attribute request.

    attributeContractFulfillment: object
        A list of mappings from attribute names to their fulfillment values.

    issuanceCriteria: IssuanceCriteria
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.

    policy: SpAttributeQueryPolicy
        The attribute query profile's security policy.

    attributeSources: list
        A list of configured data stores to look up attributes from.

    """

    def __init__(self, attributeContractFulfillment: object, attributeSources: list, attributes: list, issuanceCriteria: IssuanceCriteria = None, policy: SpAttributeQueryPolicy = None) -> None:
        self.attributes = attributes
        self.attributeContractFulfillment = attributeContractFulfillment
        self.issuanceCriteria = issuanceCriteria
        self.policy = policy
        self.attributeSources = attributeSources

    def _validate(self) -> bool:
        return any(x for x in ["attributeContractFulfillment", "attributeSources", "attributes"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SpAttributeQuery):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.attributes, self.attributeContractFulfillment, self.issuanceCriteria, self.policy, self.attributeSources]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["attributes", "attributeContractFulfillment", "issuanceCriteria", "policy", "attributeSources"] and v is not None:
                if k == "attributes":
                    valid_data[k] = [str(x) for x in v]
                if k == "attributeContractFulfillment":
                    valid_data[k] = object(**v)
                if k == "issuanceCriteria":
                    valid_data[k] = IssuanceCriteria(**v)
                if k == "policy":
                    valid_data[k] = SpAttributeQueryPolicy(**v)
                if k == "attributeSources":
                    valid_data[k] = [AttributeSource(**x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["attributes", "attributeContractFulfillment", "issuanceCriteria", "policy", "attributeSources"]:
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
