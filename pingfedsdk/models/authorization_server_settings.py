from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.persistent_grant_contract import PersistentGrantContract
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.models.scope_group_entry import ScopeGroupEntry
from pingfedsdk.models.scope_entry import ScopeEntry
from pingfedsdk.enums import ParStatus
from pingfedsdk.enums import UserAuthorizationConsentPageSetting
from pingfedsdk.enums import ActivationCodeCheckMode
from pingfedsdk.enums import TimeUnit


class AuthorizationServerSettings(Model):
    """Authorization Server Settings attributes.

    Attributes
    ----------
    defaultScopeDescription: str
        The default scope description.

    scopes: list
        The list of common scopes.

    scopeGroups: list
        The list of common scope groups.

    exclusiveScopes: list
        The list of exclusive scopes.

    exclusiveScopeGroups: list
        The list of exclusive scope groups.

    authorizationCodeTimeout: int
        The authorization code timeout, in seconds.

    authorizationCodeEntropy: int
        The authorization code entropy, in bytes.

    disallowPlainPKCE: bool
        Determines whether PKCE's 'plain' code challenge method will be disallowed. The default value is false.

    includeIssuerInAuthorizationResponse: bool
        Determines whether the authorization server's issuer value is added to the authorization response or not. The default value is false.

    trackUserSessionsForLogout: bool
        Determines whether user sessions are tracked for logout. If this property is not provided on a PUT, the setting is left unchanged.

    tokenEndpointBaseUrl: str
        The token endpoint base URL used to validate the 'aud' claim during Private Key JWT Client Authentication.

    persistentGrantLifetime: int
        The persistent grant lifetime. The default value is indefinite. -1 indicates an indefinite amount of time.

    persistentGrantLifetimeUnit: TimeUnit
        The persistent grant lifetime unit.

    persistentGrantIdleTimeout: int
        The persistent grant idle timeout. The default value is 30 (days). -1 indicates an indefinite amount of time.

    persistentGrantIdleTimeoutTimeUnit: TimeUnit
        The persistent grant idle timeout time unit.

    refreshTokenLength: int
        The refresh token length in number of characters.

    rollRefreshTokenValues: bool
        The roll refresh token values default policy. The default value is true.

    refreshTokenRollingGracePeriod: int
        The grace period that a rolled refresh token remains valid in seconds. The default value is 0.

    refreshRollingInterval: int
        The minimum interval to roll refresh tokens, in hours.

    persistentGrantReuseGrantTypes: list
        The grant types that the OAuth AS can reuse rather than creating a new grant for each request. Only 'IMPLICIT' or 'AUTHORIZATION_CODE' or 'RESOURCE_OWNER_CREDENTIALS' are valid grant types.

    persistentGrantContract: PersistentGrantContract
        The persistent grant contract defines attributes that are associated with OAuth persistent grants.

    bypassAuthorizationForApprovedGrants: bool
        Bypass authorization for previously approved persistent grants. The default value is false.

    allowUnidentifiedClientROCreds: bool
        Allow unidentified clients to request resource owner password credentials grants. The default value is false.

    allowUnidentifiedClientExtensionGrants: bool
        Allow unidentified clients to request extension grants. The default value is false.

    adminWebServicePcvRef: ResourceLink
        The password credential validator reference that is used for authenticating access to the OAuth Administrative Web Service.

    atmIdForOAuthGrantManagement: str
        The ID of the Access Token Manager used for OAuth enabled grant management.

    scopeForOAuthGrantManagement: str
        The OAuth scope to validate when accessing grant management service.

    allowedOrigins: list
        The list of allowed origins.

    userAuthorizationUrl: str
        The URL used to generate 'verification_url' and 'verification_url_complete' values in a Device Authorization request

    registeredAuthorizationPath: str
        The Registered Authorization Path is concatenated to PingFederate base URL to generate 'verification_url' and 'verification_url_complete' values in a Device Authorization request. PingFederate listens to this path if specified

    pendingAuthorizationTimeout: int
        The 'device_code' and 'user_code' timeout, in seconds.

    devicePollingInterval: int
        The amount of time client should wait between polling requests, in seconds.

    activationCodeCheckMode: ActivationCodeCheckMode
        Determines whether the user is prompted to enter or confirm the activation code after authenticating or before. The default is AFTER_AUTHENTICATION.

    bypassActivationCodeConfirmation: bool
        Indicates if the Activation Code Confirmation page should be bypassed if 'verification_url_complete' is used by the end user to authorize a device.

    userAuthorizationConsentPageSetting: UserAuthorizationConsentPageSetting
        User Authorization Consent Page setting to use PingFederate's internal consent page or an external system

    userAuthorizationConsentAdapter: str
        Adapter ID of the external consent adapter to be used for the consent page user interface.

    approvedScopesAttribute: str
        Attribute from the external consent adapter's contract, intended for storing approved scopes returned by the external consent page.

    parReferenceTimeout: int
        The timeout, in seconds, of the pushed authorization request reference. The default value is 60.

    parReferenceLength: int
        The entropy of pushed authorization request references, in bytes. The default value is 24.

    parStatus: ParStatus
        The status of pushed authorization request support. The default value is ENABLED.

    clientSecretRetentionPeriod: int
        The length of time in minutes that client secrets will be retained as secondary secrets after secret change. The default value is 0, which will disable secondary client secret retention.

    jwtSecuredAuthorizationResponseModeLifetime: int
        The lifetime, in seconds, of the JWT Secured authorization response. The default value is 600.

    """

    def __init__(self, authorizationCodeEntropy: int, authorizationCodeTimeout: int, bypassActivationCodeConfirmation: bool, defaultScopeDescription: str, devicePollingInterval: int, pendingAuthorizationTimeout: int, refreshRollingInterval: int, refreshTokenLength: int, registeredAuthorizationPath: str, scopes: list = None, scopeGroups: list = None, exclusiveScopes: list = None, exclusiveScopeGroups: list = None, disallowPlainPKCE: bool = None, includeIssuerInAuthorizationResponse: bool = None, trackUserSessionsForLogout: bool = None, tokenEndpointBaseUrl: str = None, persistentGrantLifetime: int = None, persistentGrantLifetimeUnit: TimeUnit = None, persistentGrantIdleTimeout: int = None, persistentGrantIdleTimeoutTimeUnit: TimeUnit = None, rollRefreshTokenValues: bool = None, refreshTokenRollingGracePeriod: int = None, persistentGrantReuseGrantTypes: list = None, persistentGrantContract: PersistentGrantContract = None, bypassAuthorizationForApprovedGrants: bool = None, allowUnidentifiedClientROCreds: bool = None, allowUnidentifiedClientExtensionGrants: bool = None, adminWebServicePcvRef: ResourceLink = None, atmIdForOAuthGrantManagement: str = None, scopeForOAuthGrantManagement: str = None, allowedOrigins: list = None, userAuthorizationUrl: str = None, activationCodeCheckMode: ActivationCodeCheckMode = None, userAuthorizationConsentPageSetting: UserAuthorizationConsentPageSetting = None, userAuthorizationConsentAdapter: str = None, approvedScopesAttribute: str = None, parReferenceTimeout: int = None, parReferenceLength: int = None, parStatus: ParStatus = None, clientSecretRetentionPeriod: int = None, jwtSecuredAuthorizationResponseModeLifetime: int = None) -> None:
        self.defaultScopeDescription = defaultScopeDescription
        self.scopes = scopes
        self.scopeGroups = scopeGroups
        self.exclusiveScopes = exclusiveScopes
        self.exclusiveScopeGroups = exclusiveScopeGroups
        self.authorizationCodeTimeout = authorizationCodeTimeout
        self.authorizationCodeEntropy = authorizationCodeEntropy
        self.disallowPlainPKCE = disallowPlainPKCE
        self.includeIssuerInAuthorizationResponse = includeIssuerInAuthorizationResponse
        self.trackUserSessionsForLogout = trackUserSessionsForLogout
        self.tokenEndpointBaseUrl = tokenEndpointBaseUrl
        self.persistentGrantLifetime = persistentGrantLifetime
        self.persistentGrantLifetimeUnit = persistentGrantLifetimeUnit
        self.persistentGrantIdleTimeout = persistentGrantIdleTimeout
        self.persistentGrantIdleTimeoutTimeUnit = persistentGrantIdleTimeoutTimeUnit
        self.refreshTokenLength = refreshTokenLength
        self.rollRefreshTokenValues = rollRefreshTokenValues
        self.refreshTokenRollingGracePeriod = refreshTokenRollingGracePeriod
        self.refreshRollingInterval = refreshRollingInterval
        self.persistentGrantReuseGrantTypes = persistentGrantReuseGrantTypes
        self.persistentGrantContract = persistentGrantContract
        self.bypassAuthorizationForApprovedGrants = bypassAuthorizationForApprovedGrants
        self.allowUnidentifiedClientROCreds = allowUnidentifiedClientROCreds
        self.allowUnidentifiedClientExtensionGrants = allowUnidentifiedClientExtensionGrants
        self.adminWebServicePcvRef = adminWebServicePcvRef
        self.atmIdForOAuthGrantManagement = atmIdForOAuthGrantManagement
        self.scopeForOAuthGrantManagement = scopeForOAuthGrantManagement
        self.allowedOrigins = allowedOrigins
        self.userAuthorizationUrl = userAuthorizationUrl
        self.registeredAuthorizationPath = registeredAuthorizationPath
        self.pendingAuthorizationTimeout = pendingAuthorizationTimeout
        self.devicePollingInterval = devicePollingInterval
        self.activationCodeCheckMode = activationCodeCheckMode
        self.bypassActivationCodeConfirmation = bypassActivationCodeConfirmation
        self.userAuthorizationConsentPageSetting = userAuthorizationConsentPageSetting
        self.userAuthorizationConsentAdapter = userAuthorizationConsentAdapter
        self.approvedScopesAttribute = approvedScopesAttribute
        self.parReferenceTimeout = parReferenceTimeout
        self.parReferenceLength = parReferenceLength
        self.parStatus = parStatus
        self.clientSecretRetentionPeriod = clientSecretRetentionPeriod
        self.jwtSecuredAuthorizationResponseModeLifetime = jwtSecuredAuthorizationResponseModeLifetime

    def _validate(self) -> bool:
        return any(x for x in ["authorizationCodeEntropy", "authorizationCodeTimeout", "bypassActivationCodeConfirmation", "defaultScopeDescription", "devicePollingInterval", "pendingAuthorizationTimeout", "refreshRollingInterval", "refreshTokenLength", "registeredAuthorizationPath"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthorizationServerSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.defaultScopeDescription, self.scopes, self.scopeGroups, self.exclusiveScopes, self.exclusiveScopeGroups, self.authorizationCodeTimeout, self.authorizationCodeEntropy, self.disallowPlainPKCE, self.includeIssuerInAuthorizationResponse, self.trackUserSessionsForLogout, self.tokenEndpointBaseUrl, self.persistentGrantLifetime, self.persistentGrantLifetimeUnit, self.persistentGrantIdleTimeout, self.persistentGrantIdleTimeoutTimeUnit, self.refreshTokenLength, self.rollRefreshTokenValues, self.refreshTokenRollingGracePeriod, self.refreshRollingInterval, self.persistentGrantReuseGrantTypes, self.persistentGrantContract, self.bypassAuthorizationForApprovedGrants, self.allowUnidentifiedClientROCreds, self.allowUnidentifiedClientExtensionGrants, self.adminWebServicePcvRef, self.atmIdForOAuthGrantManagement, self.scopeForOAuthGrantManagement, self.allowedOrigins, self.userAuthorizationUrl, self.registeredAuthorizationPath, self.pendingAuthorizationTimeout, self.devicePollingInterval, self.activationCodeCheckMode, self.bypassActivationCodeConfirmation, self.userAuthorizationConsentPageSetting, self.userAuthorizationConsentAdapter, self.approvedScopesAttribute, self.parReferenceTimeout, self.parReferenceLength, self.parStatus, self.clientSecretRetentionPeriod, self.jwtSecuredAuthorizationResponseModeLifetime]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["defaultScopeDescription", "scopes", "scopeGroups", "exclusiveScopes", "exclusiveScopeGroups", "authorizationCodeTimeout", "authorizationCodeEntropy", "disallowPlainPKCE", "includeIssuerInAuthorizationResponse", "trackUserSessionsForLogout", "tokenEndpointBaseUrl", "persistentGrantLifetime", "persistentGrantLifetimeUnit", "persistentGrantIdleTimeout", "persistentGrantIdleTimeoutTimeUnit", "refreshTokenLength", "rollRefreshTokenValues", "refreshTokenRollingGracePeriod", "refreshRollingInterval", "persistentGrantReuseGrantTypes", "persistentGrantContract", "bypassAuthorizationForApprovedGrants", "allowUnidentifiedClientROCreds", "allowUnidentifiedClientExtensionGrants", "adminWebServicePcvRef", "atmIdForOAuthGrantManagement", "scopeForOAuthGrantManagement", "allowedOrigins", "userAuthorizationUrl", "registeredAuthorizationPath", "pendingAuthorizationTimeout", "devicePollingInterval", "activationCodeCheckMode", "bypassActivationCodeConfirmation", "userAuthorizationConsentPageSetting", "userAuthorizationConsentAdapter", "approvedScopesAttribute", "parReferenceTimeout", "parReferenceLength", "parStatus", "clientSecretRetentionPeriod", "jwtSecuredAuthorizationResponseModeLifetime"] and v is not None:
                if k == "defaultScopeDescription":
                    valid_data[k] = str(v)
                if k == "scopes":
                    valid_data[k] = [ScopeEntry(**x) for x in v]
                if k == "scopeGroups":
                    valid_data[k] = [ScopeGroupEntry(**x) for x in v]
                if k == "exclusiveScopes":
                    valid_data[k] = [ScopeEntry(**x) for x in v]
                if k == "exclusiveScopeGroups":
                    valid_data[k] = [ScopeGroupEntry(**x) for x in v]
                if k == "authorizationCodeTimeout":
                    valid_data[k] = int(v)
                if k == "authorizationCodeEntropy":
                    valid_data[k] = int(v)
                if k == "disallowPlainPKCE":
                    valid_data[k] = bool(v)
                if k == "includeIssuerInAuthorizationResponse":
                    valid_data[k] = bool(v)
                if k == "trackUserSessionsForLogout":
                    valid_data[k] = bool(v)
                if k == "tokenEndpointBaseUrl":
                    valid_data[k] = str(v)
                if k == "persistentGrantLifetime":
                    valid_data[k] = int(v)
                if k == "persistentGrantLifetimeUnit":
                    valid_data[k] = TimeUnit[v]
                if k == "persistentGrantIdleTimeout":
                    valid_data[k] = int(v)
                if k == "persistentGrantIdleTimeoutTimeUnit":
                    valid_data[k] = TimeUnit[v]
                if k == "refreshTokenLength":
                    valid_data[k] = int(v)
                if k == "rollRefreshTokenValues":
                    valid_data[k] = bool(v)
                if k == "refreshTokenRollingGracePeriod":
                    valid_data[k] = int(v)
                if k == "refreshRollingInterval":
                    valid_data[k] = int(v)
                if k == "persistentGrantReuseGrantTypes":
                    valid_data[k] = [str(x) for x in v]
                if k == "persistentGrantContract":
                    valid_data[k] = PersistentGrantContract(**v)
                if k == "bypassAuthorizationForApprovedGrants":
                    valid_data[k] = bool(v)
                if k == "allowUnidentifiedClientROCreds":
                    valid_data[k] = bool(v)
                if k == "allowUnidentifiedClientExtensionGrants":
                    valid_data[k] = bool(v)
                if k == "adminWebServicePcvRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "atmIdForOAuthGrantManagement":
                    valid_data[k] = str(v)
                if k == "scopeForOAuthGrantManagement":
                    valid_data[k] = str(v)
                if k == "allowedOrigins":
                    valid_data[k] = [str(x) for x in v]
                if k == "userAuthorizationUrl":
                    valid_data[k] = str(v)
                if k == "registeredAuthorizationPath":
                    valid_data[k] = str(v)
                if k == "pendingAuthorizationTimeout":
                    valid_data[k] = int(v)
                if k == "devicePollingInterval":
                    valid_data[k] = int(v)
                if k == "activationCodeCheckMode":
                    valid_data[k] = ActivationCodeCheckMode[v]
                if k == "bypassActivationCodeConfirmation":
                    valid_data[k] = bool(v)
                if k == "userAuthorizationConsentPageSetting":
                    valid_data[k] = UserAuthorizationConsentPageSetting[v]
                if k == "userAuthorizationConsentAdapter":
                    valid_data[k] = str(v)
                if k == "approvedScopesAttribute":
                    valid_data[k] = str(v)
                if k == "parReferenceTimeout":
                    valid_data[k] = int(v)
                if k == "parReferenceLength":
                    valid_data[k] = int(v)
                if k == "parStatus":
                    valid_data[k] = ParStatus[v]
                if k == "clientSecretRetentionPeriod":
                    valid_data[k] = int(v)
                if k == "jwtSecuredAuthorizationResponseModeLifetime":
                    valid_data[k] = int(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["defaultScopeDescription", "scopes", "scopeGroups", "exclusiveScopes", "exclusiveScopeGroups", "authorizationCodeTimeout", "authorizationCodeEntropy", "disallowPlainPKCE", "includeIssuerInAuthorizationResponse", "trackUserSessionsForLogout", "tokenEndpointBaseUrl", "persistentGrantLifetime", "persistentGrantLifetimeUnit", "persistentGrantIdleTimeout", "persistentGrantIdleTimeoutTimeUnit", "refreshTokenLength", "rollRefreshTokenValues", "refreshTokenRollingGracePeriod", "refreshRollingInterval", "persistentGrantReuseGrantTypes", "persistentGrantContract", "bypassAuthorizationForApprovedGrants", "allowUnidentifiedClientROCreds", "allowUnidentifiedClientExtensionGrants", "adminWebServicePcvRef", "atmIdForOAuthGrantManagement", "scopeForOAuthGrantManagement", "allowedOrigins", "userAuthorizationUrl", "registeredAuthorizationPath", "pendingAuthorizationTimeout", "devicePollingInterval", "activationCodeCheckMode", "bypassActivationCodeConfirmation", "userAuthorizationConsentPageSetting", "userAuthorizationConsentAdapter", "approvedScopesAttribute", "parReferenceTimeout", "parReferenceLength", "parStatus", "clientSecretRetentionPeriod", "jwtSecuredAuthorizationResponseModeLifetime"]:
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
