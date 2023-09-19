from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.models.signing_keys import SigningKeys


class AdditionalKeySet(Model):
    """The attributes used to configure an OAuth/OpenID Connect additional signing key set with virtual issuers.

    Attributes
    ----------
    id: str
        The unique ID for the key set. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.

    name: str
        The key set name.

    description: str
        A description of the key set.

    signingKeys: SigningKeys
        A set of references to the keys.

    issuers: list
        A list of virtual issuers that will use the current key set. Once assigned to a key set, the same virtual issuer cannot be assigned to another key set instance.

    """
    def __init__(self, name: str, signingKeys: SigningKeys, issuers: list, id: str = None, description: str = None) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.signingKeys = signingKeys
        self.issuers = issuers

    def _validate(self) -> bool:
        return any(x for x in ["issuers", "name", "signingKeys"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AdditionalKeySet):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.name, self.description, self.signingKeys, self.issuers]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "name", "description", "signingKeys", "issuers"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "description":
                    valid_data[k] = str(v)
                if k == "signingKeys":
                    valid_data[k] = SigningKeys.from_dict(v)
                if k == "issuers":
                    valid_data[k] = [ResourceLink.from_dict(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "name", "description", "signingKeys", "issuers"]:
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
