from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.models.field_descriptor import FieldDescriptor


class Action(Model):
    """A read-only plugin action that either represents a file download or an arbitrary invocation performed by the plugin.

    Attributes
    ----------
    id: str
        The ID of this action.

    name: str
        The name of this action.

    description: str
        The description of this action.

    download: bool
        Whether this action will trigger a download or invoke an internal action that will return a string result.

    invocationRef: ResourceLink
        Whether this action will trigger a download or invoke an internal action that will return a string result.

    parameters: list
        List of parameters for this action.

    """

    def __init__(self, id: str = None, name: str = None, description: str = None, download: bool = None, invocationRef: ResourceLink = None, parameters: list = None) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.download = download
        self.invocationRef = invocationRef
        self.parameters = parameters

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, Action):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.name, self.description, self.download, self.invocationRef, self.parameters]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "name", "description", "download", "invocationRef", "parameters"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "description":
                    valid_data[k] = str(v)
                if k == "download":
                    valid_data[k] = bool(v)
                if k == "invocationRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "parameters":
                    valid_data[k] = [FieldDescriptor(**x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "name", "description", "download", "invocationRef", "parameters"]:
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
