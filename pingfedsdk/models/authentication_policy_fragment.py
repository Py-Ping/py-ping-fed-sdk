from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.models.authentication_policy_tree_node import AuthenticationPolicyTreeNode


class AuthenticationPolicyFragment(Model):
    """An authentication policy fragment.

    Attributes
    ----------
    id: str
        The authentication policy fragment ID. ID is unique.

    name: str
        The authentication policy fragment name. Name is unique.

    description: str
        A description for the authentication policy fragment.

    rootNode: AuthenticationPolicyTreeNode
        The beginning action for the authentication fragment policy.

    inputs: ResourceLink
        The reference to the authentication policy contract to use as the attribute inputs for this authentication policy fragment.

    outputs: ResourceLink
        The reference to the authentication policy contract to use as the attribute outputs for this authentication policy fragment.

    """

    def __init__(self, id: str = None, name: str = None, description: str = None, rootNode: AuthenticationPolicyTreeNode = None, inputs: ResourceLink = None, outputs: ResourceLink = None) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.rootNode = rootNode
        self.inputs = inputs
        self.outputs = outputs

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthenticationPolicyFragment):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.name, self.description, self.rootNode, self.inputs, self.outputs]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "name", "description", "rootNode", "inputs", "outputs"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "description":
                    valid_data[k] = str(v)
                if k == "rootNode":
                    valid_data[k] = AuthenticationPolicyTreeNode(**v)
                if k == "inputs":
                    valid_data[k] = ResourceLink(**v)
                if k == "outputs":
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
            if k in ["id", "name", "description", "rootNode", "inputs", "outputs"]:
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
