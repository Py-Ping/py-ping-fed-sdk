from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.enums import AuthnSelectorPolicyActionType


class AuthnSelectorPolicyAction(Model):
    """An authentication selector selection action.

    Attributes
    ----------
    type: AuthnSelectorPolicyActionType
        The authentication selection type.

    context: str
        The result context.

    authenticationSelectorRef: ResourceLink
        Reference to the associated authentication selector.

    """

    def __init__(self, authenticationSelectorRef: ResourceLink, type: AuthnSelectorPolicyActionType = None, context: str = None) -> None:
        self.type = type
        self.context = context
        self.authenticationSelectorRef = authenticationSelectorRef

    def _validate(self) -> bool:
        return any(x for x in ["authenticationSelectorRef"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthnSelectorPolicyAction):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.context, self.authenticationSelectorRef]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "context", "authenticationSelectorRef"] and v is not None:
                if k == "type":
                    valid_data[k] = AuthnSelectorPolicyActionType[v]
                if k == "context":
                    valid_data[k] = str(v)
                if k == "authenticationSelectorRef":
                    valid_data[k] = ResourceLink(**v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["type", "context", "authenticationSelectorRef"]:
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
