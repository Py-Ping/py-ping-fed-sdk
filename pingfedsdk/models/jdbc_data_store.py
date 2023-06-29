from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.jdbc_tag_config import JdbcTagConfig
from pingfedsdk.enums import DataStoreType


class JdbcDataStore(Model):
    """A JDBC data store.

    Attributes
    ----------
    type: DataStoreType
        The data store type.

    id: str
        The persistent, unique ID for the data store. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.

    maskAttributeValues: bool
        Whether attribute values should be masked in the log.

    connectionUrlTags: list
        The set of connection URLs and associated tags for this JDBC data store.

    connectionUrl: str
        The default location of the JDBC database. This field is required if no mapping for JDBC database location and tags are specified.

    name: str
        The data store name with a unique value across all data sources. Omitting this attribute will set the value to a combination of the connection url and the username.

    driverClass: str
        The name of the driver class used to communicate with the source database.

    userName: str
        The name that identifies the user when connecting to the database.

    password: str
        The password needed to access the database. GETs will not return this attribute. To update this field, specify the new value in this attribute.

    encryptedPassword: str
        The encrypted password needed to access the database. If you do not want to update the stored value, this attribute should be passed back unchanged. Secret Reference may be provided in this field with format 'OBF:MGR:{secretManagerId}:{secretId}'.

    validateConnectionSql: str
        A simple SQL statement used by PingFederate at runtime to verify that the database connection is still active and to reconnect if needed.

    allowMultiValueAttributes: bool
        Indicates that this data store can select more than one record from a column and return the results as a multi-value attribute.

    minPoolSize: int
        The smallest number of database connections in the connection pool for the given data store. Omitting this attribute will set the value to the connection pool default.

    maxPoolSize: int
        The largest number of database connections in the connection pool for the given data store. Omitting this attribute will set the value to the connection pool default.

    blockingTimeout: int
        The amount of time in milliseconds a request waits to get a connection from the connection pool before it fails. Omitting this attribute will set the value to the connection pool default.

    idleTimeout: int
        The length of time in minutes the connection can be idle in the pool before it is closed. Omitting this attribute will set the value to the connection pool default.

    """

    def __init__(self, driverClass: str, userName: str, type: DataStoreType = None, id: str = None, maskAttributeValues: bool = None, connectionUrlTags: list = None, connectionUrl: str = None, name: str = None, password: str = None, encryptedPassword: str = None, validateConnectionSql: str = None, allowMultiValueAttributes: bool = None, minPoolSize: int = None, maxPoolSize: int = None, blockingTimeout: int = None, idleTimeout: int = None) -> None:
        self.type = type
        self.id = id
        self.maskAttributeValues = maskAttributeValues
        self.connectionUrlTags = connectionUrlTags
        self.connectionUrl = connectionUrl
        self.name = name
        self.driverClass = driverClass
        self.userName = userName
        self.password = password
        self.encryptedPassword = encryptedPassword
        self.validateConnectionSql = validateConnectionSql
        self.allowMultiValueAttributes = allowMultiValueAttributes
        self.minPoolSize = minPoolSize
        self.maxPoolSize = maxPoolSize
        self.blockingTimeout = blockingTimeout
        self.idleTimeout = idleTimeout

    def _validate(self) -> bool:
        return any(x for x in ["driverClass", "userName"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, JdbcDataStore):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.id, self.maskAttributeValues, self.connectionUrlTags, self.connectionUrl, self.name, self.driverClass, self.userName, self.password, self.encryptedPassword, self.validateConnectionSql, self.allowMultiValueAttributes, self.minPoolSize, self.maxPoolSize, self.blockingTimeout, self.idleTimeout]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "id", "maskAttributeValues", "connectionUrlTags", "connectionUrl", "name", "driverClass", "userName", "password", "encryptedPassword", "validateConnectionSql", "allowMultiValueAttributes", "minPoolSize", "maxPoolSize", "blockingTimeout", "idleTimeout"] and v is not None:
                if k == "type":
                    valid_data[k] = DataStoreType[v]
                if k == "id":
                    valid_data[k] = str(v)
                if k == "maskAttributeValues":
                    valid_data[k] = bool(v)
                if k == "connectionUrlTags":
                    valid_data[k] = [JdbcTagConfig(**x) for x in v]
                if k == "connectionUrl":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "driverClass":
                    valid_data[k] = str(v)
                if k == "userName":
                    valid_data[k] = str(v)
                if k == "password":
                    valid_data[k] = str(v)
                if k == "encryptedPassword":
                    valid_data[k] = str(v)
                if k == "validateConnectionSql":
                    valid_data[k] = str(v)
                if k == "allowMultiValueAttributes":
                    valid_data[k] = bool(v)
                if k == "minPoolSize":
                    valid_data[k] = int(v)
                if k == "maxPoolSize":
                    valid_data[k] = int(v)
                if k == "blockingTimeout":
                    valid_data[k] = int(v)
                if k == "idleTimeout":
                    valid_data[k] = int(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["type", "id", "maskAttributeValues", "connectionUrlTags", "connectionUrl", "name", "driverClass", "userName", "password", "encryptedPassword", "validateConnectionSql", "allowMultiValueAttributes", "minPoolSize", "maxPoolSize", "blockingTimeout", "idleTimeout"]:
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
