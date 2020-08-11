class RequestPolicy():
    """The set of attributes used to configure a CIBA request policy.

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

    def __init__(self, var_id:str, name:str, authenticatorRef, identityHintContract, allowUnsignedLoginHintToken:bool=None, alternativeLoginHintTokenIssuers:list=None, identityHintContractFulfillment=None, identityHintMapping=None, requireTokenForIdentityHint:bool=None, transactionLifetime:int=None, userCodePcvRef=None) -> None:
        self.allowUnsignedLoginHintToken = allowUnsignedLoginHintToken
        self.alternativeLoginHintTokenIssuers = alternativeLoginHintTokenIssuers
        self.authenticatorRef = authenticatorRef
        self.var_id = var_id
        self.identityHintContract = identityHintContract
        self.identityHintContractFulfillment = identityHintContractFulfillment
        self.identityHintMapping = identityHintMapping
        self.name = name
        self.requireTokenForIdentityHint = requireTokenForIdentityHint
        self.transactionLifetime = transactionLifetime
        self.userCodePcvRef = userCodePcvRef

    def _validate(self) -> bool:
        return any(x for x in ["var_id", "name", "authenticatorRef", "identityHintContract"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, RequestPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.allowUnsignedLoginHintToken, self.alternativeLoginHintTokenIssuers, self.authenticatorRef, self.var_id, self.identityHintContract, self.identityHintContractFulfillment, self.identityHintMapping, self.name, self.requireTokenForIdentityHint, self.transactionLifetime, self.userCodePcvRef]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["allowUnsignedLoginHintToken", "alternativeLoginHintTokenIssuers", "authenticatorRef", "var_id", "identityHintContract", "identityHintContractFulfillment", "identityHintMapping", "name", "requireTokenForIdentityHint", "transactionLifetime", "userCodePcvRef"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__