from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.enums import LdapType
from pingfedsdk.enums import DataStoreType


class PingOneLdapGatewayDataStore(Model):
    """A LDAP gateway data store.

    Attributes
    ----------
    type: DataStoreType
        The data store type.

    id: str
        The persistent, unique ID for the data store. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.

    maskAttributeValues: bool
        Whether attribute values should be masked in the log.

    name: str
        The data store name with a unique value across all data sources. Omitting this attribute will set the value to a combination of the hostname(s) and the principal.

    ldapType: LdapType
        A type that allows PingFederate to configure many provisioning settings automatically. The value is validated against the LDAP gateway configuration in PingOne unless the header 'X-BypassExternalValidation' is set to true.

    pingOneConnectionRef: ResourceLink
        Reference to the PingOne connection this gateway uses.

    pingOneEnvironmentId: str
        The environment ID that the gateway belongs to.

    pingOneLdapGatewayId: str
        The ID of the PingOne LDAP Gateway this data store uses.

    useSsl: bool
        Connects to the LDAP data store using secure SSL/TLS encryption (LDAPS). The default value is false. The value is validated against the LDAP gateway configuration in PingOne unless the header 'X-BypassExternalValidation' is set to true.

    binaryAttributes: list
        The list of LDAP attributes to be handled as binary data.

    """

    def __init__(self, ldapType: LdapType, pingOneConnectionRef: ResourceLink, pingOneEnvironmentId: str, pingOneLdapGatewayId: str, type: DataStoreType = None, id: str = None, maskAttributeValues: bool = None, name: str = None, useSsl: bool = None, binaryAttributes: list = None) -> None:
        self.type = type
        self.id = id
        self.maskAttributeValues = maskAttributeValues
        self.name = name
        self.ldapType = ldapType
        self.pingOneConnectionRef = pingOneConnectionRef
        self.pingOneEnvironmentId = pingOneEnvironmentId
        self.pingOneLdapGatewayId = pingOneLdapGatewayId
        self.useSsl = useSsl
        self.binaryAttributes = binaryAttributes

    def _validate(self) -> bool:
        return any(x for x in ["ldapType", "pingOneConnectionRef", "pingOneEnvironmentId", "pingOneLdapGatewayId"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, PingOneLdapGatewayDataStore):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.id, self.maskAttributeValues, self.name, self.ldapType, self.pingOneConnectionRef, self.pingOneEnvironmentId, self.pingOneLdapGatewayId, self.useSsl, self.binaryAttributes]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "id", "maskAttributeValues", "name", "ldapType", "pingOneConnectionRef", "pingOneEnvironmentId", "pingOneLdapGatewayId", "useSsl", "binaryAttributes"] and v is not None:
                if k == "type":
                    valid_data[k] = DataStoreType[v]
                if k == "id":
                    valid_data[k] = str(v)
                if k == "maskAttributeValues":
                    valid_data[k] = bool(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "ldapType":
                    valid_data[k] = LdapType[v]
                if k == "pingOneConnectionRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "pingOneEnvironmentId":
                    valid_data[k] = str(v)
                if k == "pingOneLdapGatewayId":
                    valid_data[k] = str(v)
                if k == "useSsl":
                    valid_data[k] = bool(v)
                if k == "binaryAttributes":
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
            if k in ["type", "id", "maskAttributeValues", "name", "ldapType", "pingOneConnectionRef", "pingOneEnvironmentId", "pingOneLdapGatewayId", "useSsl", "binaryAttributes"]:
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
