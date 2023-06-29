from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.sp_browser_sso_attribute import SpBrowserSsoAttribute


class SpBrowserSsoAttributeContract(Model):
    """A set of user attributes that the IdP sends in the SAML assertion.

    Attributes
    ----------
    coreAttributes: list
        A list of read-only assertion attributes (for example, SAML_SUBJECT) that are automatically populated by PingFederate.

    extendedAttributes: list
        A list of additional attributes that are added to the outgoing assertion.

    """

    def __init__(self, coreAttributes: list = None, extendedAttributes: list = None) -> None:
        self.coreAttributes = coreAttributes
        self.extendedAttributes = extendedAttributes

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SpBrowserSsoAttributeContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.coreAttributes, self.extendedAttributes]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["coreAttributes", "extendedAttributes"] and v is not None:
                if k == "coreAttributes":
                    valid_data[k] = [SpBrowserSsoAttribute(**x) for x in v]
                if k == "extendedAttributes":
                    valid_data[k] = [SpBrowserSsoAttribute(**x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["coreAttributes", "extendedAttributes"]:
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
