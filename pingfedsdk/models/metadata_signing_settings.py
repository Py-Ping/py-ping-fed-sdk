from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.resource_link import ResourceLink


class MetadataSigningSettings(Model):
    """Metadata signing settings. If metadata is not signed, this model will be empty.

    Attributes
    ----------
    signingKeyRef: ResourceLink
        Reference to the key used for metadata signing. Refer to /keyPair/signing to get the list of available signing key pairs.

    signatureAlgorithm: str
        Signature algorithm. If this property is unset, the default signature algorithm for the key algorithm will be used. Supported signature algorithms are available through the /keyPairs/keyAlgorithms endpoint.

    """
    def __init__(self, signingKeyRef: ResourceLink = None, signatureAlgorithm: str = None) -> None:
        self.signingKeyRef = signingKeyRef
        self.signatureAlgorithm = signatureAlgorithm

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, MetadataSigningSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.signingKeyRef, self.signatureAlgorithm]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["signingKeyRef", "signatureAlgorithm"] and v is not None:
                if k == "signingKeyRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "signatureAlgorithm":
                    valid_data[k] = str(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["signingKeyRef", "signatureAlgorithm"]:
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
