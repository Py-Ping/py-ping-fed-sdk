from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.resource_link import ResourceLink


class AuthnApiSettings(Model):
    """Authentication API Application Settings.

    Attributes
    ----------
    apiEnabled: bool
        Specifies whether the authentication API is enabled. The default value is false.

    defaultApplicationRef: ResourceLink
        Application for non authentication policy use cases.

    enableApiDescriptions: bool
        Enable the API Descriptions endpoint.

    restrictAccessToRedirectlessMode: bool
        Determines whether access to the authentication API redirectless mode is restricted to specified applications.

    includeRequestContext: bool
        Determines whether the request context parameters are included in response for authentication API. The default value is false.

    """
    def __init__(self, apiEnabled: bool = None, defaultApplicationRef: ResourceLink = None, enableApiDescriptions: bool = None, restrictAccessToRedirectlessMode: bool = None, includeRequestContext: bool = None) -> None:
        self.apiEnabled = apiEnabled
        self.defaultApplicationRef = defaultApplicationRef
        self.enableApiDescriptions = enableApiDescriptions
        self.restrictAccessToRedirectlessMode = restrictAccessToRedirectlessMode
        self.includeRequestContext = includeRequestContext

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthnApiSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.apiEnabled, self.defaultApplicationRef, self.enableApiDescriptions, self.restrictAccessToRedirectlessMode, self.includeRequestContext]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["apiEnabled", "defaultApplicationRef", "enableApiDescriptions", "restrictAccessToRedirectlessMode", "includeRequestContext"] and v is not None:
                if k == "apiEnabled":
                    valid_data[k] = bool(v)
                if k == "defaultApplicationRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "enableApiDescriptions":
                    valid_data[k] = bool(v)
                if k == "restrictAccessToRedirectlessMode":
                    valid_data[k] = bool(v)
                if k == "includeRequestContext":
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
            if k in ["apiEnabled", "defaultApplicationRef", "enableApiDescriptions", "restrictAccessToRedirectlessMode", "includeRequestContext"]:
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
