from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.action_descriptor import ActionDescriptor
from pingfedsdk.models.field_descriptor import FieldDescriptor
from pingfedsdk.models.table_descriptor import TableDescriptor


class PluginConfigDescriptor(Model):
    """Defines the configuration fields available for a plugin.

    Attributes
    ----------
    description: str
        The description of this plugin.

    fields: list
        The configuration fields available for this plugin.

    tables: list
        Configuration tables available for this plugin.

    actionDescriptors: list
        The available actions for this plugin.

    """
    def __init__(self, description: str = None, fields: list = None, tables: list = None, actionDescriptors: list = None) -> None:
        self.description = description
        self.fields = fields
        self.tables = tables
        self.actionDescriptors = actionDescriptors

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, PluginConfigDescriptor):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.description, self.fields, self.tables, self.actionDescriptors]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["description", "fields", "tables", "actionDescriptors"] and v is not None:
                if k == "description":
                    valid_data[k] = str(v)
                if k == "fields":
                    valid_data[k] = [FieldDescriptor.from_dict(x) for x in v]
                if k == "tables":
                    valid_data[k] = [TableDescriptor.from_dict(x) for x in v]
                if k == "actionDescriptors":
                    valid_data[k] = [ActionDescriptor.from_dict(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["description", "fields", "tables", "actionDescriptors"]:
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
