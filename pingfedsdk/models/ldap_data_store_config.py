from enum import Enum

from pingfedsdk.enums import LdapDataStoreConfigType
from pingfedsdk.model import Model
from pingfedsdk.models.data_store_attribute import DataStoreAttribute
from pingfedsdk.models.resource_link import ResourceLink


class LdapDataStoreConfig(Model):
    """LDAP data store configuration.

    Attributes
    ----------
    type: LdapDataStoreConfigType
        The data store config type.

    dataStoreRef: ResourceLink
        Reference to the associated data store.

    dataStoreMapping: dict
        The data store mapping.

    baseDn: str
        The base DN to search from. If not specified, the search will start at the LDAP's root.

    createPattern: str
        The Relative DN Pattern that will be used to create objects in the directory.

    objectClass: str
        The Object Class used by the new objects stored in the LDAP data store.

    auxiliaryObjectClasses: list
        The Auxiliary Object Classes used by the new objects stored in the LDAP data store.

    """
    def __init__(self, baseDn: str, createPattern: str, objectClass: str, dataStoreMapping: dict, type: LdapDataStoreConfigType = None, dataStoreRef: ResourceLink = None, auxiliaryObjectClasses: list = None) -> None:
        self.type = type
        self.dataStoreRef = dataStoreRef
        self.dataStoreMapping = dataStoreMapping
        self.baseDn = baseDn
        self.createPattern = createPattern
        self.objectClass = objectClass
        self.auxiliaryObjectClasses = auxiliaryObjectClasses

    def _validate(self) -> bool:
        return any(x for x in ["baseDn", "createPattern", "dataStoreMapping", "objectClass"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, LdapDataStoreConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.dataStoreRef, self.dataStoreMapping, self.baseDn, self.createPattern, self.objectClass, self.auxiliaryObjectClasses]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "dataStoreRef", "dataStoreMapping", "baseDn", "createPattern", "objectClass", "auxiliaryObjectClasses"] and v is not None:
                if k == "type":
                    valid_data[k] = LdapDataStoreConfigType[v]
                if k == "dataStoreRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "dataStoreMapping":
                    valid_data[k] = {str(x): DataStoreAttribute.from_dict(y) for x, y in v.items()}
                if k == "baseDn":
                    valid_data[k] = str(v)
                if k == "createPattern":
                    valid_data[k] = str(v)
                if k == "objectClass":
                    valid_data[k] = str(v)
                if k == "auxiliaryObjectClasses":
                    valid_data[k] = [str(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["type", "dataStoreRef", "dataStoreMapping", "baseDn", "createPattern", "objectClass", "auxiliaryObjectClasses"]:
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
