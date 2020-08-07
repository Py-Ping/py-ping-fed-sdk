class GlobalAuthenticationSessionPolicy():
    """The global policy for authentication sessions.

    Attributes
    ----------
    enableSessions : boolean
 Determines whether authentication sessions are enabled globally.
    idleTimeoutDisplayUnit : str
 The display unit for the idle timeout period in the PingFederate administrative console. When the display unit is HOURS or DAYS, the timeout value in minutes must correspond to a whole number value for the specified unit.
    idleTimeoutMins : integer
 The idle timeout period, in minutes. If set to -1, the idle timeout will be set to the maximum timeout. The default is 60.
    maxTimeoutDisplayUnit : str
 The display unit for the maximum timeout period in the PingFederate administrative console. When the display unit is HOURS or DAYS, the timeout value in minutes must correspond to a whole number value for the specified unit.
    maxTimeoutMins : integer
 The maximum timeout period, in minutes. If set to -1, sessions do not expire. The default is 480.
    persistentSessions : boolean
 Determines whether authentication sessions are persistent by default. Persistent sessions are linked to a persistent cookie and stored in a data store. This field is ignored if enableSessions is false.

    """

    def __init__(self, enableSessions, idleTimeoutDisplayUnit=None, idleTimeoutMins=None, maxTimeoutDisplayUnit=None, maxTimeoutMins=None, persistentSessions=None) -> None:
        self.enableSessions = enableSessions
        self.idleTimeoutDisplayUnit = idleTimeoutDisplayUnit
        self.idleTimeoutMins = idleTimeoutMins
        self.maxTimeoutDisplayUnit = maxTimeoutDisplayUnit
        self.maxTimeoutMins = maxTimeoutMins
        self.persistentSessions = persistentSessions

    def _validate(self) -> bool:
        return any(x for x in ["enableSessions"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, GlobalAuthenticationSessionPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.enableSessions, self.idleTimeoutDisplayUnit, self.idleTimeoutMins, self.maxTimeoutDisplayUnit, self.maxTimeoutMins, self.persistentSessions))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["enableSessions", "idleTimeoutDisplayUnit", "idleTimeoutMins", "maxTimeoutDisplayUnit", "maxTimeoutMins", "persistentSessions"]}

        return cls(**valid_data)