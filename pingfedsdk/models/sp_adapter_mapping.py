from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.attribute_fulfillment_value import AttributeFulfillmentValue
from pingfedsdk.models.attribute_source import AttributeSource
from pingfedsdk.models.issuance_criteria import IssuanceCriteria
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.models.sp_adapter import SpAdapter


class SpAdapterMapping(Model):
    """A mapping to a SP adapter.

    Attributes
    ----------
    spAdapterRef: ResourceLink
        Reference to the associated SP adapter.
        Note: This is ignored if adapter overrides for this mapping exists. In this case, the override's parent adapter reference is used.

    restrictVirtualEntityIds: bool
        Restricts this mapping to specific virtual entity IDs.

    restrictedVirtualEntityIds: list
        The list of virtual server IDs that this mapping is restricted to.

    adapterOverrideSettings: SpAdapter
        Connection specific overridden adapter instance for mapping.

    attributeSources: list
        A list of configured data stores to look up attributes from.

    attributeContractFulfillment: dict
        A list of mappings from attribute names to their fulfillment values.

    issuanceCriteria: IssuanceCriteria
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.

    """
    def __init__(self, spAdapterRef: ResourceLink, attributeContractFulfillment: dict, restrictVirtualEntityIds: bool = None, restrictedVirtualEntityIds: list = None, adapterOverrideSettings: SpAdapter = None, attributeSources: list = None, issuanceCriteria: IssuanceCriteria = None) -> None:
        self.spAdapterRef = spAdapterRef
        self.restrictVirtualEntityIds = restrictVirtualEntityIds
        self.restrictedVirtualEntityIds = restrictedVirtualEntityIds
        self.adapterOverrideSettings = adapterOverrideSettings
        self.attributeSources = attributeSources
        self.attributeContractFulfillment = attributeContractFulfillment
        self.issuanceCriteria = issuanceCriteria

    def _validate(self) -> bool:
        return any(x for x in ["attributeContractFulfillment", "spAdapterRef"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SpAdapterMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.spAdapterRef, self.restrictVirtualEntityIds, self.restrictedVirtualEntityIds, self.adapterOverrideSettings, self.attributeSources, self.attributeContractFulfillment, self.issuanceCriteria]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["spAdapterRef", "restrictVirtualEntityIds", "restrictedVirtualEntityIds", "adapterOverrideSettings", "attributeSources", "attributeContractFulfillment", "issuanceCriteria"] and v is not None:
                if k == "spAdapterRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "restrictVirtualEntityIds":
                    valid_data[k] = bool(v)
                if k == "restrictedVirtualEntityIds":
                    valid_data[k] = [str(x) for x in v]
                if k == "adapterOverrideSettings":
                    valid_data[k] = SpAdapter.from_dict(v)
                if k == "attributeSources":
                    valid_data[k] = [AttributeSource.from_dict(x) for x in v]
                if k == "attributeContractFulfillment":
                    valid_data[k] = {str(x): AttributeFulfillmentValue.from_dict(y) for x, y in v.items()}
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
            if k in ["spAdapterRef", "restrictVirtualEntityIds", "restrictedVirtualEntityIds", "adapterOverrideSettings", "attributeSources", "attributeContractFulfillment", "issuanceCriteria"]:
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
