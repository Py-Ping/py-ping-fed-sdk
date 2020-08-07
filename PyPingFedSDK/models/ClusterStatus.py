class ClusterStatus():
    """Information on cluster nodes and replication status.

    Attributes
    ----------
    lastConfigUpdateTime : string
        Time when the configuration of this node was last updated.    lastReplicationTime : string
        Time when configuration changes were last replicated.    mixedMode : boolean
        Indicates whether there is more than one version of PingFederate in the cluster.    nodes : array
        List of nodes in the cluster.    replicationRequired : boolean
        Indicates whether a replication is required to propagate config updates.
    """

    __slots__ = ["lastConfigUpdateTime", "lastReplicationTime", "mixedMode", "nodes", "replicationRequired"]

    def __init__(self, lastConfigUpdateTime=None, lastReplicationTime=None, mixedMode=None, nodes=None, replicationRequired=None):
        self.lastConfigUpdateTime: str = lastConfigUpdateTime
        self.lastReplicationTime: str = lastReplicationTime
        self.mixedMode: bool = mixedMode
        self.nodes: list = nodes
        self.replicationRequired: bool = replicationRequired

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ClusterStatus):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.lastConfigUpdateTime, self.lastReplicationTime, self.mixedMode, self.nodes, self.replicationRequired))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["lastConfigUpdateTime", "lastReplicationTime", "mixedMode", "nodes", "replicationRequired"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__