from enum import Enum

from pingfedsdk.enums import LdapInboundProvisioningUserRepositoryType
from pingfedsdk.model import Model
from pingfedsdk.models.resource_link import ResourceLink


class LdapInboundProvisioningUserRepository(Model):
    """LDAP Active Directory data store user repository

    Attributes
    ----------
    type: LdapInboundProvisioningUserRepositoryType
        The user repository type.

    dataStoreRef: ResourceLink
        Reference to the associated data store.

    baseDn: str
        The base DN to search from. If not specified, the search will start at the LDAP's root.

    uniqueUserIdFilter: str
        The expression that results in a unique user identifier, when combined with the Base DN.

    uniqueGroupIdFilter: str
        The expression that results in a unique group identifier, when combined with the Base DN.

    """
    def __init__(self, dataStoreRef: ResourceLink, uniqueUserIdFilter: str, uniqueGroupIdFilter: str, type: LdapInboundProvisioningUserRepositoryType = None, baseDn: str = None) -> None:
        self.type = type
        self.dataStoreRef = dataStoreRef
        self.baseDn = baseDn
        self.uniqueUserIdFilter = uniqueUserIdFilter
        self.uniqueGroupIdFilter = uniqueGroupIdFilter

    def _validate(self) -> bool:
        return any(x for x in ["dataStoreRef", "uniqueGroupIdFilter", "uniqueUserIdFilter"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, LdapInboundProvisioningUserRepository):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.dataStoreRef, self.baseDn, self.uniqueUserIdFilter, self.uniqueGroupIdFilter]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "dataStoreRef", "baseDn", "uniqueUserIdFilter", "uniqueGroupIdFilter"] and v is not None:
                if k == "type":
                    valid_data[k] = LdapInboundProvisioningUserRepositoryType[v]
                if k == "dataStoreRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "baseDn":
                    valid_data[k] = str(v)
                if k == "uniqueUserIdFilter":
                    valid_data[k] = str(v)
                if k == "uniqueGroupIdFilter":
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
            if k in ["type", "dataStoreRef", "baseDn", "uniqueUserIdFilter", "uniqueGroupIdFilter"]:
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
