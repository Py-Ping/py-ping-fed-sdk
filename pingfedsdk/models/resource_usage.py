from enum import Enum

from pingfedsdk.enums import ResourceCategory
from pingfedsdk.model import Model
from pingfedsdk.models.resource_link import ResourceLink


class ResourceUsage(Model):
    """An API model representing a reference to an API resource.

    Attributes
    ----------
    id: str
        The ID of the referencing resource.

    name: str
        The name of the referencing resource.

    categoryId: ResourceCategory
        The category of the referencing resource.

    type: str
        The type of the referencing resource. In the case of plugins, this is the plugin type. Otherwise, it is usually the same as the name of the category.

    ref: ResourceLink
        A link to the referencing resource.

    """
    def __init__(self, id: str = None, name: str = None, categoryId: ResourceCategory = None, type: str = None, ref: ResourceLink = None) -> None:
        self.id = id
        self.name = name
        self.categoryId = categoryId
        self.type = type
        self.ref = ref

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ResourceUsage):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.name, self.categoryId, self.type, self.ref]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "name", "categoryId", "type", "ref"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "categoryId":
                    valid_data[k] = ResourceCategory[v]
                if k == "type":
                    valid_data[k] = str(v)
                if k == "ref":
                    valid_data[k] = ResourceLink.from_dict(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "name", "categoryId", "type", "ref"]:
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
