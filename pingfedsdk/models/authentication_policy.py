from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.authentication_policy_tree import AuthenticationPolicyTree
from pingfedsdk.models.authentication_source import AuthenticationSource


class AuthenticationPolicy(Model):
    """An authentication policy.

    Attributes
    ----------
    failIfNoSelection: bool
        Fail if policy finds no authentication source.

    authnSelectionTrees: list
        The list of authentication policy trees.

    defaultAuthenticationSources: list
        The default authentication sources.

    trackedHttpParameters: list
        The HTTP request parameters to track and make available to authentication sources, selectors, and contract mappings throughout the authentication policy.

    """

    def __init__(self, failIfNoSelection: bool = None, authnSelectionTrees: list = None, defaultAuthenticationSources: list = None, trackedHttpParameters: list = None) -> None:
        self.failIfNoSelection = failIfNoSelection
        self.authnSelectionTrees = authnSelectionTrees
        self.defaultAuthenticationSources = defaultAuthenticationSources
        self.trackedHttpParameters = trackedHttpParameters

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthenticationPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.failIfNoSelection, self.authnSelectionTrees, self.defaultAuthenticationSources, self.trackedHttpParameters]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["failIfNoSelection", "authnSelectionTrees", "defaultAuthenticationSources", "trackedHttpParameters"] and v is not None:
                if k == "failIfNoSelection":
                    valid_data[k] = bool(v)
                if k == "authnSelectionTrees":
                    valid_data[k] = [AuthenticationPolicyTree(**x) for x in v]
                if k == "defaultAuthenticationSources":
                    valid_data[k] = [AuthenticationSource(**x) for x in v]
                if k == "trackedHttpParameters":
                    valid_data[k] = [str(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["failIfNoSelection", "authnSelectionTrees", "defaultAuthenticationSources", "trackedHttpParameters"]:
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
