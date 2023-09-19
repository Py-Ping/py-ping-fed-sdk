from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.attribute_fulfillment_value import AttributeFulfillmentValue


class OIDCRequestParameter(Model):
    """An OIDC custom request parameter.

    Attributes
    ----------
    name: str
        Request parameter name.

    attributeValue: AttributeFulfillmentValue
        A request parameter attribute value with source type.

    value: str
        A request parameter value. A parameter can have either a value or a attribute value but not both. Value set here will be converted to an attribute value of source type TEXT. An empty value will be converted to attribute value of source type NO_MAPPING.

    applicationEndpointOverride: bool
        Indicates whether the parameter value can be overridden by an Application Endpoint parameter

    """
    def __init__(self, name: str, attributeValue: AttributeFulfillmentValue, applicationEndpointOverride: bool, value: str = None) -> None:
        self.name = name
        self.attributeValue = attributeValue
        self.value = value
        self.applicationEndpointOverride = applicationEndpointOverride

    def _validate(self) -> bool:
        return any(x for x in ["applicationEndpointOverride", "attributeValue", "name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OIDCRequestParameter):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.name, self.attributeValue, self.value, self.applicationEndpointOverride]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["name", "attributeValue", "value", "applicationEndpointOverride"] and v is not None:
                if k == "name":
                    valid_data[k] = str(v)
                if k == "attributeValue":
                    valid_data[k] = AttributeFulfillmentValue.from_dict(v)
                if k == "value":
                    valid_data[k] = str(v)
                if k == "applicationEndpointOverride":
                    valid_data[k] = bool(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["name", "attributeValue", "value", "applicationEndpointOverride"]:
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
