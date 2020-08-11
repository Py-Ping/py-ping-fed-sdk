class JdbcDataStore():
    """A JDBC data store.

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

    def __init__(self, var_type, driverClass:str, userName:str, allowMultiValueAttributes:bool=None, blockingTimeout:int=None, connectionUrl:str=None, connectionUrlTags:list=None, encryptedPassword:str=None, var_id:str=None, idleTimeout:int=None, maskAttributeValues:bool=None, maxPoolSize:int=None, minPoolSize:int=None, name:str=None, password:str=None, validateConnectionSql:str=None) -> None:
        self.allowMultiValueAttributes = allowMultiValueAttributes
        self.blockingTimeout = blockingTimeout
        self.connectionUrl = connectionUrl
        self.connectionUrlTags = connectionUrlTags
        self.driverClass = driverClass
        self.encryptedPassword = encryptedPassword
        self.var_id = var_id
        self.idleTimeout = idleTimeout
        self.maskAttributeValues = maskAttributeValues
        self.maxPoolSize = maxPoolSize
        self.minPoolSize = minPoolSize
        self.name = name
        self.password = password
        self.var_type = var_type
        self.userName = userName
        self.validateConnectionSql = validateConnectionSql

    def _validate(self) -> bool:
        return any(x for x in ["var_type", "driverClass", "userName"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, JdbcDataStore):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.allowMultiValueAttributes, self.blockingTimeout, self.connectionUrl, self.connectionUrlTags, self.driverClass, self.encryptedPassword, self.var_id, self.idleTimeout, self.maskAttributeValues, self.maxPoolSize, self.minPoolSize, self.name, self.password, self.var_type, self.userName, self.validateConnectionSql]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["allowMultiValueAttributes", "blockingTimeout", "connectionUrl", "connectionUrlTags", "driverClass", "encryptedPassword", "var_id", "idleTimeout", "maskAttributeValues", "maxPoolSize", "minPoolSize", "name", "password", "var_type", "userName", "validateConnectionSql"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__