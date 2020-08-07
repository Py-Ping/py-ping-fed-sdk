class OIDCProviderSettings():
    """The OpenID Provider settings.

    Attributes
    ----------
    authenticationScheme : str
 The OpenID Connect Authentication Scheme. This is required for Authentication using Code Flow.
    authenticationSigningAlgorithm : str
 The authentication signing algorithm for token endpoint PRIVATE_KEY_JWT authentication. Only asymmetric algorithms are allowed. For RSASSA-PSS signing algorithm, PingFederate must be integrated with a hardware security module (HSM) or Java 11.
    authorizationEndpoint : string
 URL of the OpenID Provider's OAuth 2.0 Authorization Endpoint.
    jwksURL : string
 URL of the OpenID Provider's JSON Web Key Set [JWK] document.
    loginType : str
 The OpenID Connect login type. These values maps to: <br>  CODE: Authentication using Code Flow <br> POST: Authentication using Form Post <br> POST_AT: Authentication using Form Post with Access Token
    requestParameters : array
 A map of request parameter names and values.
    requestSigningAlgorithm : str
 The request signing algorithm. Required only if you wish to use signed requests. Only asymmetric algorithms are allowed. For RSASSA-PSS signing algorithm, PingFederate must be integrated with a hardware security module (HSM) or Java 11.
    scopes : string
 Space separated scope values that the OpenID Provider supports.
    tokenEndpoint : string
 URL of the OpenID Provider's OAuth 2.0 Token Endpoint.
    userInfoEndpoint : string
 URL of the OpenID Provider's UserInfo Endpoint.

    """

    def __init__(self, scopes, authorizationEndpoint, loginType, jwksURL, authenticationScheme=None, authenticationSigningAlgorithm=None, requestParameters=None, requestSigningAlgorithm=None, tokenEndpoint=None, userInfoEndpoint=None) -> None:
        self.authenticationScheme = authenticationScheme
        self.authenticationSigningAlgorithm = authenticationSigningAlgorithm
        self.authorizationEndpoint = authorizationEndpoint
        self.jwksURL = jwksURL
        self.loginType = loginType
        self.requestParameters = requestParameters
        self.requestSigningAlgorithm = requestSigningAlgorithm
        self.scopes = scopes
        self.tokenEndpoint = tokenEndpoint
        self.userInfoEndpoint = userInfoEndpoint

    def _validate(self) -> bool:
        return any(x for x in ["scopes", "authorizationEndpoint", "loginType", "jwksURL"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, OIDCProviderSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.authenticationScheme, self.authenticationSigningAlgorithm, self.authorizationEndpoint, self.jwksURL, self.loginType, self.requestParameters, self.requestSigningAlgorithm, self.scopes, self.tokenEndpoint, self.userInfoEndpoint))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["authenticationScheme", "authenticationSigningAlgorithm", "authorizationEndpoint", "jwksURL", "loginType", "requestParameters", "requestSigningAlgorithm", "scopes", "tokenEndpoint", "userInfoEndpoint"]}

        return cls(**valid_data)