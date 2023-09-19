from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.attribute_source import AttributeSource
from pingfedsdk.models.issuance_criteria import IssuanceCriteria


class ProcessorPolicyToGeneratorMapping(Model):
    """A Token Exchange Processor policy to Token Generator Mapping.

    Attributes
    ----------
    attributeSources: list
        A list of configured data stores to look up attributes from.

    attributeContractFulfillment: object
        A list of mappings from attribute names to their fulfillment values.

    issuanceCriteria: IssuanceCriteria
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.

    id: str
        The id of the Token Exchange Processor policy to Token Generator mapping. This field is read-only and is ignored when passed in with the payload.

    sourceId: str
        The id of the Token Exchange Processor policy.

    targetId: str
        The id of the Token Generator.

    licenseConnectionGroupAssignment: str
        The license connection group.

    """
    def __init__(self, attributeContractFulfillment: object, sourceId: str, targetId: str, attributeSources: list = None, issuanceCriteria: IssuanceCriteria = None, id: str = None, licenseConnectionGroupAssignment: str = None) -> None:
        self.attributeSources = attributeSources
        self.attributeContractFulfillment = attributeContractFulfillment
        self.issuanceCriteria = issuanceCriteria
        self.id = id
        self.sourceId = sourceId
        self.targetId = targetId
        self.licenseConnectionGroupAssignment = licenseConnectionGroupAssignment

    def _validate(self) -> bool:
        return any(x for x in ["attributeContractFulfillment", "sourceId", "targetId"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ProcessorPolicyToGeneratorMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.attributeSources, self.attributeContractFulfillment, self.issuanceCriteria, self.id, self.sourceId, self.targetId, self.licenseConnectionGroupAssignment]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["attributeSources", "attributeContractFulfillment", "issuanceCriteria", "id", "sourceId", "targetId", "licenseConnectionGroupAssignment"] and v is not None:
                if k == "attributeSources":
                    valid_data[k] = [AttributeSource.from_dict(x) for x in v]
                if k == "attributeContractFulfillment":
                    valid_data[k] = object.from_dict(v)
                if k == "issuanceCriteria":
                    valid_data[k] = IssuanceCriteria.from_dict(v)
                if k == "id":
                    valid_data[k] = str(v)
                if k == "sourceId":
                    valid_data[k] = str(v)
                if k == "targetId":
                    valid_data[k] = str(v)
                if k == "licenseConnectionGroupAssignment":
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
            if k in ["attributeSources", "attributeContractFulfillment", "issuanceCriteria", "id", "sourceId", "targetId", "licenseConnectionGroupAssignment"]:
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
