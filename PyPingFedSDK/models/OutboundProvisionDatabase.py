class OutboundProvisionDatabase():
    """The settings for database used internally to facilitate outbound provisioning. The database stores state of synchronization between the source data store and the target data store.

    Attributes
    ----------
    dataStoreRef : str
 Reference to the associated data store.
    synchronizationFrequency : integer
 The synchronization frequency in seconds. The default value is 60.

    """

    def __init__(self, dataStoreRef, synchronizationFrequency:int=None) -> None:
        self.dataStoreRef = dataStoreRef
        self.synchronizationFrequency = synchronizationFrequency

    def _validate(self) -> bool:
        return any(x for x in ["dataStoreRef"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, OutboundProvisionDatabase):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.dataStoreRef, self.synchronizationFrequency))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["dataStoreRef", "synchronizationFrequency"]}

        return cls(**valid_data)