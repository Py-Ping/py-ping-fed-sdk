from enum import Enum

from pingfedsdk.enums import FragmentPolicyActionType
from pingfedsdk.model import Model
from pingfedsdk.models.attribute_mapping import AttributeMapping
from pingfedsdk.models.attribute_rules import AttributeRules
from pingfedsdk.models.resource_link import ResourceLink


class FragmentPolicyAction(Model):
    """A authentication policy fragment selection action.

    Attributes
    ----------
    type: FragmentPolicyActionType
        The authentication selection type.

    context: str
        The result context.

    attributeRules: AttributeRules
        The authentication policy rules.

    fragment: ResourceLink
        Reference to the associated authentication fragment.

    fragmentMapping: AttributeMapping
        The fragment mapping for attributes to be passed into the authentication fragment.

    """
    def __init__(self, fragment: ResourceLink, type: FragmentPolicyActionType = None, context: str = None, fragmentMapping: AttributeMapping = None, attributeRules: AttributeRules = None) -> None:
        self.type = type
        self.context = context
        self.attributeRules = attributeRules
        self.fragment = fragment
        self.fragmentMapping = fragmentMapping

    def _validate(self) -> bool:
        return any(x for x in ["fragment"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, FragmentPolicyAction):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.context, self.attributeRules, self.fragment, self.fragmentMapping]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "context", "attributeRules", "fragment", "fragmentMapping"] and v is not None:
                if k == "type":
                    valid_data[k] = FragmentPolicyActionType[v]
                if k == "context":
                    valid_data[k] = str(v)
                if k == "attributeRules":
                    valid_data[k] = AttributeRules.from_dict(v)
                if k == "fragment":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "fragmentMapping":
                    valid_data[k] = AttributeMapping.from_dict(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["type", "context", "attributeRules", "fragment", "fragmentMapping"]:
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
