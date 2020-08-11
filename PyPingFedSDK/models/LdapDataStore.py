class LdapDataStore():
    """A LDAP data store.

    Attributes
    ----------
    binaryAttributes : array
        The list of LDAP attributes to be handled as binary data.
    bindAnonymously : boolean
        Whether username and password are required. The default value is false.
    connectionTimeout : integer
        The maximum number of milliseconds that a connection attempt should be allowed to continue before returning an error. A value of -1 causes the pool to wait indefinitely. Omitting this attribute will set the value to the default value.
    createIfNecessary : boolean
        Indicates whether temporary connections can be created when the Maximum Connections threshold is reached.
    dnsTtl : integer
        The maximum time in milliseconds that DNS information are cached. Omitting this attribute will set the value to the default value.
    encryptedPassword : string
        The encrypted password credential required to access the data store.  If you do not want to update the stored value, this attribute should be passed back unchanged.
    followLDAPReferrals : boolean
        Follow LDAP Referrals in the domain tree. The default value is false. This property does not apply to PingDirectory as this functionality is configured in PingDirectory.
    hostnames : array
        The default LDAP host names. This field is required if no mapping for host names and tags are specified.
    hostnamesTags : array
        The set of host names and associated tags for this LDAP data store.
    id : string
        The persistent, unique ID for the data store. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.
    ldapDnsSrvPrefix : string
        The prefix value used to discover LDAP DNS SRV record. Omitting this attribute will set the value to the default value.
    ldapType : str
        A type that allows PingFederate to configure many provisioning settings automatically. The 'UNBOUNDID_DS' type has been deprecated, please use the 'PING_DIRECTORY' type instead.
    ldapsDnsSrvPrefix : string
        The prefix value used to discover LDAPs DNS SRV record. Omitting this attribute will set the value to the default value.
    maskAttributeValues : boolean
        Whether attribute values should be masked in the log.
    maxConnections : integer
        The largest number of active connections that can remain in each pool without releasing extra ones. Omitting this attribute will set the value to the default value.
    maxWait : integer
        The maximum number of milliseconds the pool waits for a connection to become available when trying to obtain a connection from the pool. Omitting this attribute or setting a value of -1 causes the pool not to wait at all and to either create a new connection or produce an error (when no connections are available).
    minConnections : integer
        The smallest number of connections that can remain in each pool, without creating extra ones. Omitting this attribute will set the value to the default value.
    name : string
        The data store name with a unique value across all data sources. Omitting this attribute will set the value to a combination of the hostname(s) and the principal.
    password : string
        The password credential required to access the data store. GETs will not return this attribute. To update this field, specify the new value in this attribute.
    readTimeout : integer
        The maximum number of milliseconds a connection waits for a response to be returned before producing an error. A value of -1 causes the connection to wait indefinitely. Omitting this attribute will set the value to the default value.
    testOnBorrow : boolean
        Indicates whether objects are validated before being borrowed from the pool.
    testOnReturn : boolean
        Indicates whether objects are validated before being returned to the pool.
    timeBetweenEvictions : integer
        The frequency, in milliseconds, that the evictor cleans up the connections in the pool. A value of -1 disables the evictor. Omitting this attribute will set the value to the default value.
    type : str
        The data store type.
    useDnsSrvRecords : boolean
        Use DNS SRV Records to discover LDAP server information. The default value is false.
    useSsl : boolean
        Connects to the LDAP data store using secure SSL/TLS encryption (LDAPS). The default value is false.
    userDN : string
        The username credential required to access the data store.
    verifyHost : boolean
        Verifies that the presented server certificate includes the address to which the client intended to establish a connection. Omitting this attribute will set the value to true.

    """

    def __init__(self, var_type, ldapType, binaryAttributes:list=None, bindAnonymously:bool=None, connectionTimeout:int=None, createIfNecessary:bool=None, dnsTtl:int=None, encryptedPassword:str=None, followLDAPReferrals:bool=None, hostnames:list=None, hostnamesTags:list=None, var_id:str=None, ldapDnsSrvPrefix:str=None, ldapsDnsSrvPrefix:str=None, maskAttributeValues:bool=None, maxConnections:int=None, maxWait:int=None, minConnections:int=None, name:str=None, password:str=None, readTimeout:int=None, testOnBorrow:bool=None, testOnReturn:bool=None, timeBetweenEvictions:int=None, useDnsSrvRecords:bool=None, useSsl:bool=None, userDN:str=None, verifyHost:bool=None) -> None:
        self.binaryAttributes = binaryAttributes
        self.bindAnonymously = bindAnonymously
        self.connectionTimeout = connectionTimeout
        self.createIfNecessary = createIfNecessary
        self.dnsTtl = dnsTtl
        self.encryptedPassword = encryptedPassword
        self.followLDAPReferrals = followLDAPReferrals
        self.hostnames = hostnames
        self.hostnamesTags = hostnamesTags
        self.var_id = var_id
        self.ldapDnsSrvPrefix = ldapDnsSrvPrefix
        self.ldapType = ldapType
        self.ldapsDnsSrvPrefix = ldapsDnsSrvPrefix
        self.maskAttributeValues = maskAttributeValues
        self.maxConnections = maxConnections
        self.maxWait = maxWait
        self.minConnections = minConnections
        self.name = name
        self.password = password
        self.readTimeout = readTimeout
        self.testOnBorrow = testOnBorrow
        self.testOnReturn = testOnReturn
        self.timeBetweenEvictions = timeBetweenEvictions
        self.var_type = var_type
        self.useDnsSrvRecords = useDnsSrvRecords
        self.useSsl = useSsl
        self.userDN = userDN
        self.verifyHost = verifyHost

    def _validate(self) -> bool:
        return any(x for x in ["var_type", "ldapType"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, LdapDataStore):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.binaryAttributes, self.bindAnonymously, self.connectionTimeout, self.createIfNecessary, self.dnsTtl, self.encryptedPassword, self.followLDAPReferrals, self.hostnames, self.hostnamesTags, self.var_id, self.ldapDnsSrvPrefix, self.ldapType, self.ldapsDnsSrvPrefix, self.maskAttributeValues, self.maxConnections, self.maxWait, self.minConnections, self.name, self.password, self.readTimeout, self.testOnBorrow, self.testOnReturn, self.timeBetweenEvictions, self.var_type, self.useDnsSrvRecords, self.useSsl, self.userDN, self.verifyHost))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["binaryAttributes", "bindAnonymously", "connectionTimeout", "createIfNecessary", "dnsTtl", "encryptedPassword", "followLDAPReferrals", "hostnames", "hostnamesTags", "var_id", "ldapDnsSrvPrefix", "ldapType", "ldapsDnsSrvPrefix", "maskAttributeValues", "maxConnections", "maxWait", "minConnections", "name", "password", "readTimeout", "testOnBorrow", "testOnReturn", "timeBetweenEvictions", "var_type", "useDnsSrvRecords", "useSsl", "userDN", "verifyHost"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__