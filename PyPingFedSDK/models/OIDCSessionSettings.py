class OIDCSessionSettings():
    """Settings relating to OpenID Connect session management.

    Attributes
    ----------
    revokeUserSessionOnLogout : boolean
 Determines whether the user's session is revoked on logout. This property is now available under /session/settings and should be accessed through that resource.
    sessionRevocationLifetime : integer
 How long a session revocation is tracked and stored, in minutes. This property is now available under /session/settings and should be accessed through that resource.
    trackUserSessionsForLogout : boolean
 Determines whether user sessions are tracked for logout. This property is now available under /oauth/authServerSettings and should be accessed through that resource.

    """

    def __init__(self, revokeUserSessionOnLogout:bool=None, sessionRevocationLifetime:int=None, trackUserSessionsForLogout:bool=None) -> None:
        self.revokeUserSessionOnLogout = revokeUserSessionOnLogout
        self.sessionRevocationLifetime = sessionRevocationLifetime
        self.trackUserSessionsForLogout = trackUserSessionsForLogout

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, OIDCSessionSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.revokeUserSessionOnLogout, self.sessionRevocationLifetime, self.trackUserSessionsForLogout))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["revokeUserSessionOnLogout", "sessionRevocationLifetime", "trackUserSessionsForLogout"]}

        return cls(**valid_data)