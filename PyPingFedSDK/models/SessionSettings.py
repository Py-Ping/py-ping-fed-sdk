class SessionSettings():
    """General settings related to session management.

    Attributes
    ----------
    revokeUserSessionOnLogout : boolean
        Determines whether the user's session is revoked on logout. If this property is not provided on a PUT, the setting is left unchanged.    sessionRevocationLifetime : integer
        How long a session revocation is tracked and stored, in minutes. If this property is not provided on a PUT, the setting is left unchanged.    trackAdapterSessionsForLogout : boolean
        Determines whether adapter sessions are tracked for cleanup during single logout. The default is false.
    """

    __slots__ = ["revokeUserSessionOnLogout", "sessionRevocationLifetime", "trackAdapterSessionsForLogout"]

    def __init__(self, revokeUserSessionOnLogout=None, sessionRevocationLifetime=None, trackAdapterSessionsForLogout=None):
        self.revokeUserSessionOnLogout: bool = revokeUserSessionOnLogout
        self.sessionRevocationLifetime: str = sessionRevocationLifetime
        self.trackAdapterSessionsForLogout: bool = trackAdapterSessionsForLogout

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, SessionSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.revokeUserSessionOnLogout, self.sessionRevocationLifetime, self.trackAdapterSessionsForLogout))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["revokeUserSessionOnLogout", "sessionRevocationLifetime", "trackAdapterSessionsForLogout"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__