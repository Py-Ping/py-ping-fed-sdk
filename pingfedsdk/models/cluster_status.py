from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.cluster_node import ClusterNode


class ClusterStatus(Model):
    """Information on cluster nodes and replication status.

    Attributes
    ----------
    nodes: list
        List of nodes in the cluster.

    lastConfigUpdateTime: str
        Time when the configuration of this node was last updated.

    lastReplicationTime: str
        Time when configuration changes were last replicated.

    replicationRequired: bool
        Indicates whether a replication is required to propagate config updates.

    mixedMode: bool
        Indicates whether there is more than one version of PingFederate in the cluster.

    """
    def __init__(self, nodes: list = None, lastConfigUpdateTime: str = None, lastReplicationTime: str = None, replicationRequired: bool = None, mixedMode: bool = None) -> None:
        self.nodes = nodes
        self.lastConfigUpdateTime = lastConfigUpdateTime
        self.lastReplicationTime = lastReplicationTime
        self.replicationRequired = replicationRequired
        self.mixedMode = mixedMode

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ClusterStatus):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.nodes, self.lastConfigUpdateTime, self.lastReplicationTime, self.replicationRequired, self.mixedMode]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["nodes", "lastConfigUpdateTime", "lastReplicationTime", "replicationRequired", "mixedMode"] and v is not None:
                if k == "nodes":
                    valid_data[k] = [ClusterNode.from_dict(x) for x in v]
                if k == "lastConfigUpdateTime":
                    valid_data[k] = str(v)
                if k == "lastReplicationTime":
                    valid_data[k] = str(v)
                if k == "replicationRequired":
                    valid_data[k] = bool(v)
                if k == "mixedMode":
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
            if k in ["nodes", "lastConfigUpdateTime", "lastReplicationTime", "replicationRequired", "mixedMode"]:
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
