from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.x_5_0_9_file import X509File
from pingfedsdk.models.cert_view import CertView


class MetadataUrl(Model):
    """Metadata URL and corresponding Signature Verification Certificate.

    Attributes
    ----------
    id: str
        The persistent, unique ID for the Metadata Url. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified.

    name: str
        The name for the Metadata URL.

    url: str
        The Metadata URL.

    certView: CertView
        The Signature Verification Certificate details. This property is read-only and is always ignored on a POST or PUT.

    x509File: X509File
        Data of the Signature Verification Certificate for the Metadata URL.

    validateSignature: bool
        Perform Metadata Signature Validation. The default value is TRUE.

    """

    def __init__(self, name: str, url: str, id: str = None, certView: CertView = None, x509File: X509File = None, validateSignature: bool = None) -> None:
        self.id = id
        self.name = name
        self.url = url
        self.certView = certView
        self.x509File = x509File
        self.validateSignature = validateSignature

    def _validate(self) -> bool:
        return any(x for x in ["name", "url"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, MetadataUrl):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.name, self.url, self.certView, self.x509File, self.validateSignature]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "name", "url", "certView", "x509File", "validateSignature"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "url":
                    valid_data[k] = str(v)
                if k == "certView":
                    valid_data[k] = CertView(**v)
                if k == "x509File":
                    valid_data[k] = X509File(**v)
                if k == "validateSignature":
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
            if k in ["id", "name", "url", "certView", "x509File", "validateSignature"]:
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
