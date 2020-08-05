class OutboundProvisionDatabase():
    """The settings for database used internally to facilitate outbound provisioning. The database stores state of synchronization between the source data store and the target data store.

    Attributes
    ----------
    dataStoreRef : str
        Reference to the associated data store.    synchronizationFrequency : integer
        The synchronization frequency in seconds. The default value is 60.
    """

    __slots__ = ["dataStoreRef", "synchronizationFrequency"]

    def __init__(self, dataStoreRef, synchronizationFrequency=None):
        self.dataStoreRef = dataStoreRef
        self.synchronizationFrequency = synchronizationFrequency

    def _validate(self):
        return any(x for x in ['dataStoreRef'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, OutboundProvisionDatabase):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.dataStoreRef, self.synchronizationFrequency))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["dataStoreRef", "synchronizationFrequency"]}

        return cls(**valid_data)
