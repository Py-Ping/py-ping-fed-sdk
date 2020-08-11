class IdpAttributeQueryPolicy():
    """The attribute query profile's security policy.

    Attributes
    ----------
    encryptNameId : boolean
        Encrypt the name identifier.
    maskAttributeValues : boolean
        Mask attributes in log files.
    requireEncryptedAssertion : boolean
        Require encrypted assertion.
    requireSignedAssertion : boolean
        Require signed assertion.
    requireSignedResponse : boolean
        Require signed response.
    signAttributeQuery : boolean
        Sign the attribute query.

    """

    def __init__(self, encryptNameId:bool=None, maskAttributeValues:bool=None, requireEncryptedAssertion:bool=None, requireSignedAssertion:bool=None, requireSignedResponse:bool=None, signAttributeQuery:bool=None) -> None:
        self.encryptNameId = encryptNameId
        self.maskAttributeValues = maskAttributeValues
        self.requireEncryptedAssertion = requireEncryptedAssertion
        self.requireSignedAssertion = requireSignedAssertion
        self.requireSignedResponse = requireSignedResponse
        self.signAttributeQuery = signAttributeQuery

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpAttributeQueryPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.encryptNameId, self.maskAttributeValues, self.requireEncryptedAssertion, self.requireSignedAssertion, self.requireSignedResponse, self.signAttributeQuery]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["encryptNameId", "maskAttributeValues", "requireEncryptedAssertion", "requireSignedAssertion", "requireSignedResponse", "signAttributeQuery"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__