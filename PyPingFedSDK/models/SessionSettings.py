class SessionSettings():
    """General settings related to session management.

    Attributes
    ----------
    revokeUserSessionOnLogout : boolean
 Determines whether the user's session is revoked on logout. If this property is not provided on a PUT, the setting is left unchanged.
    sessionRevocationLifetime : integer
 How long a session revocation is tracked and stored, in minutes. If this property is not provided on a PUT, the setting is left unchanged.
    trackAdapterSessionsForLogout : boolean
 Determines whether adapter sessions are tracked for cleanup during single logout. The default is false.

    """

    def __init__(self, revokeUserSessionOnLogout:bool=None, sessionRevocationLifetime:int=None, trackAdapterSessionsForLogout:bool=None) -> None:
        self.revokeUserSessionOnLogout = revokeUserSessionOnLogout
        self.sessionRevocationLifetime = sessionRevocationLifetime
        self.trackAdapterSessionsForLogout = trackAdapterSessionsForLogout

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SessionSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.revokeUserSessionOnLogout, self.sessionRevocationLifetime, self.trackAdapterSessionsForLogout))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["revokeUserSessionOnLogout", "sessionRevocationLifetime", "trackAdapterSessionsForLogout"]}

        return cls(**valid_data)