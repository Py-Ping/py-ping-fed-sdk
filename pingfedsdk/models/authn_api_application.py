from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink


class AuthnApiApplication(Model):
    """Authentication API Application.

    Attributes
    ----------
    id: str
        The persistent, unique ID for the Authentication API application. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.

    name: str
        The Authentication API Application Name. Name must be unique.

    url: str
        The Authentication API Application redirect URL.

    description: str
        The Authentication API Application description.

    additionalAllowedOrigins: list
        The domain in the redirect URL is always whitelisted. This field contains a list of additional allowed origin URL's for cross-origin resource sharing.

    clientForRedirectlessModeRef: ResourceLink
        The client this application must use if it invokes the authentication API in redirectless mode. No client may be specified if restrictAccessToRedirectlessMode is false under /authenticationApi/settings.

    """

    def __init__(self, id: str, name: str, url: str, description: str = None, additionalAllowedOrigins: list = None, clientForRedirectlessModeRef: ResourceLink = None) -> None:
        self.id = id
        self.name = name
        self.url = url
        self.description = description
        self.additionalAllowedOrigins = additionalAllowedOrigins
        self.clientForRedirectlessModeRef = clientForRedirectlessModeRef

    def _validate(self) -> bool:
        return any(x for x in ["id", "name", "url"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthnApiApplication):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.name, self.url, self.description, self.additionalAllowedOrigins, self.clientForRedirectlessModeRef]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "name", "url", "description", "additionalAllowedOrigins", "clientForRedirectlessModeRef"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "url":
                    valid_data[k] = str(v)
                if k == "description":
                    valid_data[k] = str(v)
                if k == "additionalAllowedOrigins":
                    valid_data[k] = [str(x) for x in v]
                if k == "clientForRedirectlessModeRef":
                    valid_data[k] = ResourceLink(**v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "name", "url", "description", "additionalAllowedOrigins", "clientForRedirectlessModeRef"]:
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
