from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.field_descriptor import FieldDescriptor


class TableDescriptor(Model):
    """Defines a plugin configuration table.

    Attributes
    ----------
    name: str
        The name of the table.

    description: str
        Description for the table.

    columns: list
        Get the columns in the table.

    label: str
        Label for the table to be displayed in the administrative console.

    requireDefaultRow: bool
        Configure whether this table requires default row to be set.

    """

    def __init__(self, name: str = None, description: str = None, columns: list = None, label: str = None, requireDefaultRow: bool = None) -> None:
        self.name = name
        self.description = description
        self.columns = columns
        self.label = label
        self.requireDefaultRow = requireDefaultRow

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, TableDescriptor):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.name, self.description, self.columns, self.label, self.requireDefaultRow]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["name", "description", "columns", "label", "requireDefaultRow"] and v is not None:
                if k == "name":
                    valid_data[k] = str(v)
                if k == "description":
                    valid_data[k] = str(v)
                if k == "columns":
                    valid_data[k] = [FieldDescriptor(**x) for x in v]
                if k == "label":
                    valid_data[k] = str(v)
                if k == "requireDefaultRow":
                    valid_data[k] = bool(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["name", "description", "columns", "label", "requireDefaultRow"]:
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
