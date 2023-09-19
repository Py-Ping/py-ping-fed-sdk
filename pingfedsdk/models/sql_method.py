from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.stored_procedure import StoredProcedure
from pingfedsdk.models.table import Table


class SqlMethod(Model):
    """SQL Method.

    Attributes
    ----------
    table: Table
        The Table SQL method.

    storedProcedure: StoredProcedure
        The Stored Procedure SQL method. The procedure is always called for all SSO tokens and "eventTrigger" will always be 'ALL_SAML_ASSERTIONS'.

    """
    def __init__(self, table: Table = None, storedProcedure: StoredProcedure = None) -> None:
        self.table = table
        self.storedProcedure = storedProcedure

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SqlMethod):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.table, self.storedProcedure]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["table", "storedProcedure"] and v is not None:
                if k == "table":
                    valid_data[k] = Table.from_dict(v)
                if k == "storedProcedure":
                    valid_data[k] = StoredProcedure.from_dict(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["table", "storedProcedure"]:
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
