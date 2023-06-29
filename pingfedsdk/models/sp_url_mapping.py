from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.enums import SpUrlMappingType


class SpUrlMapping(Model):
    """SP URL mapping

    Attributes
    ----------
    url: str
        The URL that will be compared against the target URL. Use a wildcard (*) to match multiple URLs to the same adapter or connection instance.

    type: SpUrlMappingType
        The URL mapping type

    ref: ResourceLink
        The adapter or connection instance mapped for this URL.

    """

    def __init__(self, url: str = None, type: SpUrlMappingType = None, ref: ResourceLink = None) -> None:
        self.url = url
        self.type = type
        self.ref = ref

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SpUrlMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.url, self.type, self.ref]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["url", "type", "ref"] and v is not None:
                if k == "url":
                    valid_data[k] = str(v)
                if k == "type":
                    valid_data[k] = SpUrlMappingType[v]
                if k == "ref":
                    valid_data[k] = ResourceLink(**v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["url", "type", "ref"]:
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
