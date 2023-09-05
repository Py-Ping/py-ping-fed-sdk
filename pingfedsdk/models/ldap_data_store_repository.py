from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.enums import LdapDataStoreRepositoryType


class LdapDataStoreRepository(Model):
    """LDAP data store user repository.

    Attributes
    ----------
    type: LdapDataStoreRepositoryType
        The data store repository type.

    dataStoreRef: ResourceLink
        Reference to the associated data store.

    jitRepositoryAttributeMapping: object
        A list of user repository mappings from attribute names to their fulfillment values.

    baseDn: str
        The base DN to search from. If not specified, the search will start at the LDAP's root.

    uniqueUserIdFilter: str
        The expression that results in a unique user identifier, when combined with the Base DN.

    """

    def __init__(self, jitRepositoryAttributeMapping: object, uniqueUserIdFilter: str, type: LdapDataStoreRepositoryType = None, dataStoreRef: ResourceLink = None, baseDn: str = None) -> None:
        self.type = type
        self.dataStoreRef = dataStoreRef
        self.jitRepositoryAttributeMapping = jitRepositoryAttributeMapping
        self.baseDn = baseDn
        self.uniqueUserIdFilter = uniqueUserIdFilter

    def _validate(self) -> bool:
        return any(x for x in ["jitRepositoryAttributeMapping", "uniqueUserIdFilter"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, LdapDataStoreRepository):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.dataStoreRef, self.jitRepositoryAttributeMapping, self.baseDn, self.uniqueUserIdFilter]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "dataStoreRef", "jitRepositoryAttributeMapping", "baseDn", "uniqueUserIdFilter"] and v is not None:
                if k == "type":
                    valid_data[k] = LdapDataStoreRepositoryType[v]
                if k == "dataStoreRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "jitRepositoryAttributeMapping":
                    valid_data[k] = object(**v)
                if k == "baseDn":
                    valid_data[k] = str(v)
                if k == "uniqueUserIdFilter":
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
            if k in ["type", "dataStoreRef", "jitRepositoryAttributeMapping", "baseDn", "uniqueUserIdFilter"]:
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
