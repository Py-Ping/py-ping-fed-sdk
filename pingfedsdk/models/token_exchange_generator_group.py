from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.token_exchange_generator_mapping import TokenExchangeGeneratorMapping


class TokenExchangeGeneratorGroup(Model):
    """The set of attributes used to configure a OAuth 2.0 Token Exchange Generator group.

    Attributes
    ----------
    id: str
        The Token Exchange Generator group ID. ID is unique.

    name: str
        The Token Exchange Generator group name. Name is unique.

    resourceUris: list
        The list of  resource URI's which map to this Token Exchange Generator group.

    generatorMappings: list
        A list of Token Generator mapping into an OAuth 2.0 Token Exchange requested token type.

    """
    def __init__(self, id: str, name: str, generatorMappings: list, resourceUris: list = None) -> None:
        self.id = id
        self.name = name
        self.resourceUris = resourceUris
        self.generatorMappings = generatorMappings

    def _validate(self) -> bool:
        return any(x for x in ["generatorMappings", "id", "name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, TokenExchangeGeneratorGroup):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.name, self.resourceUris, self.generatorMappings]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "name", "resourceUris", "generatorMappings"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "resourceUris":
                    valid_data[k] = [str(x) for x in v]
                if k == "generatorMappings":
                    valid_data[k] = [TokenExchangeGeneratorMapping.from_dict(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "name", "resourceUris", "generatorMappings"]:
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
