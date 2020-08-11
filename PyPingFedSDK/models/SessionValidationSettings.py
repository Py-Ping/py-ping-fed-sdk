class SessionValidationSettings():
    """Session validation settings for an access token management plugin instance.

    Attributes
    ----------
    checkSessionRevocationStatus : boolean
        Check the session revocation status when validating the access token.
    checkValidAuthnSession : boolean
        Check for a valid authentication session when validating the access token.
    inherited : boolean
        If this token manager has a parent, this flag determines whether session validation settings, such as checkValidAuthnSession, are inherited from the parent. When set to true, the other fields in this model become read-only. The default value is false.
    updateAuthnSessionActivity : boolean
        Update authentication session activity when validating the access token.

    """

    def __init__(self, checkSessionRevocationStatus:bool=None, checkValidAuthnSession:bool=None, inherited:bool=None, updateAuthnSessionActivity:bool=None) -> None:
        self.checkSessionRevocationStatus = checkSessionRevocationStatus
        self.checkValidAuthnSession = checkValidAuthnSession
        self.inherited = inherited
        self.updateAuthnSessionActivity = updateAuthnSessionActivity

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SessionValidationSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.checkSessionRevocationStatus, self.checkValidAuthnSession, self.inherited, self.updateAuthnSessionActivity))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["checkSessionRevocationStatus", "checkValidAuthnSession", "inherited", "updateAuthnSessionActivity"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__