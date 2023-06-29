from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.enums import ForwardedHeaderIndex


class IncomingProxySettings(Model):
    """Incoming Proxy Settings.

    Attributes
    ----------
    forwardedIpAddressHeaderName: str
        Globally specify the header name (for example, X-Forwarded-For) where PingFederate should attempt to retrieve the client IP address in all HTTP requests.

    forwardedIpAddressHeaderIndex: ForwardedHeaderIndex
        PingFederate combines multiple comma-separated header values into the same order that they are received. Define which IP address you want to use. Default is to use the last address.

    forwardedHostHeaderName: str
        Globally specify the header name (for example, X-Forwarded-Host) where PingFederate should attempt to retrieve the hostname and port in all HTTP requests.

    forwardedHostHeaderIndex: ForwardedHeaderIndex
        PingFederate combines multiple comma-separated header values into the same order that they are received. Define which hostname you want to use. Default is to use the last hostname.

    clientCertSSLHeaderName: str
        While the proxy server is configured to pass client certificates as HTTP request headers, specify the header name here.

    clientCertChainSSLHeaderName: str
        While the proxy server is configured to pass client certificates as HTTP request headers, specify the chain header name here.

    proxyTerminatesHttpsConns: bool
        Allows you to globally specify that connections to the reverse proxy are made over HTTPS even when HTTP is used between the reverse proxy and PingFederate.

    """

    def __init__(self, forwardedIpAddressHeaderName: str = None, forwardedIpAddressHeaderIndex: ForwardedHeaderIndex = None, forwardedHostHeaderName: str = None, forwardedHostHeaderIndex: ForwardedHeaderIndex = None, clientCertSSLHeaderName: str = None, clientCertChainSSLHeaderName: str = None, proxyTerminatesHttpsConns: bool = None) -> None:
        self.forwardedIpAddressHeaderName = forwardedIpAddressHeaderName
        self.forwardedIpAddressHeaderIndex = forwardedIpAddressHeaderIndex
        self.forwardedHostHeaderName = forwardedHostHeaderName
        self.forwardedHostHeaderIndex = forwardedHostHeaderIndex
        self.clientCertSSLHeaderName = clientCertSSLHeaderName
        self.clientCertChainSSLHeaderName = clientCertChainSSLHeaderName
        self.proxyTerminatesHttpsConns = proxyTerminatesHttpsConns

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, IncomingProxySettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.forwardedIpAddressHeaderName, self.forwardedIpAddressHeaderIndex, self.forwardedHostHeaderName, self.forwardedHostHeaderIndex, self.clientCertSSLHeaderName, self.clientCertChainSSLHeaderName, self.proxyTerminatesHttpsConns]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["forwardedIpAddressHeaderName", "forwardedIpAddressHeaderIndex", "forwardedHostHeaderName", "forwardedHostHeaderIndex", "clientCertSSLHeaderName", "clientCertChainSSLHeaderName", "proxyTerminatesHttpsConns"] and v is not None:
                if k == "forwardedIpAddressHeaderName":
                    valid_data[k] = str(v)
                if k == "forwardedIpAddressHeaderIndex":
                    valid_data[k] = ForwardedHeaderIndex[v]
                if k == "forwardedHostHeaderName":
                    valid_data[k] = str(v)
                if k == "forwardedHostHeaderIndex":
                    valid_data[k] = ForwardedHeaderIndex[v]
                if k == "clientCertSSLHeaderName":
                    valid_data[k] = str(v)
                if k == "clientCertChainSSLHeaderName":
                    valid_data[k] = str(v)
                if k == "proxyTerminatesHttpsConns":
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
            if k in ["forwardedIpAddressHeaderName", "forwardedIpAddressHeaderIndex", "forwardedHostHeaderName", "forwardedHostHeaderIndex", "clientCertSSLHeaderName", "clientCertChainSSLHeaderName", "proxyTerminatesHttpsConns"]:
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
