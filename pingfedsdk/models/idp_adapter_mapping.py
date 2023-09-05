from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.issuance_criteria import IssuanceCriteria
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.models.attribute_source import AttributeSource


class IdpAdapterMapping(Model):
    """The OAuth IdP Adapter Mapping.

    Attributes
    ----------
    id: str
        The ID of the adapter mapping.

    idpAdapterRef: ResourceLink
        Read only reference to the associated IdP adapter.

    attributeSources: list
        A list of configured data stores to look up attributes from.

    attributeContractFulfillment: object
        A list of mappings from attribute names to their fulfillment values.

    issuanceCriteria: IssuanceCriteria
        The issuance criteria that this transaction must meet before the corresponding attribute contract is fulfilled.

    """

    def __init__(self, attributeContractFulfillment: object, id: str, idpAdapterRef: ResourceLink = None, attributeSources: list = None, issuanceCriteria: IssuanceCriteria = None) -> None:
        self.id = id
        self.idpAdapterRef = idpAdapterRef
        self.attributeSources = attributeSources
        self.attributeContractFulfillment = attributeContractFulfillment
        self.issuanceCriteria = issuanceCriteria

    def _validate(self) -> bool:
        return any(x for x in ["attributeContractFulfillment", "id"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpAdapterMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.idpAdapterRef, self.attributeSources, self.attributeContractFulfillment, self.issuanceCriteria]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "idpAdapterRef", "attributeSources", "attributeContractFulfillment", "issuanceCriteria"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "idpAdapterRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "attributeSources":
                    valid_data[k] = [AttributeSource(**x) for x in v]
                if k == "attributeContractFulfillment":
                    valid_data[k] = object(**v)
                if k == "issuanceCriteria":
                    valid_data[k] = IssuanceCriteria(**v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "idpAdapterRef", "attributeSources", "attributeContractFulfillment", "issuanceCriteria"]:
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
