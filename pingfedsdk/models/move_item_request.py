from enum import Enum

from pingfedsdk.enums import Location
from pingfedsdk.model import Model


class MoveItemRequest(Model):
    """Metadata from a request about where to move a resource

    Attributes
    ----------
    location: Location
        Enumeration for where to move the item.

    moveToId: str
        When moving an item relative to another, this value indicates the target move-to ID.

    """
    def __init__(self, location: Location, moveToId: str = None) -> None:
        self.location = location
        self.moveToId = moveToId

    def _validate(self) -> bool:
        return any(x for x in ["location"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, MoveItemRequest):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.location, self.moveToId]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["location", "moveToId"] and v is not None:
                if k == "location":
                    valid_data[k] = Location[v]
                if k == "moveToId":
                    valid_data[k] = str(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["location", "moveToId"]:
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
