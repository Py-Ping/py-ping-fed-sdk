class DynamicClientRegistration():
    """ Dynamic client registration settings.

    Attributes
    ----------
    allowedExclusiveScopes : array
        The exclusive scopes to allow.
    bypassActivationCodeConfirmationOverride : boolean
        Indicates if the Activation Code Confirmation page should be bypassed if 'verification_url_complete' is used by the end user to authorize a device.
    cibaPollingInterval : integer
        The minimum amount of time in seconds that the Client must wait between polling requests to the token endpoint. The default is 3 seconds.
    cibaRequireSignedRequests : boolean
        Determines whether CIBA signed requests are required for this client.
    clientCertIssuerRef : str
        Client TLS Certificate Issuer DN.
    clientCertIssuerType : str
        Client TLS Certificate Issuer Type.
    defaultAccessTokenManagerRef : str
        The default access token manager for this client.
    deviceFlowSettingType : str
        Allows an administrator to override the Device Authorization Settings set globally for the OAuth AS. Defaults to SERVER_DEFAULT.
    devicePollingIntervalOverride : integer
        The amount of time client should wait between polling requests, in seconds.
    enforceReplayPrevention : boolean
        Enforce replay prevention.
    initialAccessTokenScope : string
        The initial access token to prevent unwanted client registrations.
    oidcPolicy : str
        Open ID Connect Policy settings.  This is included in the message only when OIDC is enabled.
    pendingAuthorizationTimeoutOverride : integer
        The 'device_code' and 'user_code' timeout, in seconds.
    persistentGrantExpirationTime : integer
        The persistent grant expiration time.
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
    policyRefs : array
        The client registration policies.
    refreshRolling : str
        Use ROLL or DONT_ROLL to override the Roll Refresh Token Values setting on the Authorization Server Settings. SERVER_DEFAULT will default to the Roll Refresh Token Values setting on the Authorization Server Setting screen. Defaults to SERVER_DEFAULT.
    requestPolicyRef : str
        The CIBA request policy.
    requireProofKeyForCodeExchange : boolean
        Determines whether Proof Key for Code Exchange (PKCE) is required for the dynamically created client.
    requireSignedRequests : boolean
        Require signed requests.
    restrictCommonScopes : boolean
        Restrict common scopes.
    restrictedCommonScopes : array
        The common scopes to restrict.
    tokenExchangeProcessorPolicyRef : str
        The Token Exchange Processor policy.
    userAuthorizationUrlOverride : string
        The URL is used as 'verification_url' and 'verification_url_complete' values in a Device Authorization request.

    """

    __slots__ = ["allowedExclusiveScopes", "bypassActivationCodeConfirmationOverride", "cibaPollingInterval", "cibaRequireSignedRequests", "clientCertIssuerRef", "clientCertIssuerType", "defaultAccessTokenManagerRef", "deviceFlowSettingType", "devicePollingIntervalOverride", "enforceReplayPrevention", "initialAccessTokenScope", "oidcPolicy", "pendingAuthorizationTimeoutOverride", "persistentGrantExpirationTime", "persistentGrantExpirationTimeUnit", "persistentGrantExpirationType", "persistentGrantIdleTimeout", "persistentGrantIdleTimeoutTimeUnit", "persistentGrantIdleTimeoutType", "policyRefs", "refreshRolling", "requestPolicyRef", "requireProofKeyForCodeExchange", "requireSignedRequests", "restrictCommonScopes", "restrictedCommonScopes", "tokenExchangeProcessorPolicyRef", "userAuthorizationUrlOverride"]
    def __init__(self, allowedExclusiveScopes=None, bypassActivationCodeConfirmationOverride=None, cibaPollingInterval=None, cibaRequireSignedRequests=None, clientCertIssuerRef=None, clientCertIssuerType=None, defaultAccessTokenManagerRef=None, deviceFlowSettingType=None, devicePollingIntervalOverride=None, enforceReplayPrevention=None, initialAccessTokenScope=None, oidcPolicy=None, pendingAuthorizationTimeoutOverride=None, persistentGrantExpirationTime=None, persistentGrantExpirationTimeUnit=None, persistentGrantExpirationType=None, persistentGrantIdleTimeout=None, persistentGrantIdleTimeoutTimeUnit=None, persistentGrantIdleTimeoutType=None, policyRefs=None, refreshRolling=None, requestPolicyRef=None, requireProofKeyForCodeExchange=None, requireSignedRequests=None, restrictCommonScopes=None, restrictedCommonScopes=None, tokenExchangeProcessorPolicyRef=None, userAuthorizationUrlOverride=None):
            self.allowedExclusiveScopes = allowedExclusiveScopes
            self.bypassActivationCodeConfirmationOverride = bypassActivationCodeConfirmationOverride
            self.cibaPollingInterval = cibaPollingInterval
            self.cibaRequireSignedRequests = cibaRequireSignedRequests
            self.clientCertIssuerRef = clientCertIssuerRef
            self.clientCertIssuerType = clientCertIssuerType
            self.defaultAccessTokenManagerRef = defaultAccessTokenManagerRef
            self.deviceFlowSettingType = deviceFlowSettingType
            self.devicePollingIntervalOverride = devicePollingIntervalOverride
            self.enforceReplayPrevention = enforceReplayPrevention
            self.initialAccessTokenScope = initialAccessTokenScope
            self.oidcPolicy = oidcPolicy
            self.pendingAuthorizationTimeoutOverride = pendingAuthorizationTimeoutOverride
            self.persistentGrantExpirationTime = persistentGrantExpirationTime
            self.persistentGrantExpirationTimeUnit = persistentGrantExpirationTimeUnit
            self.persistentGrantExpirationType = persistentGrantExpirationType
            self.persistentGrantIdleTimeout = persistentGrantIdleTimeout
            self.persistentGrantIdleTimeoutTimeUnit = persistentGrantIdleTimeoutTimeUnit
            self.persistentGrantIdleTimeoutType = persistentGrantIdleTimeoutType
            self.policyRefs = policyRefs
            self.refreshRolling = refreshRolling
            self.requestPolicyRef = requestPolicyRef
            self.requireProofKeyForCodeExchange = requireProofKeyForCodeExchange
            self.requireSignedRequests = requireSignedRequests
            self.restrictCommonScopes = restrictCommonScopes
            self.restrictedCommonScopes = restrictedCommonScopes
            self.tokenExchangeProcessorPolicyRef = tokenExchangeProcessorPolicyRef
            self.userAuthorizationUrlOverride = userAuthorizationUrlOverride
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, DynamicClientRegistration):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((allowedExclusiveScopes, bypassActivationCodeConfirmationOverride, cibaPollingInterval, cibaRequireSignedRequests, clientCertIssuerRef, clientCertIssuerType, defaultAccessTokenManagerRef, deviceFlowSettingType, devicePollingIntervalOverride, enforceReplayPrevention, initialAccessTokenScope, oidcPolicy, pendingAuthorizationTimeoutOverride, persistentGrantExpirationTime, persistentGrantExpirationTimeUnit, persistentGrantExpirationType, persistentGrantIdleTimeout, persistentGrantIdleTimeoutTimeUnit, persistentGrantIdleTimeoutType, policyRefs, refreshRolling, requestPolicyRef, requireProofKeyForCodeExchange, requireSignedRequests, restrictCommonScopes, restrictedCommonScopes, tokenExchangeProcessorPolicyRef, userAuthorizationUrlOverride))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
