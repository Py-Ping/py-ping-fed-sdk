from enum import Enum

from pingfedsdk.enums import JdbcAttributeSourceType
from pingfedsdk.model import Model
from pingfedsdk.models.resource_link import ResourceLink


class JdbcAttributeSource(Model):
    """The configured settings used to look up attributes from a JDBC data store.

    Attributes
    ----------
    type: JdbcAttributeSourceType
        The data store type of this attribute source.

    dataStoreRef: ResourceLink
        Reference to the associated data store.

    id: str
        The ID that defines this attribute source. Only alphanumeric characters allowed.
        Note: Required for OpenID Connect policy attribute sources, OAuth IdP adapter mappings, OAuth access token mappings and APC-to-SP Adapter Mappings. IdP Connections will ignore this property since it only allows one attribute source to be defined per mapping. IdP-to-SP Adapter Mappings can contain multiple attribute sources.

    description: str
        The description of this attribute source. The description needs to be unique amongst the attribute sources for the mapping.
        Note: Required for APC-to-SP Adapter Mappings

    attributeContractFulfillment: object
        A list of mappings from attribute names to their fulfillment values. This field is only valid for the SP Connection's Browser SSO mappings

    schema: str
        Lists the table structure that stores information within a database. Some databases, such as Oracle, require a schema for a JDBC query. Other databases, such as MySQL, do not require a schema.

    table: str
        The name of the database table. The name is used to construct the SQL query to retrieve data from the data store.

    columnNames: list
        A list of column names used to construct the SQL query to retrieve data from the specified table in the datastore.

    filter: str
        The JDBC WHERE clause used to query your data store to locate a user record.

    """
    def __init__(self, table: str, filter: str, type: JdbcAttributeSourceType = None, dataStoreRef: ResourceLink = None, id: str = None, schema: str = None, description: str = None, attributeContractFulfillment: object = None, columnNames: list = None) -> None:
        self.type = type
        self.dataStoreRef = dataStoreRef
        self.id = id
        self.description = description
        self.attributeContractFulfillment = attributeContractFulfillment
        self.schema = schema
        self.table = table
        self.columnNames = columnNames
        self.filter = filter

    def _validate(self) -> bool:
        return any(x for x in ["filter", "table"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, JdbcAttributeSource):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.dataStoreRef, self.id, self.description, self.attributeContractFulfillment, self.schema, self.table, self.columnNames, self.filter]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "dataStoreRef", "id", "description", "attributeContractFulfillment", "schema", "table", "columnNames", "filter"] and v is not None:
                if k == "type":
                    valid_data[k] = JdbcAttributeSourceType[v]
                if k == "dataStoreRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "id":
                    valid_data[k] = str(v)
                if k == "description":
                    valid_data[k] = str(v)
                if k == "attributeContractFulfillment":
                    valid_data[k] = object.from_dict(v)
                if k == "schema":
                    valid_data[k] = str(v)
                if k == "table":
                    valid_data[k] = str(v)
                if k == "columnNames":
                    valid_data[k] = [str(x) for x in v]
                if k == "filter":
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
            if k in ["type", "dataStoreRef", "id", "description", "attributeContractFulfillment", "schema", "table", "columnNames", "filter"]:
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
