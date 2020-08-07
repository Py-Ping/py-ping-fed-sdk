class ClusterNode():
    """Describes a node in a clustered deployment of PingFederate.

    Attributes
    ----------
    address : string
        The IP address and port this node is running on.    index : integer
        Index of the node within the cluster, or -1 if an index is not assigned.    mode : str
        The deployment mode of this node, from a clustering standpoint.    nodeGroup : string
        The node group for this node. This field is only populated if adaptive clustering is enabled.    nodeTags : string
        The node tags for this node. This field is only populated for engine nodes.    version : string
        The PingFederate version this node is running on.
    """

    __slots__ = ["address", "index", "mode", "nodeGroup", "nodeTags", "version"]

    def __init__(self, address=None, index=None, mode=None, nodeGroup=None, nodeTags=None, version=None):
        self.address: str = address
        self.index: str = index
        self.mode: str = mode
        self.nodeGroup: str = nodeGroup
        self.nodeTags: str = nodeTags
        self.version: str = version

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ClusterNode):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.address, self.index, self.mode, self.nodeGroup, self.nodeTags, self.version))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["address", "index", "mode", "nodeGroup", "nodeTags", "version"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__