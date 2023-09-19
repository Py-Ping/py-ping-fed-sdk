from enum import Enum

from pingfedsdk.model import Model


class ServiceAssociation(Model):
    """A model representing an association between a PingFederate component (typically a plugin) and a list of PingOne services.

    Attributes
    ----------
    componentName: str
        The display name for the component.

    serviceNames: list
        The list of PingOne services consumed by the plugin. The first service represents the primary service consumed by the plugin.

    configured: bool
        Indicates whether one or more instances of the plugin are configured for a given PingOne connection.

    """
    def __init__(self, componentName: str = None, serviceNames: list = None, configured: bool = None) -> None:
        self.componentName = componentName
        self.serviceNames = serviceNames
        self.configured = configured

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ServiceAssociation):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.componentName, self.serviceNames, self.configured]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["componentName", "serviceNames", "configured"] and v is not None:
                if k == "componentName":
                    valid_data[k] = str(v)
                if k == "serviceNames":
                    valid_data[k] = [str(x) for x in v]
                if k == "configured":
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
            if k in ["componentName", "serviceNames", "configured"]:
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
