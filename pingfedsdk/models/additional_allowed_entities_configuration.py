from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.entity import Entity


class AdditionalAllowedEntitiesConfiguration(Model):
    """Additional allowed entities or issuers configuration. Currently only used in OIDC IdP (RP) connection.

    Attributes
    ----------
    allowAdditionalEntities: bool
        Set to true to configure additional entities or issuers to be accepted during entity or issuer validation.

    allowAllEntities: bool
        Set to true to accept any entity or issuer during entity or issuer validation. (Not Recommended)

    additionalAllowedEntities: list
        An array of additional allowed entities or issuers to be accepted during entity or issuer validation.

    """

    def __init__(self, allowAdditionalEntities: bool = None, allowAllEntities: bool = None, additionalAllowedEntities: list = None) -> None:
        self.allowAdditionalEntities = allowAdditionalEntities
        self.allowAllEntities = allowAllEntities
        self.additionalAllowedEntities = additionalAllowedEntities

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AdditionalAllowedEntitiesConfiguration):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.allowAdditionalEntities, self.allowAllEntities, self.additionalAllowedEntities]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["allowAdditionalEntities", "allowAllEntities", "additionalAllowedEntities"] and v is not None:
                if k == "allowAdditionalEntities":
                    valid_data[k] = bool(v)
                if k == "allowAllEntities":
                    valid_data[k] = bool(v)
                if k == "additionalAllowedEntities":
                    valid_data[k] = [Entity(**x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["allowAdditionalEntities", "allowAllEntities", "additionalAllowedEntities"]:
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
