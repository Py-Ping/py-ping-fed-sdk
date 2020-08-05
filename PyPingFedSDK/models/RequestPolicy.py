class RequestPolicy():
    """ The set of attributes used to configure a CIBA request policy.

    Attributes
    ----------
    allowUnsignedLoginHintToken : boolean
        Allow unsigned login hint token.
    alternativeLoginHintTokenIssuers : array
        Alternative login hint token issuers.
    authenticatorRef : str
        Reference to the associated authenticator.
    id : string
        The request policy ID. ID is unique.
    identityHintContract : str
        Identity hint attribute contract.
    identityHintContractFulfillment : str
        Identity hint attribute contract fulfillment.
    identityHintMapping : str
        Identity hint contract to request policy mapping.
    name : string
        The request policy name. Name is unique.
    requireTokenForIdentityHint : boolean
        Require token for identity hint.
    transactionLifetime : integer
        The transaction lifetime in seconds.
    userCodePcvRef : str
        Reference to the associated password credential validator.

    """

    __slots__ = ["allowUnsignedLoginHintToken", "alternativeLoginHintTokenIssuers", "authenticatorRef", "id", "identityHintContract", "identityHintContractFulfillment", "identityHintMapping", "name", "requireTokenForIdentityHint", "transactionLifetime", "userCodePcvRef"]
    def __init__(self, id, name, authenticatorRef, identityHintContract, allowUnsignedLoginHintToken=None, alternativeLoginHintTokenIssuers=None, identityHintContractFulfillment=None, identityHintMapping=None, requireTokenForIdentityHint=None, transactionLifetime=None, userCodePcvRef=None):
            self.allowUnsignedLoginHintToken = allowUnsignedLoginHintToken
            self.alternativeLoginHintTokenIssuers = alternativeLoginHintTokenIssuers
            self.authenticatorRef = authenticatorRef
            self.id = id
            self.identityHintContract = identityHintContract
            self.identityHintContractFulfillment = identityHintContractFulfillment
            self.identityHintMapping = identityHintMapping
            self.name = name
            self.requireTokenForIdentityHint = requireTokenForIdentityHint
            self.transactionLifetime = transactionLifetime
            self.userCodePcvRef = userCodePcvRef
    
    def _validate(self):
        return any(x for x in ['id', 'name', 'authenticatorRef', 'identityHintContract'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, RequestPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((allowUnsignedLoginHintToken, alternativeLoginHintTokenIssuers, authenticatorRef, id, identityHintContract, identityHintContractFulfillment, identityHintMapping, name, requireTokenForIdentityHint, transactionLifetime, userCodePcvRef))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
