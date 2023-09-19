from enum import Enum

from pingfedsdk.model import Model


class EncryptionPolicy(Model):
    """Defines what to encrypt in the browser-based SSO profile.

    Attributes
    ----------
    encryptAssertion: bool
        Whether the outgoing SAML assertion will be encrypted.

    encryptedAttributes: list
        The list of outgoing SAML assertion attributes that will be encrypted. The 'encryptAssertion' property takes precedence over this.

    encryptSloSubjectNameId: bool
        Encrypt the name-identifier attribute in outbound SLO messages.  This can be set if the name id is encrypted.

    sloSubjectNameIDEncrypted: bool
        Allow the encryption of the name-identifier attribute for inbound SLO messages. This can be set if SP initiated SLO is enabled.

    """
    def __init__(self, encryptAssertion: bool = None, encryptedAttributes: list = None, encryptSloSubjectNameId: bool = None, sloSubjectNameIDEncrypted: bool = None) -> None:
        self.encryptAssertion = encryptAssertion
        self.encryptedAttributes = encryptedAttributes
        self.encryptSloSubjectNameId = encryptSloSubjectNameId
        self.sloSubjectNameIDEncrypted = sloSubjectNameIDEncrypted

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, EncryptionPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.encryptAssertion, self.encryptedAttributes, self.encryptSloSubjectNameId, self.sloSubjectNameIDEncrypted]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["encryptAssertion", "encryptedAttributes", "encryptSloSubjectNameId", "sloSubjectNameIDEncrypted"] and v is not None:
                if k == "encryptAssertion":
                    valid_data[k] = bool(v)
                if k == "encryptedAttributes":
                    valid_data[k] = [str(x) for x in v]
                if k == "encryptSloSubjectNameId":
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
            if k in ["encryptAssertion", "encryptedAttributes", "encryptSloSubjectNameId", "sloSubjectNameIDEncrypted"]:
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
