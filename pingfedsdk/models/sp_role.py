from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.sp_s_a_m_l_2_0_profile import SpSAML20Profile


class SpRole(Model):
    """This property has been deprecated and is no longer used. All Roles and protocols are always enabled.

    Attributes
    ----------
    enable: bool
        Enable Service Provider Role.

    enableSaml11: bool
        Enable SAML 1.1.

    enableSaml10: bool
        Enable SAML 1.0.

    enableWsFed: bool
        Enable WS Federation.

    enableWsTrust: bool
        Enable WS Trust.

    saml20Profile: SpSAML20Profile
        SAML 2.0 Profile settings.

    enableOpenIDConnect: bool
        Enable OpenID Connect.

    enableInboundProvisioning: bool
        Enable Inbound Provisioning.

    """
    def __init__(self, enable: bool = None, saml20Profile: SpSAML20Profile = None, enableSaml11: bool = None, enableSaml10: bool = None, enableWsFed: bool = None, enableWsTrust: bool = None, enableOpenIDConnect: bool = None, enableInboundProvisioning: bool = None) -> None:
        self.enable = enable
        self.enableSaml11 = enableSaml11
        self.enableSaml10 = enableSaml10
        self.enableWsFed = enableWsFed
        self.enableWsTrust = enableWsTrust
        self.saml20Profile = saml20Profile
        self.enableOpenIDConnect = enableOpenIDConnect
        self.enableInboundProvisioning = enableInboundProvisioning

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SpRole):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.enable, self.enableSaml11, self.enableSaml10, self.enableWsFed, self.enableWsTrust, self.saml20Profile, self.enableOpenIDConnect, self.enableInboundProvisioning]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["enable", "enableSaml11", "enableSaml10", "enableWsFed", "enableWsTrust", "saml20Profile", "enableOpenIDConnect", "enableInboundProvisioning"] and v is not None:
                if k == "enable":
                    valid_data[k] = bool(v)
                if k == "enableSaml11":
                    valid_data[k] = bool(v)
                if k == "enableSaml10":
                    valid_data[k] = bool(v)
                if k == "enableWsFed":
                    valid_data[k] = bool(v)
                if k == "enableWsTrust":
                    valid_data[k] = bool(v)
                if k == "saml20Profile":
                    valid_data[k] = SpSAML20Profile.from_dict(v)
                if k == "enableOpenIDConnect":
                    valid_data[k] = bool(v)
                if k == "enableInboundProvisioning":
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
            if k in ["enable", "enableSaml11", "enableSaml10", "enableWsFed", "enableWsTrust", "saml20Profile", "enableOpenIDConnect", "enableInboundProvisioning"]:
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
