class EncryptionPolicy():
    """Defines what to encrypt in the browser-based SSO profile.

    Attributes
    ----------
    encryptAssertion : boolean
 Whether the outgoing SAML assertion will be encrypted.
    encryptSloSubjectNameId : boolean
 Encrypt the name-identifier attribute in outbound SLO messages.  This can be set if the name id is encrypted.
    encryptedAttributes : array
 The list of outgoing SAML assertion attributes that will be encrypted. The 'encryptAssertion' property takes precedence over this.
    sloSubjectNameIDEncrypted : boolean
 Allow the encryption of the name-identifier attribute for inbound SLO messages. This can be set if SP initiated SLO is enabled.

    """

<<<<<<< HEAD
    def __init__(self, encryptAssertion=None, encryptSloSubjectNameId=None, encryptedAttributes=None, sloSubjectNameIDEncrypted=None) -> None:
        self.encryptAssertion = encryptAssertion
        self.encryptSloSubjectNameId = encryptSloSubjectNameId
        self.encryptedAttributes = encryptedAttributes
        self.sloSubjectNameIDEncrypted = sloSubjectNameIDEncrypted
=======
    def __init__(self, encryptAssertion=None, encryptSloSubjectNameId=None, encryptedAttributes=None, sloSubjectNameIDEncrypted=None):
        self.encryptAssertion: bool = encryptAssertion
        self.encryptSloSubjectNameId: bool = encryptSloSubjectNameId
        self.encryptedAttributes: list = encryptedAttributes
        self.sloSubjectNameIDEncrypted: bool = sloSubjectNameIDEncrypted
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, EncryptionPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.encryptAssertion, self.encryptSloSubjectNameId, self.encryptedAttributes, self.sloSubjectNameIDEncrypted))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["encryptAssertion", "encryptSloSubjectNameId", "encryptedAttributes", "sloSubjectNameIDEncrypted"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
