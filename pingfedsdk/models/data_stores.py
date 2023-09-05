from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.data_store import DataStore
from pingfedsdk.models.custom_data_store import CustomDataStore
from pingfedsdk.models.jdbc_data_store import JdbcDataStore
from pingfedsdk.models.ldap_data_store import LdapDataStore


class DataStores(Model):
    """A collection of data stores.

    Attributes
    ----------
    items: list
        The actual list of data stores.

    """

    def __init__(self, items: list = None) -> None:
        self.items = items

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, DataStores):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.items]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["items"] and v is not None:
                if k == "items":
                    temp_list = []
                    for x in v:
                        if x["type"] == "JDBC":
                            temp_list.append(JdbcDataStore(**x))
                        elif x["type"] == "LDAP":
                            temp_list.append(LdapDataStore(**x))
                        elif x["type"] == "CUSTOM":
                            temp_list.append(CustomDataStore(**x))
                        else:
                            temp_list.append(DataStore(**x))
                    valid_data[k] = temp_list
                

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["items"]:
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
