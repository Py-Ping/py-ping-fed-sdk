from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.resource_link import ResourceLink


class OAuthOidcKeysSettings(Model):
    """Setting for OAuth/OpenID Connect signing and decryption key settings.

    Attributes
    ----------
    staticJwksEnabled: bool
        Enable static keys.

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

    p256DecryptionActiveCertRef: ResourceLink
        Reference to the P-256 decryption key currently active.

    p256DecryptionPreviousCertRef: ResourceLink
        Reference to the P-256 decryption key previously active.

    p256DecryptionPublishX5cParameter: bool
        Enable publishing of the P-256 certificate chain associated with the active key.

    p384DecryptionActiveCertRef: ResourceLink
        Reference to the P-384 decryption key currently active.

    p384DecryptionPreviousCertRef: ResourceLink
        Reference to the P-384 decryption key previously active.

    p384DecryptionPublishX5cParameter: bool
        Enable publishing of the P-384 certificate chain associated with the active key.

    p521DecryptionActiveCertRef: ResourceLink
        Reference to the P-521 decryption key currently active.

    p521DecryptionPreviousCertRef: ResourceLink
        Reference to the P-521 decryption key previously active.

    p521DecryptionPublishX5cParameter: bool
        Enable publishing of the P-521 certificate chain associated with the active key.

    rsaDecryptionActiveCertRef: ResourceLink
        Reference to the RSA decryption key currently active.

    rsaDecryptionPreviousCertRef: ResourceLink
        Reference to the RSA decryption key previously active.

    rsaDecryptionPublishX5cParameter: bool
        Enable publishing of the RSA certificate chain associated with the active key.

    """
    def __init__(self, staticJwksEnabled: bool, p256ActiveCertRef: ResourceLink = None, p256PreviousCertRef: ResourceLink = None, p256PublishX5cParameter: bool = None, p384ActiveCertRef: ResourceLink = None, p384PreviousCertRef: ResourceLink = None, p384PublishX5cParameter: bool = None, p521ActiveCertRef: ResourceLink = None, p521PreviousCertRef: ResourceLink = None, p521PublishX5cParameter: bool = None, rsaActiveCertRef: ResourceLink = None, rsaPreviousCertRef: ResourceLink = None, rsaPublishX5cParameter: bool = None, p256DecryptionActiveCertRef: ResourceLink = None, p256DecryptionPreviousCertRef: ResourceLink = None, p256DecryptionPublishX5cParameter: bool = None, p384DecryptionActiveCertRef: ResourceLink = None, p384DecryptionPreviousCertRef: ResourceLink = None, p384DecryptionPublishX5cParameter: bool = None, p521DecryptionActiveCertRef: ResourceLink = None, p521DecryptionPreviousCertRef: ResourceLink = None, p521DecryptionPublishX5cParameter: bool = None, rsaDecryptionActiveCertRef: ResourceLink = None, rsaDecryptionPreviousCertRef: ResourceLink = None, rsaDecryptionPublishX5cParameter: bool = None) -> None:
        self.staticJwksEnabled = staticJwksEnabled
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
        self.p256DecryptionActiveCertRef = p256DecryptionActiveCertRef
        self.p256DecryptionPreviousCertRef = p256DecryptionPreviousCertRef
        self.p256DecryptionPublishX5cParameter = p256DecryptionPublishX5cParameter
        self.p384DecryptionActiveCertRef = p384DecryptionActiveCertRef
        self.p384DecryptionPreviousCertRef = p384DecryptionPreviousCertRef
        self.p384DecryptionPublishX5cParameter = p384DecryptionPublishX5cParameter
        self.p521DecryptionActiveCertRef = p521DecryptionActiveCertRef
        self.p521DecryptionPreviousCertRef = p521DecryptionPreviousCertRef
        self.p521DecryptionPublishX5cParameter = p521DecryptionPublishX5cParameter
        self.rsaDecryptionActiveCertRef = rsaDecryptionActiveCertRef
        self.rsaDecryptionPreviousCertRef = rsaDecryptionPreviousCertRef
        self.rsaDecryptionPublishX5cParameter = rsaDecryptionPublishX5cParameter

    def _validate(self) -> bool:
        return any(x for x in ["staticJwksEnabled"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OAuthOidcKeysSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.staticJwksEnabled, self.p256ActiveCertRef, self.p256PreviousCertRef, self.p256PublishX5cParameter, self.p384ActiveCertRef, self.p384PreviousCertRef, self.p384PublishX5cParameter, self.p521ActiveCertRef, self.p521PreviousCertRef, self.p521PublishX5cParameter, self.rsaActiveCertRef, self.rsaPreviousCertRef, self.rsaPublishX5cParameter, self.p256DecryptionActiveCertRef, self.p256DecryptionPreviousCertRef, self.p256DecryptionPublishX5cParameter, self.p384DecryptionActiveCertRef, self.p384DecryptionPreviousCertRef, self.p384DecryptionPublishX5cParameter, self.p521DecryptionActiveCertRef, self.p521DecryptionPreviousCertRef, self.p521DecryptionPublishX5cParameter, self.rsaDecryptionActiveCertRef, self.rsaDecryptionPreviousCertRef, self.rsaDecryptionPublishX5cParameter]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["staticJwksEnabled", "p256ActiveCertRef", "p256PreviousCertRef", "p256PublishX5cParameter", "p384ActiveCertRef", "p384PreviousCertRef", "p384PublishX5cParameter", "p521ActiveCertRef", "p521PreviousCertRef", "p521PublishX5cParameter", "rsaActiveCertRef", "rsaPreviousCertRef", "rsaPublishX5cParameter", "p256DecryptionActiveCertRef", "p256DecryptionPreviousCertRef", "p256DecryptionPublishX5cParameter", "p384DecryptionActiveCertRef", "p384DecryptionPreviousCertRef", "p384DecryptionPublishX5cParameter", "p521DecryptionActiveCertRef", "p521DecryptionPreviousCertRef", "p521DecryptionPublishX5cParameter", "rsaDecryptionActiveCertRef", "rsaDecryptionPreviousCertRef", "rsaDecryptionPublishX5cParameter"] and v is not None:
                if k == "staticJwksEnabled":
                    valid_data[k] = bool(v)
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
                if k == "p256DecryptionActiveCertRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "p256DecryptionPreviousCertRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "p256DecryptionPublishX5cParameter":
                    valid_data[k] = bool(v)
                if k == "p384DecryptionActiveCertRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "p384DecryptionPreviousCertRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "p384DecryptionPublishX5cParameter":
                    valid_data[k] = bool(v)
                if k == "p521DecryptionActiveCertRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "p521DecryptionPreviousCertRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "p521DecryptionPublishX5cParameter":
                    valid_data[k] = bool(v)
                if k == "rsaDecryptionActiveCertRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "rsaDecryptionPreviousCertRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "rsaDecryptionPublishX5cParameter":
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
            if k in ["staticJwksEnabled", "p256ActiveCertRef", "p256PreviousCertRef", "p256PublishX5cParameter", "p384ActiveCertRef", "p384PreviousCertRef", "p384PublishX5cParameter", "p521ActiveCertRef", "p521PreviousCertRef", "p521PublishX5cParameter", "rsaActiveCertRef", "rsaPreviousCertRef", "rsaPublishX5cParameter", "p256DecryptionActiveCertRef", "p256DecryptionPreviousCertRef", "p256DecryptionPublishX5cParameter", "p384DecryptionActiveCertRef", "p384DecryptionPreviousCertRef", "p384DecryptionPublishX5cParameter", "p521DecryptionActiveCertRef", "p521DecryptionPreviousCertRef", "p521DecryptionPublishX5cParameter", "rsaDecryptionActiveCertRef", "rsaDecryptionPreviousCertRef", "rsaDecryptionPublishX5cParameter"]:
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
