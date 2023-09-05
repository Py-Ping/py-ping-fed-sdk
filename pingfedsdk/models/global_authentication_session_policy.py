from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.enums import IdleTimeoutDisplayUnit
from pingfedsdk.enums import MaxTimeoutDisplayUnit


class GlobalAuthenticationSessionPolicy(Model):
    """The global policy for authentication sessions.

    Attributes
    ----------
    enableSessions: bool
        Determines whether authentication sessions are enabled globally.

    persistentSessions: bool
        Determines whether authentication sessions are persistent by default. Persistent sessions are linked to a persistent cookie and stored in a data store. This field is ignored if enableSessions is false.

    hashUniqueUserKeyAttribute: bool
        Determines whether to hash the value of the unique user key attribute.

    idleTimeoutMins: int
        The idle timeout period, in minutes. If set to -1, the idle timeout will be set to the maximum timeout. The default is 60.

    idleTimeoutDisplayUnit: IdleTimeoutDisplayUnit
        The display unit for the idle timeout period in the PingFederate administrative console. When the display unit is HOURS or DAYS, the timeout value in minutes must correspond to a whole number value for the specified unit.

    maxTimeoutMins: int
        The maximum timeout period, in minutes. If set to -1, sessions do not expire. The default is 480.

    maxTimeoutDisplayUnit: MaxTimeoutDisplayUnit
        The display unit for the maximum timeout period in the PingFederate administrative console. When the display unit is HOURS or DAYS, the timeout value in minutes must correspond to a whole number value for the specified unit.

    """

    def __init__(self, enableSessions: bool, persistentSessions: bool = None, hashUniqueUserKeyAttribute: bool = None, idleTimeoutMins: int = None, idleTimeoutDisplayUnit: IdleTimeoutDisplayUnit = None, maxTimeoutMins: int = None, maxTimeoutDisplayUnit: MaxTimeoutDisplayUnit = None) -> None:
        self.enableSessions = enableSessions
        self.persistentSessions = persistentSessions
        self.hashUniqueUserKeyAttribute = hashUniqueUserKeyAttribute
        self.idleTimeoutMins = idleTimeoutMins
        self.idleTimeoutDisplayUnit = idleTimeoutDisplayUnit
        self.maxTimeoutMins = maxTimeoutMins
        self.maxTimeoutDisplayUnit = maxTimeoutDisplayUnit

    def _validate(self) -> bool:
        return any(x for x in ["enableSessions"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, GlobalAuthenticationSessionPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.enableSessions, self.persistentSessions, self.hashUniqueUserKeyAttribute, self.idleTimeoutMins, self.idleTimeoutDisplayUnit, self.maxTimeoutMins, self.maxTimeoutDisplayUnit]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["enableSessions", "persistentSessions", "hashUniqueUserKeyAttribute", "idleTimeoutMins", "idleTimeoutDisplayUnit", "maxTimeoutMins", "maxTimeoutDisplayUnit"] and v is not None:
                if k == "enableSessions":
                    valid_data[k] = bool(v)
                if k == "persistentSessions":
                    valid_data[k] = bool(v)
                if k == "hashUniqueUserKeyAttribute":
                    valid_data[k] = bool(v)
                if k == "idleTimeoutMins":
                    valid_data[k] = int(v)
                if k == "idleTimeoutDisplayUnit":
                    valid_data[k] = IdleTimeoutDisplayUnit[v]
                if k == "maxTimeoutMins":
                    valid_data[k] = int(v)
                if k == "maxTimeoutDisplayUnit":
                    valid_data[k] = MaxTimeoutDisplayUnit[v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["enableSessions", "persistentSessions", "hashUniqueUserKeyAttribute", "idleTimeoutMins", "idleTimeoutDisplayUnit", "maxTimeoutMins", "maxTimeoutDisplayUnit"]:
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
