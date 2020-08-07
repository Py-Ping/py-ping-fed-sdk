class DecryptionPolicy():
    """Defines what to decrypt in the browser-based SSO profile.

    Attributes
    ----------
    assertionEncrypted : boolean
 Specify whether the incoming SAML assertion is encrypted for an IdP connection.
    attributesEncrypted : boolean
 Specify whether one or more incoming SAML attributes are encrypted for an IdP connection.
    sloEncryptSubjectNameID : boolean
 Encrypt the Subject Name ID in SLO messages to the IdP.
    sloSubjectNameIDEncrypted : boolean
 Allow encrypted Subject Name ID in SLO messages from the IdP.
    subjectNameIdEncrypted : boolean
 Specify whether the incoming Subject Name ID is encrypted for an IdP connection.

    """

<<<<<<< HEAD
    def __init__(self, assertionEncrypted=None, attributesEncrypted=None, sloEncryptSubjectNameID=None, sloSubjectNameIDEncrypted=None, subjectNameIdEncrypted=None) -> None:
        self.assertionEncrypted = assertionEncrypted
        self.attributesEncrypted = attributesEncrypted
        self.sloEncryptSubjectNameID = sloEncryptSubjectNameID
        self.sloSubjectNameIDEncrypted = sloSubjectNameIDEncrypted
        self.subjectNameIdEncrypted = subjectNameIdEncrypted
=======
    def __init__(self, assertionEncrypted=None, attributesEncrypted=None, sloEncryptSubjectNameID=None, sloSubjectNameIDEncrypted=None, subjectNameIdEncrypted=None):
        self.assertionEncrypted: bool = assertionEncrypted
        self.attributesEncrypted: bool = attributesEncrypted
        self.sloEncryptSubjectNameID: bool = sloEncryptSubjectNameID
        self.sloSubjectNameIDEncrypted: bool = sloSubjectNameIDEncrypted
        self.subjectNameIdEncrypted: bool = subjectNameIdEncrypted
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, DecryptionPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.assertionEncrypted, self.attributesEncrypted, self.sloEncryptSubjectNameID, self.sloSubjectNameIDEncrypted, self.subjectNameIdEncrypted))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["assertionEncrypted", "attributesEncrypted", "sloEncryptSubjectNameID", "sloSubjectNameIDEncrypted", "subjectNameIdEncrypted"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
