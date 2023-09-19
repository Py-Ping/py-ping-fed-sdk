from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.o_i_d_c_session_settings import OIDCSessionSettings
from pingfedsdk.models.resource_link import ResourceLink


class OpenIdConnectSettings(Model):
    """Settings for the OpenID Connect configuration.

    Attributes
    ----------
    defaultPolicyRef: ResourceLink
        Reference to the default policy.

    sessionSettings: OIDCSessionSettings
        Settings relating to OpenID Connect session management.

    """
    def __init__(self, defaultPolicyRef: ResourceLink = None, sessionSettings: OIDCSessionSettings = None) -> None:
        self.defaultPolicyRef = defaultPolicyRef
        self.sessionSettings = sessionSettings

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OpenIdConnectSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.defaultPolicyRef, self.sessionSettings]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["defaultPolicyRef", "sessionSettings"] and v is not None:
                if k == "defaultPolicyRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "sessionSettings":
                    valid_data[k] = OIDCSessionSettings.from_dict(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["defaultPolicyRef", "sessionSettings"]:
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
