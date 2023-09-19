from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.resource_link import ResourceLink


class SigningKeys(Model):
    """Setting for a OAuth/OpenID Connect signing key set while using multiple virtual issuers.

    Attributes
    ----------
    p256ActiveCertRef: ResourceLink
        Reference to the P-256 key currently active.

    p256PreviousCertRef: ResourceLink
        Reference to the P-256 key previously active.

    p256PublishX5cParameter: bool
        Enable publishing of the P-256 certificate chain associated with the active key.

    p384ActiveCertRef: ResourceLink
        Reference to the P-384 key currently active.

    p384PreviousCertRef: ResourceLink
        Reference to the P-384 key previously active.

    p384PublishX5cParameter: bool
        Enable publishing of the P-384 certificate chain associated with the active key.

    p521ActiveCertRef: ResourceLink
        Reference to the P-521 key currently active.

    p521PreviousCertRef: ResourceLink
        Reference to the P-521 key previously active.

    p521PublishX5cParameter: bool
        Enable publishing of the P-521 certificate chain associated with the active key.

    rsaActiveCertRef: ResourceLink
        Reference to the RSA key currently active.

    rsaPreviousCertRef: ResourceLink
        Reference to the RSA key previously active.

    rsaPublishX5cParameter: bool
        Enable publishing of the RSA certificate chain associated with the active key.

    """
    def __init__(self, p256ActiveCertRef: ResourceLink = None, p256PreviousCertRef: ResourceLink = None, p256PublishX5cParameter: bool = None, p384ActiveCertRef: ResourceLink = None, p384PreviousCertRef: ResourceLink = None, p384PublishX5cParameter: bool = None, p521ActiveCertRef: ResourceLink = None, p521PreviousCertRef: ResourceLink = None, p521PublishX5cParameter: bool = None, rsaActiveCertRef: ResourceLink = None, rsaPreviousCertRef: ResourceLink = None, rsaPublishX5cParameter: bool = None) -> None:
        self.p256ActiveCertRef = p256ActiveCertRef
        self.p256PreviousCertRef = p256PreviousCertRef
        self.p256PublishX5cParameter = p256PublishX5cParameter
        self.p384ActiveCertRef = p384ActiveCertRef
        self.p384PreviousCertRef = p384PreviousCertRef
        self.p384PublishX5cParameter = p384PublishX5cParameter
        self.p521ActiveCertRef = p521ActiveCertRef
        self.p521PreviousCertRef = p521PreviousCertRef
        self.p521PublishX5cParameter = p521PublishX5cParameter
        self.rsaActiveCertRef = rsaActiveCertRef
        self.rsaPreviousCertRef = rsaPreviousCertRef
        self.rsaPublishX5cParameter = rsaPublishX5cParameter

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SigningKeys):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.p256ActiveCertRef, self.p256PreviousCertRef, self.p256PublishX5cParameter, self.p384ActiveCertRef, self.p384PreviousCertRef, self.p384PublishX5cParameter, self.p521ActiveCertRef, self.p521PreviousCertRef, self.p521PublishX5cParameter, self.rsaActiveCertRef, self.rsaPreviousCertRef, self.rsaPublishX5cParameter]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["p256ActiveCertRef", "p256PreviousCertRef", "p256PublishX5cParameter", "p384ActiveCertRef", "p384PreviousCertRef", "p384PublishX5cParameter", "p521ActiveCertRef", "p521PreviousCertRef", "p521PublishX5cParameter", "rsaActiveCertRef", "rsaPreviousCertRef", "rsaPublishX5cParameter"] and v is not None:
                if k == "p256ActiveCertRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "p256PreviousCertRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "p256PublishX5cParameter":
                    valid_data[k] = bool(v)
                if k == "p384ActiveCertRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "p384PreviousCertRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "p384PublishX5cParameter":
                    valid_data[k] = bool(v)
                if k == "p521ActiveCertRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "p521PreviousCertRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "p521PublishX5cParameter":
                    valid_data[k] = bool(v)
                if k == "rsaActiveCertRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "rsaPreviousCertRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "rsaPublishX5cParameter":
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
            if k in ["p256ActiveCertRef", "p256PreviousCertRef", "p256PublishX5cParameter", "p384ActiveCertRef", "p384PreviousCertRef", "p384PublishX5cParameter", "p521ActiveCertRef", "p521PreviousCertRef", "p521PublishX5cParameter", "rsaActiveCertRef", "rsaPreviousCertRef", "rsaPublishX5cParameter"]:
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
