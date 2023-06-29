from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.o_auth_role import OAuthRole
from pingfedsdk.models.idp_role import IdpRole
from pingfedsdk.models.sp_role import SpRole


class RolesAndProtocols(Model):
    """This property has been deprecated and is no longer used. All Roles and protocols are always enabled.

    Attributes
    ----------
    oauthRole: OAuthRole
        OAuth role settings.

    idpRole: IdpRole
        Identity Provider (IdP) settings.

    spRole: SpRole
        Service Provider (SP) settings.

    enableIdpDiscovery: bool
        Enable IdP Discovery.

    """

    def __init__(self, oauthRole: OAuthRole = None, idpRole: IdpRole = None, spRole: SpRole = None, enableIdpDiscovery: bool = None) -> None:
        self.oauthRole = oauthRole
        self.idpRole = idpRole
        self.spRole = spRole
        self.enableIdpDiscovery = enableIdpDiscovery

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, RolesAndProtocols):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.oauthRole, self.idpRole, self.spRole, self.enableIdpDiscovery]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["oauthRole", "idpRole", "spRole", "enableIdpDiscovery"] and v is not None:
                if k == "oauthRole":
                    valid_data[k] = OAuthRole(**v)
                if k == "idpRole":
                    valid_data[k] = IdpRole(**v)
                if k == "spRole":
                    valid_data[k] = SpRole(**v)
                if k == "enableIdpDiscovery":
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
            if k in ["oauthRole", "idpRole", "spRole", "enableIdpDiscovery"]:
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
