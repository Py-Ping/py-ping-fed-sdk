from enum import Enum

from pingfedsdk.model import Model


class OIDCSessionSettings(Model):
    """Settings relating to OpenID Connect session management.

    Attributes
    ----------
    trackUserSessionsForLogout: bool
        Determines whether user sessions are tracked for logout. This property is now available under /oauth/authServerSettings and should be accessed through that resource.

    revokeUserSessionOnLogout: bool
        Determines whether the user's session is revoked on logout. This property is now available under /session/settings and should be accessed through that resource.

    sessionRevocationLifetime: int
        How long a session revocation is tracked and stored, in minutes. This property is now available under /session/settings and should be accessed through that resource.

    """
    def __init__(self, trackUserSessionsForLogout: bool = None, revokeUserSessionOnLogout: bool = None, sessionRevocationLifetime: int = None) -> None:
        self.trackUserSessionsForLogout = trackUserSessionsForLogout
        self.revokeUserSessionOnLogout = revokeUserSessionOnLogout
        self.sessionRevocationLifetime = sessionRevocationLifetime

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OIDCSessionSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.trackUserSessionsForLogout, self.revokeUserSessionOnLogout, self.sessionRevocationLifetime]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["trackUserSessionsForLogout", "revokeUserSessionOnLogout", "sessionRevocationLifetime"] and v is not None:
                if k == "trackUserSessionsForLogout":
                    valid_data[k] = bool(v)
                if k == "revokeUserSessionOnLogout":
                    valid_data[k] = bool(v)
                if k == "sessionRevocationLifetime":
                    valid_data[k] = int(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["trackUserSessionsForLogout", "revokeUserSessionOnLogout", "sessionRevocationLifetime"]:
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
