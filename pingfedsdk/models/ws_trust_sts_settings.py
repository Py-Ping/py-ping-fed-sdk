from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.models.username_password_credentials import UsernamePasswordCredentials


class WsTrustStsSettings(Model):
    """Configure PingFederate to require that client applications provide credentials to access the WS-Trust STS endpoints.

    Attributes
    ----------
    basicAuthnEnabled: bool
        Require the use of HTTP Basic Authentication to access WS-Trust STS endpoints. Requires users be populated.

    clientCertAuthnEnabled: bool
        Require the use of Client Cert Authentication to access WS-Trust STS endpoints. Requires either restrictBySubjectDn and/or restrictByIssuerCert be enabled.

    restrictBySubjectDn: bool
        Restrict Access by Subject DN. Ignored if clientCertAuthnEnabled is disabled.

    restrictByIssuerCert: bool
        Restrict Access by Issuer Certificate. Ignored if clientCertAuthnEnabled is disabled.

    subjectDns: list
        List of Subject DNs for certificates that are allowed to authenticate to WS-Trust STS endpoints. Required if restrictBySubjectDn is enabled.

    users: list
        List of users authorized to access WS-Trust STS endpoints when basicAuthnEnabled is enabled. At least one users entry is required if basicAuthnEnabled is enabled.

    issuerCerts: list
        List of certificate Issuers that are used to validate certificates for access to the WS-Trust STS endpoints. Required if restrictByIssuerCert is enabled.

    """

    def __init__(self, basicAuthnEnabled: bool = None, clientCertAuthnEnabled: bool = None, restrictBySubjectDn: bool = None, restrictByIssuerCert: bool = None, subjectDns: list = None, users: list = None, issuerCerts: list = None) -> None:
        self.basicAuthnEnabled = basicAuthnEnabled
        self.clientCertAuthnEnabled = clientCertAuthnEnabled
        self.restrictBySubjectDn = restrictBySubjectDn
        self.restrictByIssuerCert = restrictByIssuerCert
        self.subjectDns = subjectDns
        self.users = users
        self.issuerCerts = issuerCerts

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, WsTrustStsSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.basicAuthnEnabled, self.clientCertAuthnEnabled, self.restrictBySubjectDn, self.restrictByIssuerCert, self.subjectDns, self.users, self.issuerCerts]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["basicAuthnEnabled", "clientCertAuthnEnabled", "restrictBySubjectDn", "restrictByIssuerCert", "subjectDns", "users", "issuerCerts"] and v is not None:
                if k == "basicAuthnEnabled":
                    valid_data[k] = bool(v)
                if k == "clientCertAuthnEnabled":
                    valid_data[k] = bool(v)
                if k == "restrictBySubjectDn":
                    valid_data[k] = bool(v)
                if k == "restrictByIssuerCert":
                    valid_data[k] = bool(v)
                if k == "subjectDns":
                    valid_data[k] = [str(x) for x in v]
                if k == "users":
                    valid_data[k] = [UsernamePasswordCredentials(**x) for x in v]
                if k == "issuerCerts":
                    valid_data[k] = [ResourceLink(**x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["basicAuthnEnabled", "clientCertAuthnEnabled", "restrictBySubjectDn", "restrictByIssuerCert", "subjectDns", "users", "issuerCerts"]:
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
