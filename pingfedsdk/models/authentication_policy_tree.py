from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.authentication_policy_tree_node import AuthenticationPolicyTreeNode
from pingfedsdk.models.resource_link import ResourceLink


class AuthenticationPolicyTree(Model):
    """An authentication policy tree.

    Attributes
    ----------
    id: str
        The authentication policy ID. ID is unique.

    name: str
        The authentication policy name. Name is unique.

    description: str
        A description for the authentication policy.

    authenticationApiApplicationRef: ResourceLink
        Authentication API Application Id to be used in this policy branch. If the value is not specified, no Authentication API Application will be used.

    enabled: bool
        Whether or not this authentication policy tree is enabled. Default is true.

    rootNode: AuthenticationPolicyTreeNode
        A node inside the authentication policy tree.

    handleFailuresLocally: bool
        If a policy ends in failure keep the user local.

    """

    def __init__(self, id: str = None, name: str = None, description: str = None, authenticationApiApplicationRef: ResourceLink = None, enabled: bool = None, rootNode: AuthenticationPolicyTreeNode = None, handleFailuresLocally: bool = None) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.authenticationApiApplicationRef = authenticationApiApplicationRef
        self.enabled = enabled
        self.rootNode = rootNode
        self.handleFailuresLocally = handleFailuresLocally

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthenticationPolicyTree):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.name, self.description, self.authenticationApiApplicationRef, self.enabled, self.rootNode, self.handleFailuresLocally]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "name", "description", "authenticationApiApplicationRef", "enabled", "rootNode", "handleFailuresLocally"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "description":
                    valid_data[k] = str(v)
                if k == "authenticationApiApplicationRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "enabled":
                    valid_data[k] = bool(v)
                if k == "rootNode":
                    valid_data[k] = AuthenticationPolicyTreeNode(**v)
                if k == "handleFailuresLocally":
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
            if k in ["id", "name", "description", "authenticationApiApplicationRef", "enabled", "rootNode", "handleFailuresLocally"]:
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
