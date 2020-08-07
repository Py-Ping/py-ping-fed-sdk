class IdpAttributeQueryPolicy():
    """The attribute query profile's security policy.

    Attributes
    ----------
    encryptNameId : boolean
        Encrypt the name identifier.    maskAttributeValues : boolean
        Mask attributes in log files.    requireEncryptedAssertion : boolean
        Require encrypted assertion.    requireSignedAssertion : boolean
        Require signed assertion.    requireSignedResponse : boolean
        Require signed response.    signAttributeQuery : boolean
        Sign the attribute query.
    """

    __slots__ = ["encryptNameId", "maskAttributeValues", "requireEncryptedAssertion", "requireSignedAssertion", "requireSignedResponse", "signAttributeQuery"]

    def __init__(self, encryptNameId=None, maskAttributeValues=None, requireEncryptedAssertion=None, requireSignedAssertion=None, requireSignedResponse=None, signAttributeQuery=None):
        self.encryptNameId: bool = encryptNameId
        self.maskAttributeValues: bool = maskAttributeValues
        self.requireEncryptedAssertion: bool = requireEncryptedAssertion
        self.requireSignedAssertion: bool = requireSignedAssertion
        self.requireSignedResponse: bool = requireSignedResponse
        self.signAttributeQuery: bool = signAttributeQuery

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, IdpAttributeQueryPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.encryptNameId, self.maskAttributeValues, self.requireEncryptedAssertion, self.requireSignedAssertion, self.requireSignedResponse, self.signAttributeQuery))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["encryptNameId", "maskAttributeValues", "requireEncryptedAssertion", "requireSignedAssertion", "requireSignedResponse", "signAttributeQuery"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__