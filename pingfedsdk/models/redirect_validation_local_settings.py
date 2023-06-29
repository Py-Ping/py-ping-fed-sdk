from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.redirect_validation_settings_whitelist_entry import RedirectValidationSettingsWhitelistEntry


class RedirectValidationLocalSettings(Model):
    """Settings for local redirect validation.

    Attributes
    ----------
    enableTargetResourceValidationForSSO: bool
        Enable target resource validation for SSO.

    enableTargetResourceValidationForSLO: bool
        Enable target resource validation for SLO.

    enableTargetResourceValidationForIdpDiscovery: bool
        Enable target resource validation for IdP discovery.

    enableInErrorResourceValidation: bool
        Enable validation for error resource.

    whiteList: list
        List of URLs that are designated as valid target resources.

    """

    def __init__(self, enableTargetResourceValidationForSSO: bool = None, enableTargetResourceValidationForSLO: bool = None, enableTargetResourceValidationForIdpDiscovery: bool = None, enableInErrorResourceValidation: bool = None, whiteList: list = None) -> None:
        self.enableTargetResourceValidationForSSO = enableTargetResourceValidationForSSO
        self.enableTargetResourceValidationForSLO = enableTargetResourceValidationForSLO
        self.enableTargetResourceValidationForIdpDiscovery = enableTargetResourceValidationForIdpDiscovery
        self.enableInErrorResourceValidation = enableInErrorResourceValidation
        self.whiteList = whiteList

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, RedirectValidationLocalSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.enableTargetResourceValidationForSSO, self.enableTargetResourceValidationForSLO, self.enableTargetResourceValidationForIdpDiscovery, self.enableInErrorResourceValidation, self.whiteList]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["enableTargetResourceValidationForSSO", "enableTargetResourceValidationForSLO", "enableTargetResourceValidationForIdpDiscovery", "enableInErrorResourceValidation", "whiteList"] and v is not None:
                if k == "enableTargetResourceValidationForSSO":
                    valid_data[k] = bool(v)
                if k == "enableTargetResourceValidationForSLO":
                    valid_data[k] = bool(v)
                if k == "enableTargetResourceValidationForIdpDiscovery":
                    valid_data[k] = bool(v)
                if k == "enableInErrorResourceValidation":
                    valid_data[k] = bool(v)
                if k == "whiteList":
                    valid_data[k] = [RedirectValidationSettingsWhitelistEntry(**x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["enableTargetResourceValidationForSSO", "enableTargetResourceValidationForSLO", "enableTargetResourceValidationForIdpDiscovery", "enableInErrorResourceValidation", "whiteList"]:
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
