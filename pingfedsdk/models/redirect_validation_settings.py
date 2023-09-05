from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.redirect_validation_local_settings import RedirectValidationLocalSettings
from pingfedsdk.models.redirect_validation_partner_settings import RedirectValidationPartnerSettings


class RedirectValidationSettings(Model):
    """Settings for redirect validation for SSO, SLO and IdP discovery.

    Attributes
    ----------
    redirectValidationLocalSettings: RedirectValidationLocalSettings
        Settings for local redirect validation.

    redirectValidationPartnerSettings: RedirectValidationPartnerSettings
        Settings for redirection at a partner site.

    """

    def __init__(self, redirectValidationLocalSettings: RedirectValidationLocalSettings = None, redirectValidationPartnerSettings: RedirectValidationPartnerSettings = None) -> None:
        self.redirectValidationLocalSettings = redirectValidationLocalSettings
        self.redirectValidationPartnerSettings = redirectValidationPartnerSettings

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, RedirectValidationSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.redirectValidationLocalSettings, self.redirectValidationPartnerSettings]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["redirectValidationLocalSettings", "redirectValidationPartnerSettings"] and v is not None:
                if k == "redirectValidationLocalSettings":
                    valid_data[k] = RedirectValidationLocalSettings(**v)
                if k == "redirectValidationPartnerSettings":
                    valid_data[k] = RedirectValidationPartnerSettings(**v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["redirectValidationLocalSettings", "redirectValidationPartnerSettings"]:
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
