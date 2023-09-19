from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.attribute_source import AttributeSource
from pingfedsdk.models.issuance_criteria import IssuanceCriteria
from pingfedsdk.models.resource_link import ResourceLink


class SpTokenGeneratorMapping(Model):
    """The SP Token Generator Mapping.

    Attributes
    ----------
    spTokenGeneratorRef: ResourceLink
        Reference to the associated token generator.

    restrictedVirtualEntityIds: list
        The list of virtual server IDs that this mapping is restricted to.

    defaultMapping: bool
        Indicates whether the token generator mapping is the default mapping. The default value is false.

    attributeSources: list
        A list of configured data stores to look up attributes from.

    attributeContractFulfillment: object
        A list of mappings from attribute names to their fulfillment values.

    issuanceCriteria: IssuanceCriteria
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.

    """
    def __init__(self, spTokenGeneratorRef: ResourceLink, attributeContractFulfillment: object, restrictedVirtualEntityIds: list = None, defaultMapping: bool = None, attributeSources: list = None, issuanceCriteria: IssuanceCriteria = None) -> None:
        self.spTokenGeneratorRef = spTokenGeneratorRef
        self.restrictedVirtualEntityIds = restrictedVirtualEntityIds
        self.defaultMapping = defaultMapping
        self.attributeSources = attributeSources
        self.attributeContractFulfillment = attributeContractFulfillment
        self.issuanceCriteria = issuanceCriteria

    def _validate(self) -> bool:
        return any(x for x in ["attributeContractFulfillment", "spTokenGeneratorRef"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SpTokenGeneratorMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.spTokenGeneratorRef, self.restrictedVirtualEntityIds, self.defaultMapping, self.attributeSources, self.attributeContractFulfillment, self.issuanceCriteria]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["spTokenGeneratorRef", "restrictedVirtualEntityIds", "defaultMapping", "attributeSources", "attributeContractFulfillment", "issuanceCriteria"] and v is not None:
                if k == "spTokenGeneratorRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "restrictedVirtualEntityIds":
                    valid_data[k] = [str(x) for x in v]
                if k == "defaultMapping":
                    valid_data[k] = bool(v)
                if k == "attributeSources":
                    valid_data[k] = [AttributeSource.from_dict(x) for x in v]
                if k == "attributeContractFulfillment":
                    valid_data[k] = object.from_dict(v)
                if k == "issuanceCriteria":
                    valid_data[k] = IssuanceCriteria.from_dict(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["spTokenGeneratorRef", "restrictedVirtualEntityIds", "defaultMapping", "attributeSources", "attributeContractFulfillment", "issuanceCriteria"]:
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
