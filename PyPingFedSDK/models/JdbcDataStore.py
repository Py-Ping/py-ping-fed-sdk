class JdbcDataStore():
    """ A JDBC data store.

    Attributes
    ----------
    allowMultiValueAttributes : boolean
        Indicates that this data store can select more than one record from a column and return the results as a multi-value attribute.
    blockingTimeout : integer
        The amount of time in milliseconds a request waits to get a connection from the connection pool before it fails. Omitting this attribute will set the value to the connection pool default.
    connectionUrl : string
        The default location of the JDBC database. This field is required if no mapping for JDBC database location and tags are specified.
    connectionUrlTags : array
        The set of connection URLs and associated tags for this JDBC data store.
    driverClass : string
        The name of the driver class used to communicate with the source database.
    encryptedPassword : string
        The encrypted password needed to access the database. If you do not want to update the stored value, this attribute should be passed back unchanged.
    id : string
        The persistent, unique ID for the data store. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.
    idleTimeout : integer
        The length of time in minutes the connection can be idle in the pool before it is closed. Omitting this attribute will set the value to the connection pool default.
    maskAttributeValues : boolean
        Whether attribute values should be masked in the log.
    maxPoolSize : integer
        The largest number of database connections in the connection pool for the given data store. Omitting this attribute will set the value to the connection pool default.
    minPoolSize : integer
        The smallest number of database connections in the connection pool for the given data store. Omitting this attribute will set the value to the connection pool default.
    name : string
        The data store name with a unique value across all data sources. Omitting this attribute will set the value to a combination of the connection url and the username.
    password : string
        The password needed to access the database. GETs will not return this attribute. To update this field, specify the new value in this attribute.
    type : str
        The data store type.
    userName : string
        The name that identifies the user when connecting to the database.
    validateConnectionSql : string
        A simple SQL statement used by PingFederate at runtime to verify that the database connection is still active and to reconnect if needed.

    """

    __slots__ = ["allowMultiValueAttributes", "blockingTimeout", "connectionUrl", "connectionUrlTags", "driverClass", "encryptedPassword", "id", "idleTimeout", "maskAttributeValues", "maxPoolSize", "minPoolSize", "name", "password", "type", "userName", "validateConnectionSql"]
    def __init__(self, type, driverClass, userName, allowMultiValueAttributes=None, blockingTimeout=None, connectionUrl=None, connectionUrlTags=None, encryptedPassword=None, id=None, idleTimeout=None, maskAttributeValues=None, maxPoolSize=None, minPoolSize=None, name=None, password=None, validateConnectionSql=None):
            self.allowMultiValueAttributes = allowMultiValueAttributes
            self.blockingTimeout = blockingTimeout
            self.connectionUrl = connectionUrl
            self.connectionUrlTags = connectionUrlTags
            self.driverClass = driverClass
            self.encryptedPassword = encryptedPassword
            self.id = id
            self.idleTimeout = idleTimeout
            self.maskAttributeValues = maskAttributeValues
            self.maxPoolSize = maxPoolSize
            self.minPoolSize = minPoolSize
            self.name = name
            self.password = password
            self.type = type
            self.userName = userName
            self.validateConnectionSql = validateConnectionSql
    
    def _validate(self):
        return any(x for x in ['type', 'driverClass', 'userName'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, JdbcDataStore):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((allowMultiValueAttributes, blockingTimeout, connectionUrl, connectionUrlTags, driverClass, encryptedPassword, id, idleTimeout, maskAttributeValues, maxPoolSize, minPoolSize, name, password, type, userName, validateConnectionSql))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
