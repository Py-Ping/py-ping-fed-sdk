from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.models.field_entry import FieldEntry
from pingfedsdk.enums import DataStoreType


class CustomAttributeSource(Model):
    """The configured settings used to look up attributes from a custom data store.

    Attributes
    ----------
    type: DataStoreType
        The data store type of this attribute source.

    dataStoreRef: ResourceLink
        Reference to the associated data store.

    id: str
        The ID that defines this attribute source. Only alphanumeric characters allowed.
        Note: Required for OpenID Connect policy attribute sources, OAuth IdP adapter mappings, OAuth access token mappings and APC-to-SP Adapter Mappings. IdP Connections will ignore this property since it only allows one attribute source to be defined per mapping. IdP-to-SP Adapter Mappings can contain multiple attribute sources.

    description: str
        The description of this attribute source. The description needs to be unique amongst the attribute sources for the mapping.
        Note: Required for APC-to-SP Adapter Mappings

    attributeContractFulfillment: object
        A list of mappings from attribute names to their fulfillment values. This field is only valid for the SP Connection's Browser SSO mappings

    filterFields: list
        The list of fields that can be used to filter a request to the custom data store.

    """

    def __init__(self, dataStoreRef: ResourceLink, type: DataStoreType, id: str = None, description: str = None, attributeContractFulfillment: object = None, filterFields: list = None) -> None:
        self.type = type
        self.dataStoreRef = dataStoreRef
        self.id = id
        self.description = description
        self.attributeContractFulfillment = attributeContractFulfillment
        self.filterFields = filterFields

    def _validate(self) -> bool:
        return any(x for x in ["dataStoreRef", "type"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, CustomAttributeSource):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.dataStoreRef, self.id, self.description, self.attributeContractFulfillment, self.filterFields]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "dataStoreRef", "id", "description", "attributeContractFulfillment", "filterFields"] and v is not None:
                if k == "type":
                    valid_data[k] = DataStoreType[v]
                if k == "dataStoreRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "id":
                    valid_data[k] = str(v)
                if k == "description":
                    valid_data[k] = str(v)
                if k == "attributeContractFulfillment":
                    valid_data[k] = object(**v)
                if k == "filterFields":
                    valid_data[k] = [FieldEntry(**x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["type", "dataStoreRef", "id", "description", "attributeContractFulfillment", "filterFields"]:
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
