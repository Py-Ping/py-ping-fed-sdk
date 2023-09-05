from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.authentication_source import AuthenticationSource
from pingfedsdk.enums import TimeoutDisplayUnit


class AuthenticationSessionPolicy(Model):
    """The session policy for a specified authentication source.

    Attributes
    ----------
    id: str
        The persistent, unique ID for the session policy. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified.

    authenticationSource: AuthenticationSource
        The authentication source this session policy applies to. This property cannot be changed after the policy is created.

    enableSessions: bool
        Determines whether sessions are enabled for the authentication source. This value overrides the enableSessions value from the global authentication session policy.

    persistent: bool
        Determines whether sessions for the authentication source are persistent. This value overrides the persistentSessions value from the global authentication session policy. This field is ignored if enableSessions is false.

    idleTimeoutMins: int
        The idle timeout period, in minutes. If omitted, the value from the global authentication session policy will be used. If set to -1, the idle timeout will be set to the maximum timeout. If a value is provided for this property, a value must also be provided for maxTimeoutMins.

    maxTimeoutMins: int
        The maximum timeout period, in minutes. If omitted, the value from the global authentication session policy will be used. If set to -1, sessions do not expire. If a value is provided for this property, a value must also be provided for idleTimeoutMins.

    timeoutDisplayUnit: TimeoutDisplayUnit
        The display unit for session timeout periods in the PingFederate administrative console. When the display unit is HOURS or DAYS, the timeout values in minutes must correspond to a whole number value for the specified unit.

    authnContextSensitive: bool
        Determines whether the requested authentication context is considered when deciding whether an existing session is valid for a given request. The default is false.

    """

    def __init__(self, authenticationSource: AuthenticationSource, enableSessions: bool, id: str = None, persistent: bool = None, idleTimeoutMins: int = None, maxTimeoutMins: int = None, timeoutDisplayUnit: TimeoutDisplayUnit = None, authnContextSensitive: bool = None) -> None:
        self.id = id
        self.authenticationSource = authenticationSource
        self.enableSessions = enableSessions
        self.persistent = persistent
        self.idleTimeoutMins = idleTimeoutMins
        self.maxTimeoutMins = maxTimeoutMins
        self.timeoutDisplayUnit = timeoutDisplayUnit
        self.authnContextSensitive = authnContextSensitive

    def _validate(self) -> bool:
        return any(x for x in ["authenticationSource", "enableSessions"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthenticationSessionPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.authenticationSource, self.enableSessions, self.persistent, self.idleTimeoutMins, self.maxTimeoutMins, self.timeoutDisplayUnit, self.authnContextSensitive]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "authenticationSource", "enableSessions", "persistent", "idleTimeoutMins", "maxTimeoutMins", "timeoutDisplayUnit", "authnContextSensitive"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "authenticationSource":
                    valid_data[k] = AuthenticationSource(**v)
                if k == "enableSessions":
                    valid_data[k] = bool(v)
                if k == "persistent":
                    valid_data[k] = bool(v)
                if k == "idleTimeoutMins":
                    valid_data[k] = int(v)
                if k == "maxTimeoutMins":
                    valid_data[k] = int(v)
                if k == "timeoutDisplayUnit":
                    valid_data[k] = TimeoutDisplayUnit[v]
                if k == "authnContextSensitive":
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
            if k in ["id", "authenticationSource", "enableSessions", "persistent", "idleTimeoutMins", "maxTimeoutMins", "timeoutDisplayUnit", "authnContextSensitive"]:
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
