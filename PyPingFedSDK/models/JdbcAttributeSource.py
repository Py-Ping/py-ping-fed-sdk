class JdbcAttributeSource():
    """The configured settings used to look up attributes from a JDBC data store.

    Attributes
    ----------
    attributeContractFulfillment : str
 A list of mappings from attribute names to their fulfillment values. This field is only valid for the SP Connection's Browser SSO mappings
    dataStoreRef : str
 Reference to the associated data store.
    description : string
 The description of this attribute source. The description needs to be unique amongst the attribute sources for the mapping.<br>Note: Required for APC-to-SP Adapter Mappings
    filter : string
 The JDBC WHERE clause used to query your data store to locate a user record.
    id : string
 The ID that defines this attribute source. Only alphanumeric characters allowed.<br>Note: Required for OpenID Connect policy attribute sources, OAuth IdP adapter mappings, OAuth access token mappings and APC-to-SP Adapter Mappings. IdP Connections will ignore this property since it only allows one attribute source to be defined per mapping. IdP-to-SP Adapter Mappings can contain multiple attribute sources.
    schema : string
 Lists the table structure that stores information within a database. Some databases, such as Oracle, require a schema for a JDBC query. Other databases, such as MySQL, do not require a schema.
    table : string
 The name of the database table. The name is used to construct the SQL query to retrieve data from the data store.
    type : str
 The data store type of this attribute source.

    """

    def __init__(self, var_type, dataStoreRef, table, filter, attributeContractFulfillment=None, description=None, var_id=None, schema=None) -> None:
        self.attributeContractFulfillment = attributeContractFulfillment
        self.dataStoreRef = dataStoreRef
        self.description = description
        self.filter = filter
        self.var_id = var_id
        self.schema = schema
        self.table = table
        self.var_type = var_type

    def _validate(self) -> bool:
        return any(x for x in ["var_type", "dataStoreRef", "table", "filter"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, JdbcAttributeSource):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.attributeContractFulfillment, self.dataStoreRef, self.description, self.filter, self.var_id, self.schema, self.table, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeContractFulfillment", "dataStoreRef", "description", "filter", "var_id", "schema", "table", "var_type"]}

        return cls(**valid_data)