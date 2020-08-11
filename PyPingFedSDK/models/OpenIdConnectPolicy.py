class OpenIdConnectPolicy():
    """The set of attributes used to configure an OpenID Connect policy.

    Attributes
    ----------
    accessTokenManagerRef : str
        The access token manager associated with this Open ID Connect policy.
    attributeContract : str
        The list of attributes that will be returned to OAuth clients in response to requests received at the PingFederate UserInfo endpoint.
    attributeMapping : str
        The attributes mapping from attribute sources to attribute targets.
    id : string
        The policy ID used internally.
    idTokenLifetime : integer
        The ID Token Lifetime, in minutes. The default value is 5.
    includeSHashInIdToken : boolean
        Determines whether the State Hash should be included in the ID token.
    includeSriInIdToken : boolean
        Determines whether a Session Reference Identifier is included in the ID token.
    includeUserInfoInIdToken : boolean
        Determines whether the User Info is always included in the ID token.
    name : string
        The name used for display in UI screens.
    returnIdTokenOnRefreshGrant : boolean
        Determines whether an ID Token should be returned when refresh grant is requested or not.
    scopeAttributeMappings : str
        The attribute scope mappings from scopes to attribute names.

    """

    def __init__(self, var_id:str, name:str, accessTokenManagerRef, attributeContract, attributeMapping, idTokenLifetime:int=None, includeSHashInIdToken:bool=None, includeSriInIdToken:bool=None, includeUserInfoInIdToken:bool=None, returnIdTokenOnRefreshGrant:bool=None, scopeAttributeMappings=None) -> None:
        self.accessTokenManagerRef = accessTokenManagerRef
        self.attributeContract = attributeContract
        self.attributeMapping = attributeMapping
        self.var_id = var_id
        self.idTokenLifetime = idTokenLifetime
        self.includeSHashInIdToken = includeSHashInIdToken
        self.includeSriInIdToken = includeSriInIdToken
        self.includeUserInfoInIdToken = includeUserInfoInIdToken
        self.name = name
        self.returnIdTokenOnRefreshGrant = returnIdTokenOnRefreshGrant
        self.scopeAttributeMappings = scopeAttributeMappings

    def _validate(self) -> bool:
        return any(x for x in ["var_id", "name", "accessTokenManagerRef", "attributeContract", "attributeMapping"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, OpenIdConnectPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.accessTokenManagerRef, self.attributeContract, self.attributeMapping, self.var_id, self.idTokenLifetime, self.includeSHashInIdToken, self.includeSriInIdToken, self.includeUserInfoInIdToken, self.name, self.returnIdTokenOnRefreshGrant, self.scopeAttributeMappings))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["accessTokenManagerRef", "attributeContract", "attributeMapping", "var_id", "idTokenLifetime", "includeSHashInIdToken", "includeSriInIdToken", "includeUserInfoInIdToken", "name", "returnIdTokenOnRefreshGrant", "scopeAttributeMappings"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__