from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.o_i_d_c_request_parameter import OIDCRequestParameter
from pingfedsdk.enums import AuthenticationScheme
from pingfedsdk.enums import SigningAlgorithm
from pingfedsdk.enums import LoginType


class OIDCProviderSettings(Model):
    """The OpenID Provider settings.

    Attributes
    ----------
    scopes: str
        Space separated scope values that the OpenID Provider supports.

    authorizationEndpoint: str
        URL of the OpenID Provider's OAuth 2.0 Authorization Endpoint.

    loginType: LoginType
        The OpenID Connect login type. These values maps to:
          CODE: Authentication using Code Flow
         POST: Authentication using Form Post
         POST_AT: Authentication using Form Post with Access Token

    authenticationScheme: AuthenticationScheme
        The OpenID Connect Authentication Scheme. This is required for Authentication using Code Flow.

    authenticationSigningAlgorithm: SigningAlgorithm
        The authentication signing algorithm for token endpoint PRIVATE_KEY_JWT authentication. Only asymmetric algorithms are allowed. For RSASSA-PSS signing algorithm, PingFederate must be integrated with a hardware security module (HSM) or Java 11.

    requestSigningAlgorithm: SigningAlgorithm
        The request signing algorithm. Required only if you wish to use signed requests. Only asymmetric algorithms are allowed. For RSASSA-PSS signing algorithm, PingFederate must be integrated with a hardware security module (HSM) or Java 11.

    enablePKCE: bool
        Enable Proof Key for Code Exchange (PKCE). When enabled, the client sends an SHA-256 code challenge and corresponding code verifier to the OpenID Provider during the authorization code flow.

    tokenEndpoint: str
        URL of the OpenID Provider's OAuth 2.0 Token Endpoint.

    userInfoEndpoint: str
        URL of the OpenID Provider's UserInfo Endpoint.

    jwksURL: str
        URL of the OpenID Provider's JSON Web Key Set [JWK] document.

    requestParameters: list
        A list of request parameters. Request parameters with same name but different attribute values are treated as a multi-valued request parameter.

    """

    def __init__(self, authorizationEndpoint: str, jwksURL: str, loginType: LoginType, scopes: str, authenticationScheme: AuthenticationScheme = None, authenticationSigningAlgorithm: SigningAlgorithm = None, requestSigningAlgorithm: SigningAlgorithm = None, enablePKCE: bool = None, tokenEndpoint: str = None, userInfoEndpoint: str = None, requestParameters: list = None) -> None:
        self.scopes = scopes
        self.authorizationEndpoint = authorizationEndpoint
        self.loginType = loginType
        self.authenticationScheme = authenticationScheme
        self.authenticationSigningAlgorithm = authenticationSigningAlgorithm
        self.requestSigningAlgorithm = requestSigningAlgorithm
        self.enablePKCE = enablePKCE
        self.tokenEndpoint = tokenEndpoint
        self.userInfoEndpoint = userInfoEndpoint
        self.jwksURL = jwksURL
        self.requestParameters = requestParameters

    def _validate(self) -> bool:
        return any(x for x in ["authorizationEndpoint", "jwksURL", "loginType", "scopes"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OIDCProviderSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.scopes, self.authorizationEndpoint, self.loginType, self.authenticationScheme, self.authenticationSigningAlgorithm, self.requestSigningAlgorithm, self.enablePKCE, self.tokenEndpoint, self.userInfoEndpoint, self.jwksURL, self.requestParameters]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["scopes", "authorizationEndpoint", "loginType", "authenticationScheme", "authenticationSigningAlgorithm", "requestSigningAlgorithm", "enablePKCE", "tokenEndpoint", "userInfoEndpoint", "jwksURL", "requestParameters"] and v is not None:
                if k == "scopes":
                    valid_data[k] = str(v)
                if k == "authorizationEndpoint":
                    valid_data[k] = str(v)
                if k == "loginType":
                    valid_data[k] = LoginType[v]
                if k == "authenticationScheme":
                    valid_data[k] = AuthenticationScheme[v]
                if k == "authenticationSigningAlgorithm":
                    valid_data[k] = SigningAlgorithm[v]
                if k == "requestSigningAlgorithm":
                    valid_data[k] = SigningAlgorithm[v]
                if k == "enablePKCE":
                    valid_data[k] = bool(v)
                if k == "tokenEndpoint":
                    valid_data[k] = str(v)
                if k == "userInfoEndpoint":
                    valid_data[k] = str(v)
                if k == "jwksURL":
                    valid_data[k] = str(v)
                if k == "requestParameters":
                    valid_data[k] = [OIDCRequestParameter(**x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["scopes", "authorizationEndpoint", "loginType", "authenticationScheme", "authenticationSigningAlgorithm", "requestSigningAlgorithm", "enablePKCE", "tokenEndpoint", "userInfoEndpoint", "jwksURL", "requestParameters"]:
                if isinstance(v, Model):
                    body[k] = v.to_dict(remove_nonetypes)
                elif isinstance(v, list):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, dict):
                    vals = {}
                    for x, y in v.items():
                        if isinstance(y, Model):
                            vals[x] = y.to_dict(remove_nonetypes)
                        elif not remove_nonetypes or (remove_nonetypes and y is not None):
                            vals[x] = y
                    body[k] = vals
                elif isinstance(v, set):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, Enum):
                    body[k] = str(v).split('.')[-1]
                elif not remove_nonetypes or (remove_nonetypes and v is not None):
                    body[k] = v
        return body
