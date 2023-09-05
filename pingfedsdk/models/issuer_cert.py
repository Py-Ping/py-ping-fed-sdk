from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.cert_view import CertView
from pingfedsdk.models.x_5_0_9_file import X509File


class IssuerCert(Model):
    """A certificate used to validate certificates for access to the WS-Trust STS endpoints.

    Attributes
    ----------
    certView: CertView
        Certificate details. This property is read-only and is always ignored on a POST or PUT.

    x509File: X509File
        The certificate data. This property must always be supplied on a POST or PUT.

    active: bool
        Indicates whether this an active certificate or not.

    """

    def __init__(self, x509File: X509File, certView: CertView = None, active: bool = None) -> None:
        self.certView = certView
        self.x509File = x509File
        self.active = active

    def _validate(self) -> bool:
        return any(x for x in ["x509File"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, IssuerCert):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.certView, self.x509File, self.active]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["certView", "x509File", "active"] and v is not None:
                if k == "certView":
                    valid_data[k] = CertView(**v)
                if k == "x509File":
                    valid_data[k] = X509File(**v)
                if k == "active":
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
            if k in ["certView", "x509File", "active"]:
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
