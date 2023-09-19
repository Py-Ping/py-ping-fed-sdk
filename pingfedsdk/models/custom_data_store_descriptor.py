from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.plugin_config_descriptor import PluginConfigDescriptor


class CustomDataStoreDescriptor(Model):
    """A custom data store descriptor.

    Attributes
    ----------
    id: str
        Unique ID of the plugin.

    name: str
        Friendly name for the plugin.

    className: str
        Full class name of the class that implements this plugin.

    attributeContract: list
        The attribute contract for this plugin.

    supportsExtendedContract: bool
        Determines whether this plugin supports extending the attribute contract.

    configDescriptor: PluginConfigDescriptor
        The descriptor which defines the configuration fields available for this plugin.

    """
    def __init__(self, id: str = None, name: str = None, className: str = None, attributeContract: list = None, supportsExtendedContract: bool = None, configDescriptor: PluginConfigDescriptor = None) -> None:
        self.id = id
        self.name = name
        self.className = className
        self.attributeContract = attributeContract
        self.supportsExtendedContract = supportsExtendedContract
        self.configDescriptor = configDescriptor

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, CustomDataStoreDescriptor):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.name, self.className, self.attributeContract, self.supportsExtendedContract, self.configDescriptor]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "name", "className", "attributeContract", "supportsExtendedContract", "configDescriptor"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "className":
                    valid_data[k] = str(v)
                if k == "attributeContract":
                    valid_data[k] = [str(x) for x in v]
                if k == "supportsExtendedContract":
                    valid_data[k] = bool(v)
                if k == "configDescriptor":
                    valid_data[k] = PluginConfigDescriptor.from_dict(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "name", "className", "attributeContract", "supportsExtendedContract", "configDescriptor"]:
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
