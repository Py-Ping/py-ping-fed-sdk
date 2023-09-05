from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.saas_attribute_mapping import SaasAttributeMapping
from pingfedsdk.models.channel_source import ChannelSource


class Channel(Model):
    """A channel is a combination of a source data store and a provisioning target. It include settings of a source data store, managing provisioning threads and mapping of attributes.

    Attributes
    ----------
    active: bool
        Indicates whether the channel is the active channel for this connection.

    channelSource: ChannelSource
        The LDAP settings that apply to the source user-data store.

    attributeMapping: list
        The mapping of attributes from the local data store into Fields specified by the service provider.

    name: str
        The name of the channel.

    maxThreads: int
        The number of processing threads. The default value is 1.

    timeout: int
        Timeout is the number of seconds that can be adjusted if more time is needed for provisioning a large amount of data. It is applicable when the number of processing thread is more than 1. The default value is 60.

    """

    def __init__(self, active: bool, attributeMapping: list, channelSource: ChannelSource, maxThreads: int, name: str, timeout: int) -> None:
        self.active = active
        self.channelSource = channelSource
        self.attributeMapping = attributeMapping
        self.name = name
        self.maxThreads = maxThreads
        self.timeout = timeout

    def _validate(self) -> bool:
        return any(x for x in ["active", "attributeMapping", "channelSource", "maxThreads", "name", "timeout"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, Channel):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.active, self.channelSource, self.attributeMapping, self.name, self.maxThreads, self.timeout]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["active", "channelSource", "attributeMapping", "name", "maxThreads", "timeout"] and v is not None:
                if k == "active":
                    valid_data[k] = bool(v)
                if k == "channelSource":
                    valid_data[k] = ChannelSource(**v)
                if k == "attributeMapping":
                    valid_data[k] = [SaasAttributeMapping(**x) for x in v]
                if k == "name":
                    valid_data[k] = str(v)
                if k == "maxThreads":
                    valid_data[k] = int(v)
                if k == "timeout":
                    valid_data[k] = int(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["active", "channelSource", "attributeMapping", "name", "maxThreads", "timeout"]:
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
