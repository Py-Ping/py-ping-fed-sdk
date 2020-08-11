class AuthenticationSessionPolicy():
    """The session policy for a specified authentication source.

    Attributes
    ----------
    authenticationSource : str
        The authentication source this session policy applies to. This property cannot be changed after the policy is created.
    authnContextSensitive : boolean
        Determines whether the requested authentication context is considered when deciding whether an existing session is valid for a given request. The default is false.
    enableSessions : boolean
        Determines whether sessions are enabled for the authentication source. This value overrides the enableSessions value from the global authentication session policy.
    id : string
        The persistent, unique ID for the session policy. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified.
    idleTimeoutMins : integer
        The idle timeout period, in minutes. If omitted, the value from the global authentication session policy will be used. If set to -1, the idle timeout will be set to the maximum timeout. If a value is provided for this property, a value must also be provided for maxTimeoutMins.
    maxTimeoutMins : integer
        The maximum timeout period, in minutes. If omitted, the value from the global authentication session policy will be used. If set to -1, sessions do not expire. If a value is provided for this property, a value must also be provided for idleTimeoutMins.
    persistent : boolean
        Determines whether sessions for the authentication source are persistent. This value overrides the persistentSessions value from the global authentication session policy. This field is ignored if enableSessions is false.
    timeoutDisplayUnit : str
        The display unit for session timeout periods in the PingFederate administrative console. When the display unit is HOURS or DAYS, the timeout values in minutes must correspond to a whole number value for the specified unit.

    """

    def __init__(self, authenticationSource, enableSessions:bool, authnContextSensitive:bool=None, var_id:str=None, idleTimeoutMins:int=None, maxTimeoutMins:int=None, persistent:bool=None, timeoutDisplayUnit=None) -> None:
        self.authenticationSource = authenticationSource
        self.authnContextSensitive = authnContextSensitive
        self.enableSessions = enableSessions
        self.var_id = var_id
        self.idleTimeoutMins = idleTimeoutMins
        self.maxTimeoutMins = maxTimeoutMins
        self.persistent = persistent
        self.timeoutDisplayUnit = timeoutDisplayUnit

    def _validate(self) -> bool:
        return any(x for x in ["authenticationSource", "enableSessions"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthenticationSessionPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.authenticationSource, self.authnContextSensitive, self.enableSessions, self.var_id, self.idleTimeoutMins, self.maxTimeoutMins, self.persistent, self.timeoutDisplayUnit))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["authenticationSource", "authnContextSensitive", "enableSessions", "var_id", "idleTimeoutMins", "maxTimeoutMins", "persistent", "timeoutDisplayUnit"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__