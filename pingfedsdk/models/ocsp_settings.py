from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink


class OcspSettings(Model):
    """OCSP settings.

    Attributes
    ----------
    requesterAddNonce: bool
        Do not allow responder to use cached responses. This setting defaults to disabled.

    responderUrl: str
        Default responder URL. This URL is used if the certificate being checked does not specify an OCSP responder URL.

    responderCertReference: ResourceLink
        Resource link to OCSP responder signature verification certificate. A previously selected certificate will be deselected if this attribute is not defined.

    currentUpdateGracePeriod: int
        Current update grace period in minutes. This value defaults to "5".

    nextUpdateGracePeriod: int
        Next update grace period in minutes. This value defaults to "5".

    responseCachePeriod: int
        Response cache period in hours. This value defaults to "48".

    responderTimeout: int
        Responder connection timeout in seconds. This value defaults to "5".

    actionOnResponderUnavailable: str
        Action on responder unavailable. This value defaults to  "CONTINUE".

    actionOnStatusUnknown: str
        Action on status unknown. This value defaults to  "FAIL".

    actionOnUnsuccessfulResponse: str
        Action on unsuccessful response. This value defaults to  "FAIL".

    """

    def __init__(self, requesterAddNonce: bool = None, responderUrl: str = None, responderCertReference: ResourceLink = None, currentUpdateGracePeriod: int = None, nextUpdateGracePeriod: int = None, responseCachePeriod: int = None, responderTimeout: int = None, actionOnResponderUnavailable: str = None, actionOnStatusUnknown: str = None, actionOnUnsuccessfulResponse: str = None) -> None:
        self.requesterAddNonce = requesterAddNonce
        self.responderUrl = responderUrl
        self.responderCertReference = responderCertReference
        self.currentUpdateGracePeriod = currentUpdateGracePeriod
        self.nextUpdateGracePeriod = nextUpdateGracePeriod
        self.responseCachePeriod = responseCachePeriod
        self.responderTimeout = responderTimeout
        self.actionOnResponderUnavailable = actionOnResponderUnavailable
        self.actionOnStatusUnknown = actionOnStatusUnknown
        self.actionOnUnsuccessfulResponse = actionOnUnsuccessfulResponse

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OcspSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.requesterAddNonce, self.responderUrl, self.responderCertReference, self.currentUpdateGracePeriod, self.nextUpdateGracePeriod, self.responseCachePeriod, self.responderTimeout, self.actionOnResponderUnavailable, self.actionOnStatusUnknown, self.actionOnUnsuccessfulResponse]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["requesterAddNonce", "responderUrl", "responderCertReference", "currentUpdateGracePeriod", "nextUpdateGracePeriod", "responseCachePeriod", "responderTimeout", "actionOnResponderUnavailable", "actionOnStatusUnknown", "actionOnUnsuccessfulResponse"] and v is not None:
                if k == "requesterAddNonce":
                    valid_data[k] = bool(v)
                if k == "responderUrl":
                    valid_data[k] = str(v)
                if k == "responderCertReference":
                    valid_data[k] = ResourceLink(**v)
                if k == "currentUpdateGracePeriod":
                    valid_data[k] = int(v)
                if k == "nextUpdateGracePeriod":
                    valid_data[k] = int(v)
                if k == "responseCachePeriod":
                    valid_data[k] = int(v)
                if k == "responderTimeout":
                    valid_data[k] = int(v)
                if k == "actionOnResponderUnavailable":
                    valid_data[k] = str(v)
                if k == "actionOnStatusUnknown":
                    valid_data[k] = str(v)
                if k == "actionOnUnsuccessfulResponse":
                    valid_data[k] = str(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["requesterAddNonce", "responderUrl", "responderCertReference", "currentUpdateGracePeriod", "nextUpdateGracePeriod", "responseCachePeriod", "responderTimeout", "actionOnResponderUnavailable", "actionOnStatusUnknown", "actionOnUnsuccessfulResponse"]:
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
