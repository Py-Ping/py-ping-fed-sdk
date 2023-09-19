from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.cert_view import CertView
from pingfedsdk.models.x_5_0_9_file import X509File


class ConnectionCert(Model):
    """A certificate used for signature verification or XML encryption.

    Attributes
    ----------
    certView: CertView
        Certificate details. This property is read-only and is always ignored on a POST or PUT.

    x509File: X509File
        The certificate data. This property must always be supplied on a POST or PUT.

    activeVerificationCert: bool
        Indicates whether this is an active signature verification certificate.

    primaryVerificationCert: bool
        Indicates whether this is the primary signature verification certificate. Only one certificate in the collection can have this flag set.

    secondaryVerificationCert: bool
        Indicates whether this is the secondary signature verification certificate. Only one certificate in the collection can have this flag set.

    encryptionCert: bool
        Indicates whether to use this cert to encrypt outgoing assertions. Only one certificate in the collection can have this flag set.

    """
    def __init__(self, x509File: X509File, certView: CertView = None, activeVerificationCert: bool = None, primaryVerificationCert: bool = None, secondaryVerificationCert: bool = None, encryptionCert: bool = None) -> None:
        self.certView = certView
        self.x509File = x509File
        self.activeVerificationCert = activeVerificationCert
        self.primaryVerificationCert = primaryVerificationCert
        self.secondaryVerificationCert = secondaryVerificationCert
        self.encryptionCert = encryptionCert

    def _validate(self) -> bool:
        return any(x for x in ["x509File"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ConnectionCert):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.certView, self.x509File, self.activeVerificationCert, self.primaryVerificationCert, self.secondaryVerificationCert, self.encryptionCert]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["certView", "x509File", "activeVerificationCert", "primaryVerificationCert", "secondaryVerificationCert", "encryptionCert"] and v is not None:
                if k == "certView":
                    valid_data[k] = CertView.from_dict(v)
                if k == "x509File":
                    valid_data[k] = X509File.from_dict(v)
                if k == "activeVerificationCert":
                    valid_data[k] = bool(v)
                if k == "primaryVerificationCert":
                    valid_data[k] = bool(v)
                if k == "secondaryVerificationCert":
                    valid_data[k] = bool(v)
                if k == "encryptionCert":
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
            if k in ["certView", "x509File", "activeVerificationCert", "primaryVerificationCert", "secondaryVerificationCert", "encryptionCert"]:
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
