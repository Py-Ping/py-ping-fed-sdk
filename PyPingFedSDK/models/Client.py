class Client():
    """OAuth client.

    Attributes
    ----------
    bypassActivationCodeConfirmationOverride : boolean
 Indicates if the Activation Code Confirmation page should be bypassed if 'verification_url_complete' is used by the end user to authorize a device. This overrides the 'bypassUseCodeConfirmation' value present in Authorization Server Settings.
    bypassApprovalPage : boolean
 Use this setting, for example, when you want to deploy a trusted application and authenticate end users via an IdP adapter or IdP connection.
    cibaDeliveryMode : str
 The token delivery mode for the client.  The default value is 'POLL'.
    cibaNotificationEndpoint : string
 The endpoint the OP will call after a successful or failed end-user authentication.
    cibaPollingInterval : integer
 The minimum amount of time in seconds that the Client must wait between polling requests to the token endpoint. The default is 3 seconds.
    cibaRequestObjectSigningAlgorithm : str
 The JSON Web Signature [JWS] algorithm that must be used to sign the CIBA Request Object. All signing algorithms are allowed if value is not present <br>RS256 - RSA using SHA-256<br>RS384 - RSA using SHA-384<br>RS512 - RSA using SHA-512<br>ES256 - ECDSA using P256 Curve and SHA-256<br>ES384 - ECDSA using P384 Curve and SHA-384<br>ES512 - ECDSA using P521 Curve and SHA-512<br>PS256 - RSASSA-PSS using SHA-256 and MGF1 padding with SHA-256<br>PS384 - RSASSA-PSS using SHA-384 and MGF1 padding with SHA-384<br>PS512 - RSASSA-PSS using SHA-512 and MGF1 padding with SHA-512<br>RSASSA-PSS is only supported with SafeNet Luna, Thales nCipher or Java 11.
    cibaRequireSignedRequests : boolean
 Determines whether CIBA signed requests are required for this client.
    cibaUserCodeSupported : boolean
 Determines whether CIBA user code is supported for this client.
    clientAuth : str
 Client authentication settings.  If this model is null, it indicates that no client authentication will be used.
    clientId : string
 A unique identifier the client provides to the Resource Server to identify itself. This identifier is included with every request the client makes. For PUT requests, this field is optional and it will be overridden by the 'id' parameter of the PUT request.
    defaultAccessTokenManagerRef : str
 The default access token manager for this client.
    description : string
 A description of what the client application does. This description appears when the user is prompted for authorization.
    deviceFlowSettingType : str
 Allows an administrator to override the Device Authorization Settings set globally for the OAuth AS. Defaults to SERVER_DEFAULT.
    devicePollingIntervalOverride : integer
 The amount of time client should wait between polling requests, in seconds. This overrides the 'devicePollingInterval' value present in Authorization Server Settings.
    enabled : boolean
 Specifies whether the client is enabled. The default value is true.
    exclusiveScopes : str
 The exclusive scopes available for this client.
    extendedParameters : str
 OAuth Client Metadata can be extended to use custom Client Metadata Parameters. The names of these custom parameters should be defined in /extendedProperties.
    grantTypes : str
 The grant types allowed for this client. The EXTENSION grant type applies to SAML/JWT assertion grants.
    jwksSettings : str
 JSON Web Key Set Settings of the OAuth client. Required if private key JWT client authentication or signed requests is enabled.
    logoUrl : string
 The location of the logo used on user-facing OAuth grant authorization and revocation pages.
    name : string
 A descriptive name for the client instance. This name appears when the user is prompted for authorization.
    oidcPolicy : str
 Open ID Connect Policy settings.  This is included in the message only when OIDC is enabled.
    pendingAuthorizationTimeoutOverride : integer
 The 'device_code' and 'user_code' timeout, in seconds. This overrides the 'pendingAuthorizationTimeout' value present in Authorization Server Settings.
    persistentGrantExpirationTime : integer
 The persistent grant expiration time. -1 indicates an indefinite amount of time.
    persistentGrantExpirationTimeUnit : str
 The persistent grant expiration time unit.
    persistentGrantExpirationType : str
 Allows an administrator to override the Persistent Grant Lifetime set globally for the OAuth AS. Defaults to SERVER_DEFAULT.
    persistentGrantIdleTimeout : integer
 The persistent grant idle timeout.
    persistentGrantIdleTimeoutTimeUnit : str
 The persistent grant idle timeout time unit.
    persistentGrantIdleTimeoutType : str
 Allows an administrator to override the Persistent Grant Idle Timeout set globally for the OAuth AS. Defaults to SERVER_DEFAULT.
    redirectUris : array
 URIs to which the OAuth AS may redirect the resource owner's user agent after authorization is obtained. A redirection URI is used with the Authorization Code and Implicit grant types. Wildcards are allowed. However, for security reasons, make the URL as restrictive as possible.For example: https://*.company.com/* Important: If more than one URI is added or if a single URI uses wildcards, then Authorization Code grant and token requests must contain a specific matching redirect uri parameter.
    refreshRolling : str
 Use ROLL or DONT_ROLL to override the Roll Refresh Token Values setting on the Authorization Server Settings. SERVER_DEFAULT will default to the Roll Refresh Token Values setting on the Authorization Server Setting screen. Defaults to SERVER_DEFAULT.
    requestObjectSigningAlgorithm : str
 The JSON Web Signature [JWS] algorithm that must be used to sign the Request Object. All signing algorithms are allowed if value is not present <br>RS256 - RSA using SHA-256<br>RS384 - RSA using SHA-384<br>RS512 - RSA using SHA-512<br>ES256 - ECDSA using P256 Curve and SHA-256<br>ES384 - ECDSA using P384 Curve and SHA-384<br>ES512 - ECDSA using P521 Curve and SHA-512<br>PS256 - RSASSA-PSS using SHA-256 and MGF1 padding with SHA-256<br>PS384 - RSASSA-PSS using SHA-384 and MGF1 padding with SHA-384<br>PS512 - RSASSA-PSS using SHA-512 and MGF1 padding with SHA-512<br>RSASSA-PSS is only supported with SafeNet Luna, Thales nCipher or Java 11.
    requestPolicyRef : str
 The CIBA request policy.
    requireProofKeyForCodeExchange : boolean
 Determines whether Proof Key for Code Exchange (PKCE) is required for this client.
    requireSignedRequests : boolean
 Determines whether signed requests are required for this client
    restrictScopes : boolean
 Restricts this client's access to specific scopes.
    restrictedResponseTypes : str
 The response types allowed for this client. If omitted all response types are available to the client.
    restrictedScopes : str
 The scopes available for this client.
    tokenExchangeProcessorPolicyRef : str
 The Token Exchange Processor policy.
    userAuthorizationUrlOverride : string
 The URL used as 'verification_url' and 'verification_url_complete' values in a Device Authorization request. This property overrides the 'userAuthorizationUrl' value present in Authorization Server Settings.
    validateUsingAllEligibleAtms : boolean
 Validates token using all eligible access token managers for the client.

    """

    def __init__(self, clientId:str, grantTypes, name:str, bypassActivationCodeConfirmationOverride:bool=None, bypassApprovalPage:bool=None, cibaDeliveryMode=None, cibaNotificationEndpoint:str=None, cibaPollingInterval:int=None, cibaRequestObjectSigningAlgorithm=None, cibaRequireSignedRequests:bool=None, cibaUserCodeSupported:bool=None, clientAuth=None, defaultAccessTokenManagerRef=None, description:str=None, deviceFlowSettingType=None, devicePollingIntervalOverride:int=None, enabled:bool=None, exclusiveScopes=None, extendedParameters=None, jwksSettings=None, logoUrl:str=None, oidcPolicy=None, pendingAuthorizationTimeoutOverride:int=None, persistentGrantExpirationTime:int=None, persistentGrantExpirationTimeUnit=None, persistentGrantExpirationType=None, persistentGrantIdleTimeout:int=None, persistentGrantIdleTimeoutTimeUnit=None, persistentGrantIdleTimeoutType=None, redirectUris:list=None, refreshRolling=None, requestObjectSigningAlgorithm=None, requestPolicyRef=None, requireProofKeyForCodeExchange:bool=None, requireSignedRequests:bool=None, restrictScopes:bool=None, restrictedResponseTypes=None, restrictedScopes=None, tokenExchangeProcessorPolicyRef=None, userAuthorizationUrlOverride:str=None, validateUsingAllEligibleAtms:bool=None) -> None:
        self.bypassActivationCodeConfirmationOverride = bypassActivationCodeConfirmationOverride
        self.bypassApprovalPage = bypassApprovalPage
        self.cibaDeliveryMode = cibaDeliveryMode
        self.cibaNotificationEndpoint = cibaNotificationEndpoint
        self.cibaPollingInterval = cibaPollingInterval
        self.cibaRequestObjectSigningAlgorithm = cibaRequestObjectSigningAlgorithm
        self.cibaRequireSignedRequests = cibaRequireSignedRequests
        self.cibaUserCodeSupported = cibaUserCodeSupported
        self.clientAuth = clientAuth
        self.clientId = clientId
        self.defaultAccessTokenManagerRef = defaultAccessTokenManagerRef
        self.description = description
        self.deviceFlowSettingType = deviceFlowSettingType
        self.devicePollingIntervalOverride = devicePollingIntervalOverride
        self.enabled = enabled
        self.exclusiveScopes = exclusiveScopes
        self.extendedParameters = extendedParameters
        self.grantTypes = grantTypes
        self.jwksSettings = jwksSettings
        self.logoUrl = logoUrl
        self.name = name
        self.oidcPolicy = oidcPolicy
        self.pendingAuthorizationTimeoutOverride = pendingAuthorizationTimeoutOverride
        self.persistentGrantExpirationTime = persistentGrantExpirationTime
        self.persistentGrantExpirationTimeUnit = persistentGrantExpirationTimeUnit
        self.persistentGrantExpirationType = persistentGrantExpirationType
        self.persistentGrantIdleTimeout = persistentGrantIdleTimeout
        self.persistentGrantIdleTimeoutTimeUnit = persistentGrantIdleTimeoutTimeUnit
        self.persistentGrantIdleTimeoutType = persistentGrantIdleTimeoutType
        self.redirectUris = redirectUris
        self.refreshRolling = refreshRolling
        self.requestObjectSigningAlgorithm = requestObjectSigningAlgorithm
        self.requestPolicyRef = requestPolicyRef
        self.requireProofKeyForCodeExchange = requireProofKeyForCodeExchange
        self.requireSignedRequests = requireSignedRequests
        self.restrictScopes = restrictScopes
        self.restrictedResponseTypes = restrictedResponseTypes
        self.restrictedScopes = restrictedScopes
        self.tokenExchangeProcessorPolicyRef = tokenExchangeProcessorPolicyRef
        self.userAuthorizationUrlOverride = userAuthorizationUrlOverride
        self.validateUsingAllEligibleAtms = validateUsingAllEligibleAtms

    def _validate(self) -> bool:
        return any(x for x in ["clientId", "grantTypes", "name"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Client):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.bypassActivationCodeConfirmationOverride, self.bypassApprovalPage, self.cibaDeliveryMode, self.cibaNotificationEndpoint, self.cibaPollingInterval, self.cibaRequestObjectSigningAlgorithm, self.cibaRequireSignedRequests, self.cibaUserCodeSupported, self.clientAuth, self.clientId, self.defaultAccessTokenManagerRef, self.description, self.deviceFlowSettingType, self.devicePollingIntervalOverride, self.enabled, self.exclusiveScopes, self.extendedParameters, self.grantTypes, self.jwksSettings, self.logoUrl, self.name, self.oidcPolicy, self.pendingAuthorizationTimeoutOverride, self.persistentGrantExpirationTime, self.persistentGrantExpirationTimeUnit, self.persistentGrantExpirationType, self.persistentGrantIdleTimeout, self.persistentGrantIdleTimeoutTimeUnit, self.persistentGrantIdleTimeoutType, self.redirectUris, self.refreshRolling, self.requestObjectSigningAlgorithm, self.requestPolicyRef, self.requireProofKeyForCodeExchange, self.requireSignedRequests, self.restrictScopes, self.restrictedResponseTypes, self.restrictedScopes, self.tokenExchangeProcessorPolicyRef, self.userAuthorizationUrlOverride, self.validateUsingAllEligibleAtms))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["bypassActivationCodeConfirmationOverride", "bypassApprovalPage", "cibaDeliveryMode", "cibaNotificationEndpoint", "cibaPollingInterval", "cibaRequestObjectSigningAlgorithm", "cibaRequireSignedRequests", "cibaUserCodeSupported", "clientAuth", "clientId", "defaultAccessTokenManagerRef", "description", "deviceFlowSettingType", "devicePollingIntervalOverride", "enabled", "exclusiveScopes", "extendedParameters", "grantTypes", "jwksSettings", "logoUrl", "name", "oidcPolicy", "pendingAuthorizationTimeoutOverride", "persistentGrantExpirationTime", "persistentGrantExpirationTimeUnit", "persistentGrantExpirationType", "persistentGrantIdleTimeout", "persistentGrantIdleTimeoutTimeUnit", "persistentGrantIdleTimeoutType", "redirectUris", "refreshRolling", "requestObjectSigningAlgorithm", "requestPolicyRef", "requireProofKeyForCodeExchange", "requireSignedRequests", "restrictScopes", "restrictedResponseTypes", "restrictedScopes", "tokenExchangeProcessorPolicyRef", "userAuthorizationUrlOverride", "validateUsingAllEligibleAtms"]}

        return cls(**valid_data)