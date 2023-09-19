from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.read_users import ReadUsers
from pingfedsdk.models.write_users import WriteUsers


class Users(Model):
    """User creation and read configuration.

    Attributes
    ----------
    writeUsers: WriteUsers
        Configuration to create a user within the user repository.

    readUsers: ReadUsers
        Configuration to lookup user info within the user repository and respond to incoming SCIM requests.

    """
    def __init__(self, writeUsers: WriteUsers, readUsers: ReadUsers) -> None:
        self.writeUsers = writeUsers
        self.readUsers = readUsers

    def _validate(self) -> bool:
        return any(x for x in ["readUsers", "writeUsers"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, Users):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.writeUsers, self.readUsers]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["writeUsers", "readUsers"] and v is not None:
                if k == "writeUsers":
                    valid_data[k] = WriteUsers.from_dict(v)
                if k == "readUsers":
                    valid_data[k] = ReadUsers.from_dict(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["writeUsers", "readUsers"]:
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
