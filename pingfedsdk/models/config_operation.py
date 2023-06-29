from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.enums import OperationType


class ConfigOperation(Model):
    """Model describing a list of configuration operations for a given resource type.

    Attributes
    ----------
    resourceType: str
        The identifier for the resource type the operation applies to.

    subResource: str
        The subresource for the operation.

    operationType: OperationType
        The type of operation to be performed.

    items: list
        The configuration items for the operation. This field only applies to the SAVE operation type.

    itemIds: list
        The item ID's for the operation. This field only applies to the DELETE operation type.

    """

    def __init__(self, operationType: OperationType, resourceType: str, subResource: str = None, items: list = None, itemIds: list = None) -> None:
        self.resourceType = resourceType
        self.subResource = subResource
        self.operationType = operationType
        self.items = items
        self.itemIds = itemIds

    def _validate(self) -> bool:
        return any(x for x in ["operationType", "resourceType"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ConfigOperation):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.resourceType, self.subResource, self.operationType, self.items, self.itemIds]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["resourceType", "subResource", "operationType", "items", "itemIds"] and v is not None:
                if k == "resourceType":
                    valid_data[k] = str(v)
                if k == "subResource":
                    valid_data[k] = str(v)
                if k == "operationType":
                    valid_data[k] = OperationType[v]
                if k == "items":
                    valid_data[k] = v
                if k == "itemIds":
                    valid_data[k] = [str(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["resourceType", "subResource", "operationType", "items", "itemIds"]:
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
