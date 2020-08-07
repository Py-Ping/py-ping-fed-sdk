class Channel():
    """A channel is a combination of a source data store and a provisioning target. It include settings of a source data store, managing provisioning threads and mapping of attributes.

    Attributes
    ----------
    active : boolean
 Indicates whether the channel is the active channel for this connection.
    attributeMapping : array
 The mapping of attributes from the local data store into Fields specified by the service provider.
    channelSource : str
 The LDAP settings that apply to the source user-data store.
    maxThreads : integer
 The number of processing threads. The default value is 1.
    name : string
 The name of the channel.
    timeout : integer
 Timeout is the number of seconds that can be adjusted if more time is needed for provisioning a large amount of data. It is applicable when the number of processing thread is more than 1. The default value is 60.

    """

    def __init__(self, active, channelSource, attributeMapping, name, maxThreads, timeout) -> None:
        self.active = active
        self.attributeMapping = attributeMapping
        self.channelSource = channelSource
        self.maxThreads = maxThreads
        self.name = name
        self.timeout = timeout

    def _validate(self) -> bool:
        return any(x for x in ["active", "channelSource", "attributeMapping", "name", "maxThreads", "timeout"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Channel):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.active, self.attributeMapping, self.channelSource, self.maxThreads, self.name, self.timeout))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["active", "attributeMapping", "channelSource", "maxThreads", "name", "timeout"]}

        return cls(**valid_data)