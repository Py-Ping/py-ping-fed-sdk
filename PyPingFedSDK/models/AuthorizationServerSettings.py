class AuthorizationServerSettings():
    """Authorization Server Settings attributes.

    Attributes
    ----------
    adminWebServicePcvRef : str
        The password credential validator reference that is used for authenticating access to the OAuth Administrative Web Service.    allowUnidentifiedClientExtensionGrants : boolean
        Allow unidentified clients to request extension grants. The default value is false.    allowUnidentifiedClientROCreds : boolean
        Allow unidentified clients to request resource owner password credentials grants. The default value is false.    allowedOrigins : array
        The list of allowed origins.    approvedScopesAttribute : string
        Attribute from the external consent adapter's contract, intended for storing approved scopes returned by the external consent page.    atmIdForOAuthGrantManagement : string
        The ID of the Access Token Manager used for OAuth enabled grant management.    authorizationCodeEntropy : integer
        The authorization code entropy, in bytes.    authorizationCodeTimeout : integer
        The authorization code timeout, in seconds.    bypassActivationCodeConfirmation : boolean
        Indicates if the Activation Code Confirmation page should be bypassed if 'verification_url_complete' is used by the end user to authorize a device.    bypassAuthorizationForApprovedGrants : boolean
        Bypass authorization for previously approved persistent grants. The default value is false.    defaultScopeDescription : string
        The default scope description.    devicePollingInterval : integer
        The amount of time client should wait between polling requests, in seconds.    exclusiveScopeGroups : array
        The list of exclusive scope groups.    exclusiveScopes : array
        The list of exclusive scopes.    pendingAuthorizationTimeout : integer
        The 'device_code' and 'user_code' timeout, in seconds.    persistentGrantContract : str
        The persistent grant contract defines attributes that are associated with OAuth persistent grants.    persistentGrantIdleTimeout : integer
        The persistent grant idle timeout.    persistentGrantIdleTimeoutTimeUnit : str
        The persistent grant idle timeout time unit.    persistentGrantLifetime : integer
        The persistent grant lifetime. The default value is indefinite.    persistentGrantLifetimeUnit : str
        The persistent grant lifetime unit.    persistentGrantReuseGrantTypes : array
        The grant types that the OAuth AS can reuse rather than creating a new grant for each request.    refreshRollingInterval : integer
        The minimum interval to roll refresh tokens, in hours.    refreshTokenLength : integer
        The refresh token length in number of characters.    registeredAuthorizationPath : string
        The Registered Authorization Path is concatenated to PingFederate base URL to generate 'verification_url' and 'verification_url_complete' values in a Device Authorization request. PingFederate listens to this path if specified    rollRefreshTokenValues : boolean
        The roll refresh token values default policy. The default value is true.    scopeForOAuthGrantManagement : string
        The OAuth scope to validate when accessing grant management service.    scopeGroups : array
        The list of common scope groups.    scopes : array
        The list of common scopes.    tokenEndpointBaseUrl : string
        The token endpoint base URL used to validate the 'aud' claim during Private Key JWT Client Authentication.    trackUserSessionsForLogout : boolean
        Determines whether user sessions are tracked for logout. If this property is not provided on a PUT, the setting is left unchanged.    userAuthorizationConsentAdapter : string
        Adapter ID of the external consent adapter to be used for the consent page user interface.    userAuthorizationConsentPageSetting : str
        User Authorization Consent Page setting to use PingFederate's internal consent page or an external system    userAuthorizationUrl : string
        The URL used to generate 'verification_url' and 'verification_url_complete' values in a Device Authorization request
    """

    __slots__ = ["adminWebServicePcvRef", "allowUnidentifiedClientExtensionGrants", "allowUnidentifiedClientROCreds", "allowedOrigins", "approvedScopesAttribute", "atmIdForOAuthGrantManagement", "authorizationCodeEntropy", "authorizationCodeTimeout", "bypassActivationCodeConfirmation", "bypassAuthorizationForApprovedGrants", "defaultScopeDescription", "devicePollingInterval", "exclusiveScopeGroups", "exclusiveScopes", "pendingAuthorizationTimeout", "persistentGrantContract", "persistentGrantIdleTimeout", "persistentGrantIdleTimeoutTimeUnit", "persistentGrantLifetime", "persistentGrantLifetimeUnit", "persistentGrantReuseGrantTypes", "refreshRollingInterval", "refreshTokenLength", "registeredAuthorizationPath", "rollRefreshTokenValues", "scopeForOAuthGrantManagement", "scopeGroups", "scopes", "tokenEndpointBaseUrl", "trackUserSessionsForLogout", "userAuthorizationConsentAdapter", "userAuthorizationConsentPageSetting", "userAuthorizationUrl"]

    def __init__(self, defaultScopeDescription, authorizationCodeTimeout, authorizationCodeEntropy, refreshTokenLength, refreshRollingInterval, registeredAuthorizationPath, pendingAuthorizationTimeout, devicePollingInterval, bypassActivationCodeConfirmation, adminWebServicePcvRef=None, allowUnidentifiedClientExtensionGrants=None, allowUnidentifiedClientROCreds=None, allowedOrigins=None, approvedScopesAttribute=None, atmIdForOAuthGrantManagement=None, bypassAuthorizationForApprovedGrants=None, exclusiveScopeGroups=None, exclusiveScopes=None, persistentGrantContract=None, persistentGrantIdleTimeout=None, persistentGrantIdleTimeoutTimeUnit=None, persistentGrantLifetime=None, persistentGrantLifetimeUnit=None, persistentGrantReuseGrantTypes=None, rollRefreshTokenValues=None, scopeForOAuthGrantManagement=None, scopeGroups=None, scopes=None, tokenEndpointBaseUrl=None, trackUserSessionsForLogout=None, userAuthorizationConsentAdapter=None, userAuthorizationConsentPageSetting=None, userAuthorizationUrl=None):
        self.adminWebServicePcvRef = adminWebServicePcvRef
        self.allowUnidentifiedClientExtensionGrants = allowUnidentifiedClientExtensionGrants
        self.allowUnidentifiedClientROCreds = allowUnidentifiedClientROCreds
        self.allowedOrigins = allowedOrigins
        self.approvedScopesAttribute = approvedScopesAttribute
        self.atmIdForOAuthGrantManagement = atmIdForOAuthGrantManagement
        self.authorizationCodeEntropy = authorizationCodeEntropy
        self.authorizationCodeTimeout = authorizationCodeTimeout
        self.bypassActivationCodeConfirmation = bypassActivationCodeConfirmation
        self.bypassAuthorizationForApprovedGrants = bypassAuthorizationForApprovedGrants
        self.defaultScopeDescription = defaultScopeDescription
        self.devicePollingInterval = devicePollingInterval
        self.exclusiveScopeGroups = exclusiveScopeGroups
        self.exclusiveScopes = exclusiveScopes
        self.pendingAuthorizationTimeout = pendingAuthorizationTimeout
        self.persistentGrantContract = persistentGrantContract
        self.persistentGrantIdleTimeout = persistentGrantIdleTimeout
        self.persistentGrantIdleTimeoutTimeUnit = persistentGrantIdleTimeoutTimeUnit
        self.persistentGrantLifetime = persistentGrantLifetime
        self.persistentGrantLifetimeUnit = persistentGrantLifetimeUnit
        self.persistentGrantReuseGrantTypes = persistentGrantReuseGrantTypes
        self.refreshRollingInterval = refreshRollingInterval
        self.refreshTokenLength = refreshTokenLength
        self.registeredAuthorizationPath = registeredAuthorizationPath
        self.rollRefreshTokenValues = rollRefreshTokenValues
        self.scopeForOAuthGrantManagement = scopeForOAuthGrantManagement
        self.scopeGroups = scopeGroups
        self.scopes = scopes
        self.tokenEndpointBaseUrl = tokenEndpointBaseUrl
        self.trackUserSessionsForLogout = trackUserSessionsForLogout
        self.userAuthorizationConsentAdapter = userAuthorizationConsentAdapter
        self.userAuthorizationConsentPageSetting = userAuthorizationConsentPageSetting
        self.userAuthorizationUrl = userAuthorizationUrl

    def _validate(self):
        return any(x for x in ['defaultScopeDescription', 'authorizationCodeTimeout', 'authorizationCodeEntropy', 'refreshTokenLength', 'refreshRollingInterval', 'registeredAuthorizationPath', 'pendingAuthorizationTimeout', 'devicePollingInterval', 'bypassActivationCodeConfirmation'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AuthorizationServerSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.adminWebServicePcvRef, self.allowUnidentifiedClientExtensionGrants, self.allowUnidentifiedClientROCreds, self.allowedOrigins, self.approvedScopesAttribute, self.atmIdForOAuthGrantManagement, self.authorizationCodeEntropy, self.authorizationCodeTimeout, self.bypassActivationCodeConfirmation, self.bypassAuthorizationForApprovedGrants, self.defaultScopeDescription, self.devicePollingInterval, self.exclusiveScopeGroups, self.exclusiveScopes, self.pendingAuthorizationTimeout, self.persistentGrantContract, self.persistentGrantIdleTimeout, self.persistentGrantIdleTimeoutTimeUnit, self.persistentGrantLifetime, self.persistentGrantLifetimeUnit, self.persistentGrantReuseGrantTypes, self.refreshRollingInterval, self.refreshTokenLength, self.registeredAuthorizationPath, self.rollRefreshTokenValues, self.scopeForOAuthGrantManagement, self.scopeGroups, self.scopes, self.tokenEndpointBaseUrl, self.trackUserSessionsForLogout, self.userAuthorizationConsentAdapter, self.userAuthorizationConsentPageSetting, self.userAuthorizationUrl))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["adminWebServicePcvRef", "allowUnidentifiedClientExtensionGrants", "allowUnidentifiedClientROCreds", "allowedOrigins", "approvedScopesAttribute", "atmIdForOAuthGrantManagement", "authorizationCodeEntropy", "authorizationCodeTimeout", "bypassActivationCodeConfirmation", "bypassAuthorizationForApprovedGrants", "defaultScopeDescription", "devicePollingInterval", "exclusiveScopeGroups", "exclusiveScopes", "pendingAuthorizationTimeout", "persistentGrantContract", "persistentGrantIdleTimeout", "persistentGrantIdleTimeoutTimeUnit", "persistentGrantLifetime", "persistentGrantLifetimeUnit", "persistentGrantReuseGrantTypes", "refreshRollingInterval", "refreshTokenLength", "registeredAuthorizationPath", "rollRefreshTokenValues", "scopeForOAuthGrantManagement", "scopeGroups", "scopes", "tokenEndpointBaseUrl", "trackUserSessionsForLogout", "userAuthorizationConsentAdapter", "userAuthorizationConsentPageSetting", "userAuthorizationUrl"]}

        return cls(**valid_data)
