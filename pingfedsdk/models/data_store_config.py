from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.enums import DataStoreConfigType


class DataStoreConfig(Model):
    """Local identity profile data store.

    Attributes
    ----------
    type: DataStoreConfigType
        The data store config type.

    dataStoreRef: ResourceLink
        Reference to the associated data store.

    dataStoreMapping: object
        The data store mapping.

    """

    def __init__(self, dataStoreRef: ResourceLink, type: DataStoreConfigType, dataStoreMapping: object = None) -> None:
        self.type = type
        self.dataStoreRef = dataStoreRef
        self.dataStoreMapping = dataStoreMapping

    def _validate(self) -> bool:
        return any(x for x in ["dataStoreRef", "type"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, DataStoreConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.dataStoreRef, self.dataStoreMapping]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "dataStoreRef", "dataStoreMapping"] and v is not None:
                if k == "type":
                    valid_data[k] = DataStoreConfigType[v]
                if k == "dataStoreRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "dataStoreMapping":
                    valid_data[k] = object(**v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["type", "dataStoreRef", "dataStoreMapping"]:
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
