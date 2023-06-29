from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.attribute_query_name_mapping import AttributeQueryNameMapping
from pingfedsdk.models.idp_attribute_query_policy import IdpAttributeQueryPolicy


class IdpAttributeQuery(Model):
    """The attribute query profile supports local applications in requesting user attributes from an attribute authority.

    Attributes
    ----------
    url: str
        The URL at your IdP partner's site where attribute queries are to be sent.

    nameMappings: list
        The attribute name mappings between the SP and the IdP.

    policy: IdpAttributeQueryPolicy
        The attribute query profile's security policy.

    """

    def __init__(self, url: str, nameMappings: list = None, policy: IdpAttributeQueryPolicy = None) -> None:
        self.url = url
        self.nameMappings = nameMappings
        self.policy = policy

    def _validate(self) -> bool:
        return any(x for x in ["url"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpAttributeQuery):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.url, self.nameMappings, self.policy]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["url", "nameMappings", "policy"] and v is not None:
                if k == "url":
                    valid_data[k] = str(v)
                if k == "nameMappings":
                    valid_data[k] = [AttributeQueryNameMapping(**x) for x in v]
                if k == "policy":
                    valid_data[k] = IdpAttributeQueryPolicy(**v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["url", "nameMappings", "policy"]:
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
