from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.plugin_config_descriptor import PluginConfigDescriptor
from pingfedsdk.models.saas_plugin_field_info_descriptor import SaasPluginFieldInfoDescriptor


class SaasPluginDescriptor(Model):
    """A SaaS Plugin.

    Attributes
    ----------
    id: str
        The SaaS plugin type.

    description: str
        The SaaS plugin description.

    configDescriptor: PluginConfigDescriptor
        The plugin configuration that includes information to access the target service provider.

    saasPluginFieldInfoDescriptors: list
        The SaaS plugin attribute list for mapping from the local data store into Fields specified by the service provide.

    """
    def __init__(self, id: str = None, description: str = None, configDescriptor: PluginConfigDescriptor = None, saasPluginFieldInfoDescriptors: list = None) -> None:
        self.id = id
        self.description = description
        self.configDescriptor = configDescriptor
        self.saasPluginFieldInfoDescriptors = saasPluginFieldInfoDescriptors

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SaasPluginDescriptor):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.description, self.configDescriptor, self.saasPluginFieldInfoDescriptors]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "description", "configDescriptor", "saasPluginFieldInfoDescriptors"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "description":
                    valid_data[k] = str(v)
                if k == "configDescriptor":
                    valid_data[k] = PluginConfigDescriptor.from_dict(v)
                if k == "saasPluginFieldInfoDescriptors":
                    valid_data[k] = [SaasPluginFieldInfoDescriptor.from_dict(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "description", "configDescriptor", "saasPluginFieldInfoDescriptors"]:
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
