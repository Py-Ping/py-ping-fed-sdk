from enum import Enum

from pingfedsdk.model import Model


class SpAdapterTargetApplicationInfo(Model):
    """Target Application Information exposed by an SP adapter.

    Attributes
    ----------
    applicationName: str
        The application name.

    applicationIconUrl: str
        The application icon URL.

    inherited: bool
        Specifies Whether target application information is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false.

    """
    def __init__(self, applicationName: str = None, applicationIconUrl: str = None, inherited: bool = None) -> None:
        self.applicationName = applicationName
        self.applicationIconUrl = applicationIconUrl
        self.inherited = inherited

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SpAdapterTargetApplicationInfo):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.applicationName, self.applicationIconUrl, self.inherited]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["applicationName", "applicationIconUrl", "inherited"] and v is not None:
                if k == "applicationName":
                    valid_data[k] = str(v)
                if k == "applicationIconUrl":
                    valid_data[k] = str(v)
                if k == "inherited":
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
            if k in ["applicationName", "applicationIconUrl", "inherited"]:
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
