class CertificateRevocationSettings():
    """Certificate revocation settings.

    Attributes
    ----------
    crlSettings : str
 Certificate revocation CRL settings. CRL revocation is enabled by default. It will be disabled if this attribute is not defined in the request body.
    ocspSettings : str
 Certificate revocation OCSP settings. OCSP revocation is disabled by default. It will be enabled if this attribute is defined in the request body.
    proxySettings : str
 If OCSP messaging is routed through a proxy server, specify the server's host (DNS name or IP address) and the port number. The same proxy information applies to CRL checking, when CRL is enabled for failover.

    """

    def __init__(self, crlSettings=None, ocspSettings=None, proxySettings=None) -> None:
        self.crlSettings = crlSettings
        self.ocspSettings = ocspSettings
        self.proxySettings = proxySettings

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, CertificateRevocationSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.crlSettings, self.ocspSettings, self.proxySettings))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["crlSettings", "ocspSettings", "proxySettings"]}

        return cls(**valid_data)