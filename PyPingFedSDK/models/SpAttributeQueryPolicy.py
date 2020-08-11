class SpAttributeQueryPolicy():
    """The attribute query profile's security policy.

    Attributes
    ----------
    encryptAssertion : boolean
 Encrypt the assertion.
    requireEncryptedNameId : boolean
 Require an encrypted name identifier.
    requireSignedAttributeQuery : boolean
 Require signed attribute query.
    signAssertion : boolean
 Sign the assertion.
    signResponse : boolean
 Sign the response.

    """

    def __init__(self, encryptAssertion:bool=None, requireEncryptedNameId:bool=None, requireSignedAttributeQuery:bool=None, signAssertion:bool=None, signResponse:bool=None) -> None:
        self.encryptAssertion = encryptAssertion
        self.requireEncryptedNameId = requireEncryptedNameId
        self.requireSignedAttributeQuery = requireSignedAttributeQuery
        self.signAssertion = signAssertion
        self.signResponse = signResponse

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SpAttributeQueryPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.encryptAssertion, self.requireEncryptedNameId, self.requireSignedAttributeQuery, self.signAssertion, self.signResponse))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["encryptAssertion", "requireEncryptedNameId", "requireSignedAttributeQuery", "signAssertion", "signResponse"]}

        return cls(**valid_data)