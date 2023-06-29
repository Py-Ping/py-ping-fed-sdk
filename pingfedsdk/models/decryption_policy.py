from pingfedsdk.model import Model
from enum import Enum


class DecryptionPolicy(Model):
    """Defines what to decrypt in the browser-based SSO profile.

    Attributes
    ----------
    assertionEncrypted: bool
        Specify whether the incoming SAML assertion is encrypted for an IdP connection.

    attributesEncrypted: bool
        Specify whether one or more incoming SAML attributes are encrypted for an IdP connection.

    subjectNameIdEncrypted: bool
        Specify whether the incoming Subject Name ID is encrypted for an IdP connection.

    sloEncryptSubjectNameID: bool
        Encrypt the Subject Name ID in SLO messages to the IdP.

    sloSubjectNameIDEncrypted: bool
        Allow encrypted Subject Name ID in SLO messages from the IdP.

    """

    def __init__(self, assertionEncrypted: bool = None, attributesEncrypted: bool = None, subjectNameIdEncrypted: bool = None, sloEncryptSubjectNameID: bool = None, sloSubjectNameIDEncrypted: bool = None) -> None:
        self.assertionEncrypted = assertionEncrypted
        self.attributesEncrypted = attributesEncrypted
        self.subjectNameIdEncrypted = subjectNameIdEncrypted
        self.sloEncryptSubjectNameID = sloEncryptSubjectNameID
        self.sloSubjectNameIDEncrypted = sloSubjectNameIDEncrypted

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, DecryptionPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.assertionEncrypted, self.attributesEncrypted, self.subjectNameIdEncrypted, self.sloEncryptSubjectNameID, self.sloSubjectNameIDEncrypted]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["assertionEncrypted", "attributesEncrypted", "subjectNameIdEncrypted", "sloEncryptSubjectNameID", "sloSubjectNameIDEncrypted"] and v is not None:
                if k == "assertionEncrypted":
                    valid_data[k] = bool(v)
                if k == "attributesEncrypted":
                    valid_data[k] = bool(v)
                if k == "subjectNameIdEncrypted":
                    valid_data[k] = bool(v)
                if k == "sloEncryptSubjectNameID":
                    valid_data[k] = bool(v)
                if k == "sloSubjectNameIDEncrypted":
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
            if k in ["assertionEncrypted", "attributesEncrypted", "subjectNameIdEncrypted", "sloEncryptSubjectNameID", "sloSubjectNameIDEncrypted"]:
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
