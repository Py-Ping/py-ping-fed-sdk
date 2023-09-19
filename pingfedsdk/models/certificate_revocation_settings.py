from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.crl_settings import CrlSettings
from pingfedsdk.models.ocsp_settings import OcspSettings
from pingfedsdk.models.proxy_settings import ProxySettings


class CertificateRevocationSettings(Model):
    """Certificate revocation settings.

    Attributes
    ----------
    ocspSettings: OcspSettings
        Certificate revocation OCSP settings. If this attribute is omitted, OCSP checks are disabled.

    crlSettings: CrlSettings
        Certificate revocation CRL settings. If this attribute is omitted, CRL checks are disabled.

    proxySettings: ProxySettings
        If OCSP messaging is routed through a proxy server, specify the server's host (DNS name or IP address) and the port number. The same proxy information applies to CRL checking, when CRL is enabled for failover.

    """
    def __init__(self, ocspSettings: OcspSettings = None, crlSettings: CrlSettings = None, proxySettings: ProxySettings = None) -> None:
        self.ocspSettings = ocspSettings
        self.crlSettings = crlSettings
        self.proxySettings = proxySettings

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, CertificateRevocationSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.ocspSettings, self.crlSettings, self.proxySettings]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["ocspSettings", "crlSettings", "proxySettings"] and v is not None:
                if k == "ocspSettings":
                    valid_data[k] = OcspSettings.from_dict(v)
                if k == "crlSettings":
                    valid_data[k] = CrlSettings.from_dict(v)
                if k == "proxySettings":
                    valid_data[k] = ProxySettings.from_dict(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["ocspSettings", "crlSettings", "proxySettings"]:
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
