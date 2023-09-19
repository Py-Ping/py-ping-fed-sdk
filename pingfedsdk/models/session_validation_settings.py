from enum import Enum

from pingfedsdk.model import Model


class SessionValidationSettings(Model):
    """Session validation settings for an access token management plugin instance.

    Attributes
    ----------
    inherited: bool
        If this token manager has a parent, this flag determines whether session validation settings, such as checkValidAuthnSession, are inherited from the parent. When set to true, the other fields in this model become read-only. The default value is false.

    includeSessionId: bool
        Include the session identifier in the access token. Note that if any of the session validation features is enabled, the session identifier will already be included in the access tokens.

    checkValidAuthnSession: bool
        Check for a valid authentication session when validating the access token.

    checkSessionRevocationStatus: bool
        Check the session revocation status when validating the access token.

    updateAuthnSessionActivity: bool
        Update authentication session activity when validating the access token.

    """
    def __init__(self, inherited: bool = None, includeSessionId: bool = None, checkValidAuthnSession: bool = None, checkSessionRevocationStatus: bool = None, updateAuthnSessionActivity: bool = None) -> None:
        self.inherited = inherited
        self.includeSessionId = includeSessionId
        self.checkValidAuthnSession = checkValidAuthnSession
        self.checkSessionRevocationStatus = checkSessionRevocationStatus
        self.updateAuthnSessionActivity = updateAuthnSessionActivity

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SessionValidationSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.inherited, self.includeSessionId, self.checkValidAuthnSession, self.checkSessionRevocationStatus, self.updateAuthnSessionActivity]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["inherited", "includeSessionId", "checkValidAuthnSession", "checkSessionRevocationStatus", "updateAuthnSessionActivity"] and v is not None:
                if k == "inherited":
                    valid_data[k] = bool(v)
                if k == "includeSessionId":
                    valid_data[k] = bool(v)
                if k == "checkValidAuthnSession":
                    valid_data[k] = bool(v)
                if k == "checkSessionRevocationStatus":
                    valid_data[k] = bool(v)
                if k == "updateAuthnSessionActivity":
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
            if k in ["inherited", "includeSessionId", "checkValidAuthnSession", "checkSessionRevocationStatus", "updateAuthnSessionActivity"]:
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
