from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.field_descriptor import FieldDescriptor


class ActionDescriptor(Model):
    """Describes an arbitrary action that is available for a plugin.

    Attributes
    ----------
    name: str
        The name of this action

    description: str
        The description of this action

    download: bool
        Whether this action will trigger a download or invoke an internal action that will return a string result.

    downloadContentType: str
        If this is a download, this is the Content-Type of the downloaded file. Otherwise, this is null.

    downloadFileName: str
        If this is a download, this is the suggested file name of the downloaded file. Otherwise, this is null.

    parameters: list
        List of parameters for this action.

    """
    def __init__(self, name: str = None, description: str = None, download: bool = None, downloadContentType: str = None, downloadFileName: str = None, parameters: list = None) -> None:
        self.name = name
        self.description = description
        self.download = download
        self.downloadContentType = downloadContentType
        self.downloadFileName = downloadFileName
        self.parameters = parameters

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ActionDescriptor):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.name, self.description, self.download, self.downloadContentType, self.downloadFileName, self.parameters]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["name", "description", "download", "downloadContentType", "downloadFileName", "parameters"] and v is not None:
                if k == "name":
                    valid_data[k] = str(v)
                if k == "description":
                    valid_data[k] = str(v)
                if k == "download":
                    valid_data[k] = bool(v)
                if k == "downloadContentType":
                    valid_data[k] = str(v)
                if k == "downloadFileName":
                    valid_data[k] = str(v)
                if k == "parameters":
                    valid_data[k] = [FieldDescriptor.from_dict(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["name", "description", "download", "downloadContentType", "downloadFileName", "parameters"]:
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
