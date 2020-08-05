class SpAttributeQueryPolicy():
    """ The attribute query profile's security policy.

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

    __slots__ = ["encryptAssertion", "requireEncryptedNameId", "requireSignedAttributeQuery", "signAssertion", "signResponse"]
    def __init__(self, encryptAssertion=None, requireEncryptedNameId=None, requireSignedAttributeQuery=None, signAssertion=None, signResponse=None):
            self.encryptAssertion = encryptAssertion
            self.requireEncryptedNameId = requireEncryptedNameId
            self.requireSignedAttributeQuery = requireSignedAttributeQuery
            self.signAssertion = signAssertion
            self.signResponse = signResponse
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, SpAttributeQueryPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((encryptAssertion, requireEncryptedNameId, requireSignedAttributeQuery, signAssertion, signResponse))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
