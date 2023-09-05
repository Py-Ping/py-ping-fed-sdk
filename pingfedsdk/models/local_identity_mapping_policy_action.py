from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.attribute_mapping import AttributeMapping
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.enums import LocalIdentityMappingPolicyActionType


class LocalIdentityMappingPolicyAction(Model):
    """A local identity profile selection action.

    Attributes
    ----------
    type: LocalIdentityMappingPolicyActionType
        The authentication selection type.

    context: str
        The result context.

    localIdentityRef: ResourceLink
        Reference to the associated local identity profile.

    inboundMapping: AttributeMapping
        Inbound mappings into the local identity profile fields.

    outboundAttributeMapping: AttributeMapping
        Authentication policy contract mappings associated with this local Identity profile.

    """

    def __init__(self, localIdentityRef: ResourceLink, outboundAttributeMapping: AttributeMapping, type: LocalIdentityMappingPolicyActionType = None, context: str = None, inboundMapping: AttributeMapping = None) -> None:
        self.type = type
        self.context = context
        self.localIdentityRef = localIdentityRef
        self.inboundMapping = inboundMapping
        self.outboundAttributeMapping = outboundAttributeMapping

    def _validate(self) -> bool:
        return any(x for x in ["localIdentityRef", "outboundAttributeMapping"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, LocalIdentityMappingPolicyAction):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.context, self.localIdentityRef, self.inboundMapping, self.outboundAttributeMapping]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "context", "localIdentityRef", "inboundMapping", "outboundAttributeMapping"] and v is not None:
                if k == "type":
                    valid_data[k] = LocalIdentityMappingPolicyActionType[v]
                if k == "context":
                    valid_data[k] = str(v)
                if k == "localIdentityRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "inboundMapping":
                    valid_data[k] = AttributeMapping(**v)
                if k == "outboundAttributeMapping":
                    valid_data[k] = AttributeMapping(**v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["type", "context", "localIdentityRef", "inboundMapping", "outboundAttributeMapping"]:
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
