from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.attribute import Attribute
from pingfedsdk.models.attribute_fulfillment_value import AttributeFulfillmentValue
from pingfedsdk.models.idp_inbound_provisioning_attribute_contract import IdpInboundProvisioningAttributeContract


class ReadGroups(Model):
    """Group info lookup and respond to incoming SCIM requests configuration.

    Attributes
    ----------
    attributeContract: IdpInboundProvisioningAttributeContract
        A list of attributes that the IdP sends in the SCIM response.

    attributes: list
        A list of LDAP data store attributes to populate a response to a user-provisioning request.

    attributeFulfillment: dict
        A list of user repository mappings from attribute names to their fulfillment values.

    """
    def __init__(self, attributeContract: IdpInboundProvisioningAttributeContract, attributes: list, attributeFulfillment: dict) -> None:
        self.attributeContract = attributeContract
        self.attributes = attributes
        self.attributeFulfillment = attributeFulfillment

    def _validate(self) -> bool:
        return any(x for x in ["attributeContract", "attributeFulfillment", "attributes"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ReadGroups):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.attributeContract, self.attributes, self.attributeFulfillment]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["attributeContract", "attributes", "attributeFulfillment"] and v is not None:
                if k == "attributeContract":
                    valid_data[k] = IdpInboundProvisioningAttributeContract.from_dict(v)
                if k == "attributes":
                    valid_data[k] = [Attribute.from_dict(x) for x in v]
                if k == "attributeFulfillment":
                    valid_data[k] = {str(x): AttributeFulfillmentValue.from_dict(y) for x, y in v.items()}

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["attributeContract", "attributes", "attributeFulfillment"]:
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
