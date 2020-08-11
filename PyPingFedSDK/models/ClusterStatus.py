class ClusterStatus():
    """Information on cluster nodes and replication status.

    Attributes
    ----------
    lastConfigUpdateTime : string
 Time when the configuration of this node was last updated.
    lastReplicationTime : string
 Time when configuration changes were last replicated.
    mixedMode : boolean
 Indicates whether there is more than one version of PingFederate in the cluster.
    nodes : array
 List of nodes in the cluster.
    replicationRequired : boolean
 Indicates whether a replication is required to propagate config updates.

    """

    def __init__(self, lastConfigUpdateTime:str=None, lastReplicationTime:str=None, mixedMode:bool=None, nodes:list=None, replicationRequired:bool=None) -> None:
        self.lastConfigUpdateTime = lastConfigUpdateTime
        self.lastReplicationTime = lastReplicationTime
        self.mixedMode = mixedMode
        self.nodes = nodes
        self.replicationRequired = replicationRequired

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ClusterStatus):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.lastConfigUpdateTime, self.lastReplicationTime, self.mixedMode, self.nodes, self.replicationRequired))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["lastConfigUpdateTime", "lastReplicationTime", "mixedMode", "nodes", "replicationRequired"]}

        return cls(**valid_data)