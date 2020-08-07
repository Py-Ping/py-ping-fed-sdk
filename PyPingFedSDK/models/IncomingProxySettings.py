class IncomingProxySettings():
    """Incoming Proxy Settings.

    Attributes
    ----------
    clientCertChainSSLHeaderName : string
 While the proxy server is configured to pass client certificates as HTTP request headers, specify the chain header name here.
    clientCertSSLHeaderName : string
 While the proxy server is configured to pass client certificates as HTTP request headers, specify the header name here.
    forwardedHostHeaderIndex : str
 PingFederate combines multiple comma-separated header values into the same order that they are received. Define which hostname you want to use. Default is to use the last hostname.
    forwardedHostHeaderName : string
 Globally specify the header name (for example, X-Forwarded-Host) where PingFederate should attempt to retrieve the hostname and port in all HTTP requests.
    forwardedIpAddressHeaderIndex : str
 PingFederate combines multiple comma-separated header values into the same order that they are received. Define which IP address you want to use. Default is to use the last address.
    forwardedIpAddressHeaderName : string
 Globally specify the header name (for example, X-Forwarded-For) where PingFederate should attempt to retrieve the client IP address in all HTTP requests.
    proxyTerminatesHttpsConns : boolean
 Allows you to globally specify that connections to the reverse proxy are made over HTTPS even when HTTP is used between the reverse proxy and PingFederate.

    """

    def __init__(self, clientCertChainSSLHeaderName=None, clientCertSSLHeaderName=None, forwardedHostHeaderIndex=None, forwardedHostHeaderName=None, forwardedIpAddressHeaderIndex=None, forwardedIpAddressHeaderName=None, proxyTerminatesHttpsConns=None) -> None:
        self.clientCertChainSSLHeaderName = clientCertChainSSLHeaderName
        self.clientCertSSLHeaderName = clientCertSSLHeaderName
        self.forwardedHostHeaderIndex = forwardedHostHeaderIndex
        self.forwardedHostHeaderName = forwardedHostHeaderName
        self.forwardedIpAddressHeaderIndex = forwardedIpAddressHeaderIndex
        self.forwardedIpAddressHeaderName = forwardedIpAddressHeaderName
        self.proxyTerminatesHttpsConns = proxyTerminatesHttpsConns

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, IncomingProxySettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.clientCertChainSSLHeaderName, self.clientCertSSLHeaderName, self.forwardedHostHeaderIndex, self.forwardedHostHeaderName, self.forwardedIpAddressHeaderIndex, self.forwardedIpAddressHeaderName, self.proxyTerminatesHttpsConns))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["clientCertChainSSLHeaderName", "clientCertSSLHeaderName", "forwardedHostHeaderIndex", "forwardedHostHeaderName", "forwardedIpAddressHeaderIndex", "forwardedIpAddressHeaderName", "proxyTerminatesHttpsConns"]}

        return cls(**valid_data)