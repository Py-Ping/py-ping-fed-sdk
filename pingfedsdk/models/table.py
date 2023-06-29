from pingfedsdk.model import Model
from enum import Enum


class Table(Model):
    """SQL Method Table.

    Attributes
    ----------
    schema: str
        Lists the table structure that stores information within a database.

    tableName: str
        The name of the database table.

    uniqueIdColumn: str
        The database column that uniquely identifies the provisioned user on the SP side.

    """

    def __init__(self, schema: str, tableName: str, uniqueIdColumn: str) -> None:
        self.schema = schema
        self.tableName = tableName
        self.uniqueIdColumn = uniqueIdColumn

    def _validate(self) -> bool:
        return any(x for x in ["schema", "tableName", "uniqueIdColumn"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, Table):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.schema, self.tableName, self.uniqueIdColumn]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["schema", "tableName", "uniqueIdColumn"] and v is not None:
                if k == "schema":
                    valid_data[k] = str(v)
                if k == "tableName":
                    valid_data[k] = str(v)
                if k == "uniqueIdColumn":
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
            if k in ["schema", "tableName", "uniqueIdColumn"]:
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
