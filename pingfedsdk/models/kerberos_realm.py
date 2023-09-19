from enum import Enum

from pingfedsdk.enums import ConnectionType
from pingfedsdk.model import Model
from pingfedsdk.models.kerberos_key_set import KerberosKeySet
from pingfedsdk.models.resource_link import ResourceLink


class KerberosRealm(Model):
    """

    Attributes
    ----------
    id: str
        The persistent, unique ID for the Kerberos Realm. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified.

    kerberosRealmName: str
        The Domain/Realm name used for display in UI screens.

    connectionType: ConnectionType
        Controls how PingFederate connects to the Active Directory/Kerberos Realm. The default is: "DIRECT".

    keyDistributionCenters: list
        The Domain Controller/Key Distribution Center Host Action Names. Only applicable when 'connectionType' is "DIRECT".

    kerberosUsername: str
        The Domain/Realm username. Only required when 'connectionType' is "DIRECT".

    kerberosPassword: str
        The Domain/Realm password. GETs will not return this attribute. To update this field, specify the new value in this attribute. Only applicable when 'connectionType' is "DIRECT".

    kerberosEncryptedPassword: str
        For GET requests, this field contains the encrypted Domain/Realm password, if one exists. For POST and PUT requests, if you wish to reuse the existing password, this field should be passed back unchanged. Only applicable when 'connectionType' is "DIRECT".

    keySets: list
        A list of key sets for validating Kerberos tickets. On POST or PUT, if 'retainPreviousKeysOnPasswordChange' is true, PingFederate automatically adds the key set for the current password to this list and removes expired key sets. If 'retainPreviousKeysOnPasswordChange' is false, this list is cleared. Only applicable when 'connectionType' is "DIRECT".

    retainPreviousKeysOnPasswordChange: bool
        Determines whether the previous encryption keys are retained when the password is updated. Retaining the previous keys allows existing Kerberos tickets to continue to be validated. The default is false. Only applicable when 'connectionType' is "DIRECT".

    suppressDomainNameConcatenation: bool
        Controls whether the KDC hostnames and the realm name are concatenated in the auto-generated krb5.conf file. Default is false. Only applicable when 'connectionType' is "DIRECT".

    ldapGatewayDataStoreRef: ResourceLink
        The LDAP gateway used by PingFederate to communicate with the Active Directory. Only required when 'connectionType' is "LDAP_GATEWAY".

    """
    def __init__(self, kerberosRealmName: str, id: str = None, connectionType: ConnectionType = None, keyDistributionCenters: list = None, kerberosUsername: str = None, kerberosPassword: str = None, kerberosEncryptedPassword: str = None, keySets: list = None, retainPreviousKeysOnPasswordChange: bool = None, suppressDomainNameConcatenation: bool = None, ldapGatewayDataStoreRef: ResourceLink = None) -> None:
        self.id = id
        self.kerberosRealmName = kerberosRealmName
        self.connectionType = connectionType
        self.keyDistributionCenters = keyDistributionCenters
        self.kerberosUsername = kerberosUsername
        self.kerberosPassword = kerberosPassword
        self.kerberosEncryptedPassword = kerberosEncryptedPassword
        self.keySets = keySets
        self.retainPreviousKeysOnPasswordChange = retainPreviousKeysOnPasswordChange
        self.suppressDomainNameConcatenation = suppressDomainNameConcatenation
        self.ldapGatewayDataStoreRef = ldapGatewayDataStoreRef

    def _validate(self) -> bool:
        return any(x for x in ["kerberosRealmName"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, KerberosRealm):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.kerberosRealmName, self.connectionType, self.keyDistributionCenters, self.kerberosUsername, self.kerberosPassword, self.kerberosEncryptedPassword, self.keySets, self.retainPreviousKeysOnPasswordChange, self.suppressDomainNameConcatenation, self.ldapGatewayDataStoreRef]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "kerberosRealmName", "connectionType", "keyDistributionCenters", "kerberosUsername", "kerberosPassword", "kerberosEncryptedPassword", "keySets", "retainPreviousKeysOnPasswordChange", "suppressDomainNameConcatenation", "ldapGatewayDataStoreRef"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "kerberosRealmName":
                    valid_data[k] = str(v)
                if k == "connectionType":
                    valid_data[k] = ConnectionType[v]
                if k == "keyDistributionCenters":
                    valid_data[k] = [str(x) for x in v]
                if k == "kerberosUsername":
                    valid_data[k] = str(v)
                if k == "kerberosPassword":
                    valid_data[k] = str(v)
                if k == "kerberosEncryptedPassword":
                    valid_data[k] = str(v)
                if k == "keySets":
                    valid_data[k] = [KerberosKeySet.from_dict(x) for x in v]
                if k == "retainPreviousKeysOnPasswordChange":
                    valid_data[k] = bool(v)
                if k == "suppressDomainNameConcatenation":
                    valid_data[k] = bool(v)
                if k == "ldapGatewayDataStoreRef":
                    valid_data[k] = ResourceLink.from_dict(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "kerberosRealmName", "connectionType", "keyDistributionCenters", "kerberosUsername", "kerberosPassword", "kerberosEncryptedPassword", "keySets", "retainPreviousKeysOnPasswordChange", "suppressDomainNameConcatenation", "ldapGatewayDataStoreRef"]:
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
