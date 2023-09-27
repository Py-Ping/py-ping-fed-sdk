from enum import Enum

from pingfedsdk.enums import JdbcDataStoreRepositoryType
from pingfedsdk.model import Model
from pingfedsdk.models.attribute_fulfillment_value import AttributeFulfillmentValue
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.models.sql_method import SqlMethod


class JdbcDataStoreRepository(Model):
    """JDBC data store user repository.

    Attributes
    ----------
    type: JdbcDataStoreRepositoryType
        The data store repository type.

    dataStoreRef: ResourceLink
        Reference to the associated data store.

    jitRepositoryAttributeMapping: dict
        A list of user repository mappings from attribute names to their fulfillment values.

    sqlMethod: SqlMethod
        The method to map attributes from the assertion directly to database table columns or to stored-procedure parameters.

    """
    def __init__(self, sqlMethod: SqlMethod, jitRepositoryAttributeMapping: dict, type: JdbcDataStoreRepositoryType = None, dataStoreRef: ResourceLink = None) -> None:
        self.type = type
        self.dataStoreRef = dataStoreRef
        self.jitRepositoryAttributeMapping = jitRepositoryAttributeMapping
        self.sqlMethod = sqlMethod

    def _validate(self) -> bool:
        return any(x for x in ["jitRepositoryAttributeMapping", "sqlMethod"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, JdbcDataStoreRepository):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.dataStoreRef, self.jitRepositoryAttributeMapping, self.sqlMethod]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "dataStoreRef", "jitRepositoryAttributeMapping", "sqlMethod"] and v is not None:
                if k == "type":
                    valid_data[k] = JdbcDataStoreRepositoryType[v]
                if k == "dataStoreRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "jitRepositoryAttributeMapping":
                    valid_data[k] = {str(x): AttributeFulfillmentValue.from_dict(y) for x, y in v.items()}
                if k == "sqlMethod":
                    valid_data[k] = SqlMethod.from_dict(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["type", "dataStoreRef", "jitRepositoryAttributeMapping", "sqlMethod"]:
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
