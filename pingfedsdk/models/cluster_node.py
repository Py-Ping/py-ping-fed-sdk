from enum import Enum

from pingfedsdk.enums import Mode
from pingfedsdk.enums import ReplicationStatus
from pingfedsdk.model import Model


class ClusterNode(Model):
    """Describes a node in a clustered deployment of PingFederate.

    Attributes
    ----------
    address: str
        The IP address and port this node is running on.

    index: int
        Index of the node within the cluster, or -1 if an index is not assigned.

    mode: Mode
        The deployment mode of this node, from a clustering standpoint. CLUSTERED_DUAL is not supported.

    nodeGroup: str
        The node group for this node. This field is only populated if adaptive clustering is enabled.

    version: str
        The PingFederate version this node is running on.

    nodeTags: str
        The node tags for this node. This field is only populated for engine nodes.

    configurationTimestamp: str
        The time stamp of the configuration data retrieved by this node.

    replicationStatus: ReplicationStatus
        The replication status of the node.

    """
    def __init__(self, address: str = None, index: int = None, mode: Mode = None, nodeGroup: str = None, version: str = None, nodeTags: str = None, configurationTimestamp: str = None, replicationStatus: ReplicationStatus = None) -> None:
        self.address = address
        self.index = index
        self.mode = mode
        self.nodeGroup = nodeGroup
        self.version = version
        self.nodeTags = nodeTags
        self.configurationTimestamp = configurationTimestamp
        self.replicationStatus = replicationStatus

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ClusterNode):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.address, self.index, self.mode, self.nodeGroup, self.version, self.nodeTags, self.configurationTimestamp, self.replicationStatus]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["address", "index", "mode", "nodeGroup", "version", "nodeTags", "configurationTimestamp", "replicationStatus"] and v is not None:
                if k == "address":
                    valid_data[k] = str(v)
                if k == "index":
                    valid_data[k] = int(v)
                if k == "mode":
                    valid_data[k] = Mode[v]
                if k == "nodeGroup":
                    valid_data[k] = str(v)
                if k == "version":
                    valid_data[k] = str(v)
                if k == "nodeTags":
                    valid_data[k] = str(v)
                if k == "configurationTimestamp":
                    valid_data[k] = str(v)
                if k == "replicationStatus":
                    valid_data[k] = ReplicationStatus[v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["address", "index", "mode", "nodeGroup", "version", "nodeTags", "configurationTimestamp", "replicationStatus"]:
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
