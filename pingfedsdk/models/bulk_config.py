from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.bulk_config_metadata import BulkConfigMetadata
from pingfedsdk.models.config_operation import ConfigOperation


class BulkConfig(Model):
    """Model describing a series of configuration operations.

    Attributes
    ----------
    metadata: BulkConfigMetadata
        The metadata detailing how this config was generated.

    operations: list
        A list of configuration operations.

    """

    def __init__(self, metadata: BulkConfigMetadata, operations: list) -> None:
        self.metadata = metadata
        self.operations = operations

    def _validate(self) -> bool:
        return any(x for x in ["metadata", "operations"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, BulkConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.metadata, self.operations]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["metadata", "operations"] and v is not None:
                if k == "metadata":
                    valid_data[k] = BulkConfigMetadata(**v)
                if k == "operations":
                    valid_data[k] = [ConfigOperation(**x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["metadata", "operations"]:
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
