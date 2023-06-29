from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.enums import ChangedUsersAlgorithm


class ChangeDetectionSettings(Model):
    """Setting to detect changes to a user or a group.

    Attributes
    ----------
    userObjectClass: str
        The user object class.

    groupObjectClass: str
        The group object class.

    changedUsersAlgorithm: ChangedUsersAlgorithm
        The changed user algorithm. ACTIVE_DIRECTORY_USN - For Active Directory only, this algorithm queries for update sequence numbers on user records that are larger than the last time records were checked. TIMESTAMP - Queries for timestamps on user records that are not older than the last time records were checked. This check is more efficient from the point of view of the PingFederate provisioner but can be more time consuming on the LDAP side, particularly with the Oracle Directory Server. TIMESTAMP_NO_NEGATION - Queries for timestamps on user records that are newer than the last time records were checked. This algorithm is recommended for the Oracle Directory Server.

    usnAttributeName: str
        The USN attribute name.

    timeStampAttributeName: str
        The timestamp attribute name.

    """

    def __init__(self, changedUsersAlgorithm: ChangedUsersAlgorithm, groupObjectClass: str, timeStampAttributeName: str, userObjectClass: str, usnAttributeName: str = None) -> None:
        self.userObjectClass = userObjectClass
        self.groupObjectClass = groupObjectClass
        self.changedUsersAlgorithm = changedUsersAlgorithm
        self.usnAttributeName = usnAttributeName
        self.timeStampAttributeName = timeStampAttributeName

    def _validate(self) -> bool:
        return any(x for x in ["changedUsersAlgorithm", "groupObjectClass", "timeStampAttributeName", "userObjectClass"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ChangeDetectionSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.userObjectClass, self.groupObjectClass, self.changedUsersAlgorithm, self.usnAttributeName, self.timeStampAttributeName]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["userObjectClass", "groupObjectClass", "changedUsersAlgorithm", "usnAttributeName", "timeStampAttributeName"] and v is not None:
                if k == "userObjectClass":
                    valid_data[k] = str(v)
                if k == "groupObjectClass":
                    valid_data[k] = str(v)
                if k == "changedUsersAlgorithm":
                    valid_data[k] = ChangedUsersAlgorithm[v]
                if k == "usnAttributeName":
                    valid_data[k] = str(v)
                if k == "timeStampAttributeName":
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
            if k in ["userObjectClass", "groupObjectClass", "changedUsersAlgorithm", "usnAttributeName", "timeStampAttributeName"]:
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
