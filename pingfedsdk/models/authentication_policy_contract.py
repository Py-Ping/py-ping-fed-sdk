from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.authentication_policy_contract_attribute import AuthenticationPolicyContractAttribute


class AuthenticationPolicyContract(Model):
    """Authentication Policy Contracts carry user attributes from the identity provider to the service provider.

    Attributes
    ----------
    id: str
        The persistent, unique ID for the authentication policy contract. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.

    name: str
        The Authentication Policy Contract Name. Name is unique.

    coreAttributes: list
        A list of read-only assertion attributes (for example, subject) that are automatically populated by PingFederate.

    extendedAttributes: list
        A list of additional attributes as needed.

    """
    def __init__(self, id: str = None, name: str = None, coreAttributes: list = None, extendedAttributes: list = None) -> None:
        self.id = id
        self.name = name
        self.coreAttributes = coreAttributes
        self.extendedAttributes = extendedAttributes

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthenticationPolicyContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.name, self.coreAttributes, self.extendedAttributes]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "name", "coreAttributes", "extendedAttributes"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "coreAttributes":
                    valid_data[k] = [AuthenticationPolicyContractAttribute.from_dict(x) for x in v]
                if k == "extendedAttributes":
                    valid_data[k] = [AuthenticationPolicyContractAttribute.from_dict(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "name", "coreAttributes", "extendedAttributes"]:
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
