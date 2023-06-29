from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.ldap_tag_config import LdapTagConfig
from pingfedsdk.enums import LdapType
from pingfedsdk.enums import DataStoreType


class LdapDataStore(Model):
    """A LDAP data store.

    Attributes
    ----------
    type: DataStoreType
        The data store type.

    id: str
        The persistent, unique ID for the data store. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.

    maskAttributeValues: bool
        Whether attribute values should be masked in the log.

    hostnamesTags: list
        The set of host names and associated tags for this LDAP data store.

    hostnames: list
        The default LDAP host names. This field is required if no mapping for host names and tags are specified.

    name: str
        The data store name with a unique value across all data sources. Omitting this attribute will set the value to a combination of the hostname(s) and the principal.

    ldapType: LdapType
        A type that allows PingFederate to configure many provisioning settings automatically. The 'UNBOUNDID_DS' type has been deprecated, please use the 'PING_DIRECTORY' type instead.

    bindAnonymously: bool
        Whether username and password are required. The default value is false.

    userDN: str
        The username credential required to access the data store.

    password: str
        The password credential required to access the data store. GETs will not return this attribute. To update this field, specify the new value in this attribute.

    encryptedPassword: str
        The encrypted password credential required to access the data store.  If you do not want to update the stored value, this attribute should be passed back unchanged. Secret Reference may be provided in this field with format 'OBF:MGR:{secretManagerId}:{secretId}'.

    useSsl: bool
        Connects to the LDAP data store using secure SSL/TLS encryption (LDAPS). The default value is false.

    useDnsSrvRecords: bool
        Use DNS SRV Records to discover LDAP server information. The default value is false.

    followLDAPReferrals: bool
        Follow LDAP Referrals in the domain tree. The default value is false. This property does not apply to PingDirectory as this functionality is configured in PingDirectory.

    testOnBorrow: bool
        Indicates whether objects are validated before being borrowed from the pool.

    testOnReturn: bool
        Indicates whether objects are validated before being returned to the pool.

    createIfNecessary: bool
        Indicates whether temporary connections can be created when the Maximum Connections threshold is reached.

    verifyHost: bool
        Verifies that the presented server certificate includes the address to which the client intended to establish a connection. Omitting this attribute will set the value to true.

    minConnections: int
        The smallest number of connections that can remain in each pool, without creating extra ones. Omitting this attribute will set the value to the default value.

    maxConnections: int
        The largest number of active connections that can remain in each pool without releasing extra ones. Omitting this attribute will set the value to the default value.

    maxWait: int
        The maximum number of milliseconds the pool waits for a connection to become available when trying to obtain a connection from the pool. Omitting this attribute or setting a value of -1 causes the pool not to wait at all and to either create a new connection or produce an error (when no connections are available).

    timeBetweenEvictions: int
        The frequency, in milliseconds, that the evictor cleans up the connections in the pool. A value of -1 disables the evictor. Omitting this attribute will set the value to the default value.

    readTimeout: int
        The maximum number of milliseconds a connection waits for a response to be returned before producing an error. A value of -1 causes the connection to wait indefinitely. Omitting this attribute will set the value to the default value.

    connectionTimeout: int
        The maximum number of milliseconds that a connection attempt should be allowed to continue before returning an error. A value of -1 causes the pool to wait indefinitely. Omitting this attribute will set the value to the default value.

    dnsTtl: int
        The maximum time in milliseconds that DNS information are cached. Omitting this attribute will set the value to the default value.

    ldapDnsSrvPrefix: str
        The prefix value used to discover LDAP DNS SRV record. Omitting this attribute will set the value to the default value.

    ldapsDnsSrvPrefix: str
        The prefix value used to discover LDAPs DNS SRV record. Omitting this attribute will set the value to the default value.

    binaryAttributes: list
        The list of LDAP attributes to be handled as binary data.

    """

    def __init__(self, ldapType: LdapType, type: DataStoreType = None, id: str = None, maskAttributeValues: bool = None, hostnamesTags: list = None, hostnames: list = None, name: str = None, bindAnonymously: bool = None, userDN: str = None, password: str = None, encryptedPassword: str = None, useSsl: bool = None, useDnsSrvRecords: bool = None, followLDAPReferrals: bool = None, testOnBorrow: bool = None, testOnReturn: bool = None, createIfNecessary: bool = None, verifyHost: bool = None, minConnections: int = None, maxConnections: int = None, maxWait: int = None, timeBetweenEvictions: int = None, readTimeout: int = None, connectionTimeout: int = None, dnsTtl: int = None, ldapDnsSrvPrefix: str = None, ldapsDnsSrvPrefix: str = None, binaryAttributes: list = None) -> None:
        self.type = type
        self.id = id
        self.maskAttributeValues = maskAttributeValues
        self.hostnamesTags = hostnamesTags
        self.hostnames = hostnames
        self.name = name
        self.ldapType = ldapType
        self.bindAnonymously = bindAnonymously
        self.userDN = userDN
        self.password = password
        self.encryptedPassword = encryptedPassword
        self.useSsl = useSsl
        self.useDnsSrvRecords = useDnsSrvRecords
        self.followLDAPReferrals = followLDAPReferrals
        self.testOnBorrow = testOnBorrow
        self.testOnReturn = testOnReturn
        self.createIfNecessary = createIfNecessary
        self.verifyHost = verifyHost
        self.minConnections = minConnections
        self.maxConnections = maxConnections
        self.maxWait = maxWait
        self.timeBetweenEvictions = timeBetweenEvictions
        self.readTimeout = readTimeout
        self.connectionTimeout = connectionTimeout
        self.dnsTtl = dnsTtl
        self.ldapDnsSrvPrefix = ldapDnsSrvPrefix
        self.ldapsDnsSrvPrefix = ldapsDnsSrvPrefix
        self.binaryAttributes = binaryAttributes

    def _validate(self) -> bool:
        return any(x for x in ["ldapType"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, LdapDataStore):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.id, self.maskAttributeValues, self.hostnamesTags, self.hostnames, self.name, self.ldapType, self.bindAnonymously, self.userDN, self.password, self.encryptedPassword, self.useSsl, self.useDnsSrvRecords, self.followLDAPReferrals, self.testOnBorrow, self.testOnReturn, self.createIfNecessary, self.verifyHost, self.minConnections, self.maxConnections, self.maxWait, self.timeBetweenEvictions, self.readTimeout, self.connectionTimeout, self.dnsTtl, self.ldapDnsSrvPrefix, self.ldapsDnsSrvPrefix, self.binaryAttributes]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "id", "maskAttributeValues", "hostnamesTags", "hostnames", "name", "ldapType", "bindAnonymously", "userDN", "password", "encryptedPassword", "useSsl", "useDnsSrvRecords", "followLDAPReferrals", "testOnBorrow", "testOnReturn", "createIfNecessary", "verifyHost", "minConnections", "maxConnections", "maxWait", "timeBetweenEvictions", "readTimeout", "connectionTimeout", "dnsTtl", "ldapDnsSrvPrefix", "ldapsDnsSrvPrefix", "binaryAttributes"] and v is not None:
                if k == "type":
                    valid_data[k] = DataStoreType[v]
                if k == "id":
                    valid_data[k] = str(v)
                if k == "maskAttributeValues":
                    valid_data[k] = bool(v)
                if k == "hostnamesTags":
                    valid_data[k] = [LdapTagConfig(**x) for x in v]
                if k == "hostnames":
                    valid_data[k] = [str(x) for x in v]
                if k == "name":
                    valid_data[k] = str(v)
                if k == "ldapType":
                    valid_data[k] = LdapType[v]
                if k == "bindAnonymously":
                    valid_data[k] = bool(v)
                if k == "userDN":
                    valid_data[k] = str(v)
                if k == "password":
                    valid_data[k] = str(v)
                if k == "encryptedPassword":
                    valid_data[k] = str(v)
                if k == "useSsl":
                    valid_data[k] = bool(v)
                if k == "useDnsSrvRecords":
                    valid_data[k] = bool(v)
                if k == "followLDAPReferrals":
                    valid_data[k] = bool(v)
                if k == "testOnBorrow":
                    valid_data[k] = bool(v)
                if k == "testOnReturn":
                    valid_data[k] = bool(v)
                if k == "createIfNecessary":
                    valid_data[k] = bool(v)
                if k == "verifyHost":
                    valid_data[k] = bool(v)
                if k == "minConnections":
                    valid_data[k] = int(v)
                if k == "maxConnections":
                    valid_data[k] = int(v)
                if k == "maxWait":
                    valid_data[k] = int(v)
                if k == "timeBetweenEvictions":
                    valid_data[k] = int(v)
                if k == "readTimeout":
                    valid_data[k] = int(v)
                if k == "connectionTimeout":
                    valid_data[k] = int(v)
                if k == "dnsTtl":
                    valid_data[k] = int(v)
                if k == "ldapDnsSrvPrefix":
                    valid_data[k] = str(v)
                if k == "ldapsDnsSrvPrefix":
                    valid_data[k] = str(v)
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
            if k in ["type", "id", "maskAttributeValues", "hostnamesTags", "hostnames", "name", "ldapType", "bindAnonymously", "userDN", "password", "encryptedPassword", "useSsl", "useDnsSrvRecords", "followLDAPReferrals", "testOnBorrow", "testOnReturn", "createIfNecessary", "verifyHost", "minConnections", "maxConnections", "maxWait", "timeBetweenEvictions", "readTimeout", "connectionTimeout", "dnsTtl", "ldapDnsSrvPrefix", "ldapsDnsSrvPrefix", "binaryAttributes"]:
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
