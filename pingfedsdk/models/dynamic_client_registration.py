from enum import Enum

from pingfedsdk.enums import ClientCertIssuerType
from pingfedsdk.enums import DeviceFlowSettingType
from pingfedsdk.enums import PersistentGrantLifetimeType
from pingfedsdk.enums import RefreshRolling
from pingfedsdk.enums import RefreshTokenRollingGracePeriodType
from pingfedsdk.enums import TimeUnit
from pingfedsdk.model import Model
from pingfedsdk.models.client_registration_o_i_d_c_policy import ClientRegistrationOIDCPolicy
from pingfedsdk.models.resource_link import ResourceLink


class DynamicClientRegistration(Model):
    """Dynamic client registration settings.

    Attributes
    ----------
    initialAccessTokenScope: str
        The initial access token to prevent unwanted client registrations.

    restrictCommonScopes: bool
        Restrict common scopes.

    restrictedCommonScopes: list
        The common scopes to restrict.

    allowedExclusiveScopes: list
        The exclusive scopes to allow.

    enforceReplayPrevention: bool
        Enforce replay prevention.

    requireSignedRequests: bool
        Require signed requests.

    defaultAccessTokenManagerRef: ResourceLink
        The default access token manager for this client.

    restrictToDefaultAccessTokenManager: bool
        Determines whether the client is restricted to using only its default access token manager. The default is false.

    persistentGrantExpirationType: PersistentGrantLifetimeType
        Allows an administrator to override the Persistent Grant Lifetime set globally for the OAuth AS. Defaults to SERVER_DEFAULT.

    persistentGrantExpirationTime: int
        The persistent grant expiration time.

    persistentGrantExpirationTimeUnit: TimeUnit
        The persistent grant expiration time unit.

    persistentGrantIdleTimeoutType: PersistentGrantLifetimeType
        Allows an administrator to override the Persistent Grant Idle Timeout set globally for the OAuth AS. Defaults to SERVER_DEFAULT.

    persistentGrantIdleTimeout: int
        The persistent grant idle timeout.

    persistentGrantIdleTimeoutTimeUnit: TimeUnit
        The persistent grant idle timeout time unit.

    clientCertIssuerType: ClientCertIssuerType
        Client TLS Certificate Issuer Type.

    clientCertIssuerRef: ResourceLink
        Client TLS Certificate Issuer DN.

    refreshRolling: RefreshRolling
        Use ROLL or DONT_ROLL to override the Roll Refresh Token Values setting on the Authorization Server Settings. SERVER_DEFAULT will default to the Roll Refresh Token Values setting on the Authorization Server Setting screen. Defaults to SERVER_DEFAULT.

    refreshTokenRollingIntervalType: DeviceFlowSettingType
        Use OVERRIDE_SERVER_DEFAULT to override the Refresh Token Rolling Interval value on the Authorization Server Settings. SERVER_DEFAULT will default to the Refresh Token Rolling Interval value on the Authorization Server Setting. Defaults to SERVER_DEFAULT.

    refreshTokenRollingInterval: int
        The minimum interval to roll refresh tokens, in hours. This value will override the Refresh Token Rolling Interval Value on the Authorization Server Settings.

    oidcPolicy: ClientRegistrationOIDCPolicy
        Open ID Connect Policy settings.  This is included in the message only when OIDC is enabled.

    policyRefs: list
        The client registration policies.

    deviceFlowSettingType: DeviceFlowSettingType
        Allows an administrator to override the Device Authorization Settings set globally for the OAuth AS. Defaults to SERVER_DEFAULT.

    userAuthorizationUrlOverride: str
        The URL is used as 'verification_url' and 'verification_url_complete' values in a Device Authorization request.

    pendingAuthorizationTimeoutOverride: int
        The 'device_code' and 'user_code' timeout, in seconds.

    devicePollingIntervalOverride: int
        The amount of time client should wait between polling requests, in seconds.

    bypassActivationCodeConfirmationOverride: bool
        Indicates if the Activation Code Confirmation page should be bypassed if 'verification_url_complete' is used by the end user to authorize a device.

    requireProofKeyForCodeExchange: bool
        Determines whether Proof Key for Code Exchange (PKCE) is required for the dynamically created client.

    cibaPollingInterval: int
        The minimum amount of time in seconds that the Client must wait between polling requests to the token endpoint. The default is 3 seconds.

    cibaRequireSignedRequests: bool
        Determines whether CIBA signed requests are required for this client.

    requestPolicyRef: ResourceLink
        The CIBA request policy.

    tokenExchangeProcessorPolicyRef: ResourceLink
        The Token Exchange Processor policy.

    rotateClientSecret: bool
        Rotate registration access token on dynamic client management requests.

    rotateRegistrationAccessToken: bool
        Rotate client secret on dynamic client management requests.

    allowClientDelete: bool
        Allow client deletion from dynamic client management.

    disableRegistrationAccessTokens: bool
        Disable registration access tokens. Local standards may mandate different registration access token requirements. If applicable, implement custom validation and enforcement rules using the DynamicClientRegistrationPlugin interface from the PingFederate SDK, configure the client registration policies (policyRefs), and set this property (disableRegistrationAccessTokens) to true. CAUTION: When the disableRegistrationAccessTokens property is set to true, all clients, not just the ones created using the Dynamic Client Registration protocol, are vulnerable to unrestricted retrievals, updates (including modifications to the client authentication scheme and redirect URIs), and deletes at the /as/clients.oauth2 endpoint unless one or more client registration policies are in place to protect against unauthorized attempts.

    refreshTokenRollingGracePeriodType: RefreshTokenRollingGracePeriodType
        When specified, it overrides the global Refresh Token Grace Period defined in the Authorization Server Settings. The default value is SERVER_DEFAULT

    refreshTokenRollingGracePeriod: int
        The grace period that a rolled refresh token remains valid in seconds.

    retainClientSecret: bool
        Temporarily retain the old client secret on client secret change.

    clientSecretRetentionPeriodType: str
        Use OVERRIDE_SERVER_DEFAULT to override the Client Secret Retention Period value on the Authorization Server Settings. SERVER_DEFAULT will default to the Client Secret Retention Period value on the Authorization Server Setting. Defaults to SERVER_DEFAULT.

    clientSecretRetentionPeriodOverride: int
        The length of time in minutes that client secrets will be retained as secondary secrets after secret change. The default value is 0, which will disable secondary client secret retention. This value will override the Client Secret Retention Period value on the Authorization Server Settings.

    requireJwtSecuredAuthorizationResponseMode: bool
        Determines whether JWT Secured authorization response mode is required when initiating an authorization request. The default is false.

    """
    def __init__(self, initialAccessTokenScope: str = None, restrictCommonScopes: bool = None, restrictedCommonScopes: list = None, allowedExclusiveScopes: list = None, enforceReplayPrevention: bool = None, requireSignedRequests: bool = None, defaultAccessTokenManagerRef: ResourceLink = None, restrictToDefaultAccessTokenManager: bool = None, persistentGrantExpirationType: PersistentGrantLifetimeType = None, persistentGrantExpirationTime: int = None, persistentGrantExpirationTimeUnit: TimeUnit = None, persistentGrantIdleTimeoutType: PersistentGrantLifetimeType = None, persistentGrantIdleTimeout: int = None, persistentGrantIdleTimeoutTimeUnit: TimeUnit = None, clientCertIssuerType: ClientCertIssuerType = None, clientCertIssuerRef: ResourceLink = None, refreshRolling: RefreshRolling = None, refreshTokenRollingIntervalType: DeviceFlowSettingType = None, refreshTokenRollingInterval: int = None, oidcPolicy: ClientRegistrationOIDCPolicy = None, policyRefs: list = None, deviceFlowSettingType: DeviceFlowSettingType = None, userAuthorizationUrlOverride: str = None, pendingAuthorizationTimeoutOverride: int = None, devicePollingIntervalOverride: int = None, bypassActivationCodeConfirmationOverride: bool = None, requireProofKeyForCodeExchange: bool = None, cibaPollingInterval: int = None, cibaRequireSignedRequests: bool = None, requestPolicyRef: ResourceLink = None, tokenExchangeProcessorPolicyRef: ResourceLink = None, rotateClientSecret: bool = None, rotateRegistrationAccessToken: bool = None, allowClientDelete: bool = None, disableRegistrationAccessTokens: bool = None, refreshTokenRollingGracePeriodType: RefreshTokenRollingGracePeriodType = None, refreshTokenRollingGracePeriod: int = None, retainClientSecret: bool = None, clientSecretRetentionPeriodType: str = None, clientSecretRetentionPeriodOverride: int = None, requireJwtSecuredAuthorizationResponseMode: bool = None) -> None:
        self.initialAccessTokenScope = initialAccessTokenScope
        self.restrictCommonScopes = restrictCommonScopes
        self.restrictedCommonScopes = restrictedCommonScopes
        self.allowedExclusiveScopes = allowedExclusiveScopes
        self.enforceReplayPrevention = enforceReplayPrevention
        self.requireSignedRequests = requireSignedRequests
        self.defaultAccessTokenManagerRef = defaultAccessTokenManagerRef
        self.restrictToDefaultAccessTokenManager = restrictToDefaultAccessTokenManager
        self.persistentGrantExpirationType = persistentGrantExpirationType
        self.persistentGrantExpirationTime = persistentGrantExpirationTime
        self.persistentGrantExpirationTimeUnit = persistentGrantExpirationTimeUnit
        self.persistentGrantIdleTimeoutType = persistentGrantIdleTimeoutType
        self.persistentGrantIdleTimeout = persistentGrantIdleTimeout
        self.persistentGrantIdleTimeoutTimeUnit = persistentGrantIdleTimeoutTimeUnit
        self.clientCertIssuerType = clientCertIssuerType
        self.clientCertIssuerRef = clientCertIssuerRef
        self.refreshRolling = refreshRolling
        self.refreshTokenRollingIntervalType = refreshTokenRollingIntervalType
        self.refreshTokenRollingInterval = refreshTokenRollingInterval
        self.oidcPolicy = oidcPolicy
        self.policyRefs = policyRefs
        self.deviceFlowSettingType = deviceFlowSettingType
        self.userAuthorizationUrlOverride = userAuthorizationUrlOverride
        self.pendingAuthorizationTimeoutOverride = pendingAuthorizationTimeoutOverride
        self.devicePollingIntervalOverride = devicePollingIntervalOverride
        self.bypassActivationCodeConfirmationOverride = bypassActivationCodeConfirmationOverride
        self.requireProofKeyForCodeExchange = requireProofKeyForCodeExchange
        self.cibaPollingInterval = cibaPollingInterval
        self.cibaRequireSignedRequests = cibaRequireSignedRequests
        self.requestPolicyRef = requestPolicyRef
        self.tokenExchangeProcessorPolicyRef = tokenExchangeProcessorPolicyRef
        self.rotateClientSecret = rotateClientSecret
        self.rotateRegistrationAccessToken = rotateRegistrationAccessToken
        self.allowClientDelete = allowClientDelete
        self.disableRegistrationAccessTokens = disableRegistrationAccessTokens
        self.refreshTokenRollingGracePeriodType = refreshTokenRollingGracePeriodType
        self.refreshTokenRollingGracePeriod = refreshTokenRollingGracePeriod
        self.retainClientSecret = retainClientSecret
        self.clientSecretRetentionPeriodType = clientSecretRetentionPeriodType
        self.clientSecretRetentionPeriodOverride = clientSecretRetentionPeriodOverride
        self.requireJwtSecuredAuthorizationResponseMode = requireJwtSecuredAuthorizationResponseMode

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, DynamicClientRegistration):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.initialAccessTokenScope, self.restrictCommonScopes, self.restrictedCommonScopes, self.allowedExclusiveScopes, self.enforceReplayPrevention, self.requireSignedRequests, self.defaultAccessTokenManagerRef, self.restrictToDefaultAccessTokenManager, self.persistentGrantExpirationType, self.persistentGrantExpirationTime, self.persistentGrantExpirationTimeUnit, self.persistentGrantIdleTimeoutType, self.persistentGrantIdleTimeout, self.persistentGrantIdleTimeoutTimeUnit, self.clientCertIssuerType, self.clientCertIssuerRef, self.refreshRolling, self.refreshTokenRollingIntervalType, self.refreshTokenRollingInterval, self.oidcPolicy, self.policyRefs, self.deviceFlowSettingType, self.userAuthorizationUrlOverride, self.pendingAuthorizationTimeoutOverride, self.devicePollingIntervalOverride, self.bypassActivationCodeConfirmationOverride, self.requireProofKeyForCodeExchange, self.cibaPollingInterval, self.cibaRequireSignedRequests, self.requestPolicyRef, self.tokenExchangeProcessorPolicyRef, self.rotateClientSecret, self.rotateRegistrationAccessToken, self.allowClientDelete, self.disableRegistrationAccessTokens, self.refreshTokenRollingGracePeriodType, self.refreshTokenRollingGracePeriod, self.retainClientSecret, self.clientSecretRetentionPeriodType, self.clientSecretRetentionPeriodOverride, self.requireJwtSecuredAuthorizationResponseMode]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["initialAccessTokenScope", "restrictCommonScopes", "restrictedCommonScopes", "allowedExclusiveScopes", "enforceReplayPrevention", "requireSignedRequests", "defaultAccessTokenManagerRef", "restrictToDefaultAccessTokenManager", "persistentGrantExpirationType", "persistentGrantExpirationTime", "persistentGrantExpirationTimeUnit", "persistentGrantIdleTimeoutType", "persistentGrantIdleTimeout", "persistentGrantIdleTimeoutTimeUnit", "clientCertIssuerType", "clientCertIssuerRef", "refreshRolling", "refreshTokenRollingIntervalType", "refreshTokenRollingInterval", "oidcPolicy", "policyRefs", "deviceFlowSettingType", "userAuthorizationUrlOverride", "pendingAuthorizationTimeoutOverride", "devicePollingIntervalOverride", "bypassActivationCodeConfirmationOverride", "requireProofKeyForCodeExchange", "cibaPollingInterval", "cibaRequireSignedRequests", "requestPolicyRef", "tokenExchangeProcessorPolicyRef", "rotateClientSecret", "rotateRegistrationAccessToken", "allowClientDelete", "disableRegistrationAccessTokens", "refreshTokenRollingGracePeriodType", "refreshTokenRollingGracePeriod", "retainClientSecret", "clientSecretRetentionPeriodType", "clientSecretRetentionPeriodOverride", "requireJwtSecuredAuthorizationResponseMode"] and v is not None:
                if k == "initialAccessTokenScope":
                    valid_data[k] = str(v)
                if k == "restrictCommonScopes":
                    valid_data[k] = bool(v)
                if k == "restrictedCommonScopes":
                    valid_data[k] = [str(x) for x in v]
                if k == "allowedExclusiveScopes":
                    valid_data[k] = [str(x) for x in v]
                if k == "enforceReplayPrevention":
                    valid_data[k] = bool(v)
                if k == "requireSignedRequests":
                    valid_data[k] = bool(v)
                if k == "defaultAccessTokenManagerRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "restrictToDefaultAccessTokenManager":
                    valid_data[k] = bool(v)
                if k == "persistentGrantExpirationType":
                    valid_data[k] = PersistentGrantLifetimeType[v]
                if k == "persistentGrantExpirationTime":
                    valid_data[k] = int(v)
                if k == "persistentGrantExpirationTimeUnit":
                    valid_data[k] = TimeUnit[v]
                if k == "persistentGrantIdleTimeoutType":
                    valid_data[k] = PersistentGrantLifetimeType[v]
                if k == "persistentGrantIdleTimeout":
                    valid_data[k] = int(v)
                if k == "persistentGrantIdleTimeoutTimeUnit":
                    valid_data[k] = TimeUnit[v]
                if k == "clientCertIssuerType":
                    valid_data[k] = ClientCertIssuerType[v]
                if k == "clientCertIssuerRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "refreshRolling":
                    valid_data[k] = RefreshRolling[v]
                if k == "refreshTokenRollingIntervalType":
                    valid_data[k] = DeviceFlowSettingType[v]
                if k == "refreshTokenRollingInterval":
                    valid_data[k] = int(v)
                if k == "oidcPolicy":
                    valid_data[k] = ClientRegistrationOIDCPolicy.from_dict(v)
                if k == "policyRefs":
                    valid_data[k] = [ResourceLink.from_dict(x) for x in v]
                if k == "deviceFlowSettingType":
                    valid_data[k] = DeviceFlowSettingType[v]
                if k == "userAuthorizationUrlOverride":
                    valid_data[k] = str(v)
                if k == "pendingAuthorizationTimeoutOverride":
                    valid_data[k] = int(v)
                if k == "devicePollingIntervalOverride":
                    valid_data[k] = int(v)
                if k == "bypassActivationCodeConfirmationOverride":
                    valid_data[k] = bool(v)
                if k == "requireProofKeyForCodeExchange":
                    valid_data[k] = bool(v)
                if k == "cibaPollingInterval":
                    valid_data[k] = int(v)
                if k == "cibaRequireSignedRequests":
                    valid_data[k] = bool(v)
                if k == "requestPolicyRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "tokenExchangeProcessorPolicyRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "rotateClientSecret":
                    valid_data[k] = bool(v)
                if k == "rotateRegistrationAccessToken":
                    valid_data[k] = bool(v)
                if k == "allowClientDelete":
                    valid_data[k] = bool(v)
                if k == "disableRegistrationAccessTokens":
                    valid_data[k] = bool(v)
                if k == "refreshTokenRollingGracePeriodType":
                    valid_data[k] = RefreshTokenRollingGracePeriodType[v]
                if k == "refreshTokenRollingGracePeriod":
                    valid_data[k] = int(v)
                if k == "retainClientSecret":
                    valid_data[k] = bool(v)
                if k == "clientSecretRetentionPeriodType":
                    valid_data[k] = str(v)
                if k == "clientSecretRetentionPeriodOverride":
                    valid_data[k] = int(v)
                if k == "requireJwtSecuredAuthorizationResponseMode":
                    valid_data[k] = bool(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["initialAccessTokenScope", "restrictCommonScopes", "restrictedCommonScopes", "allowedExclusiveScopes", "enforceReplayPrevention", "requireSignedRequests", "defaultAccessTokenManagerRef", "restrictToDefaultAccessTokenManager", "persistentGrantExpirationType", "persistentGrantExpirationTime", "persistentGrantExpirationTimeUnit", "persistentGrantIdleTimeoutType", "persistentGrantIdleTimeout", "persistentGrantIdleTimeoutTimeUnit", "clientCertIssuerType", "clientCertIssuerRef", "refreshRolling", "refreshTokenRollingIntervalType", "refreshTokenRollingInterval", "oidcPolicy", "policyRefs", "deviceFlowSettingType", "userAuthorizationUrlOverride", "pendingAuthorizationTimeoutOverride", "devicePollingIntervalOverride", "bypassActivationCodeConfirmationOverride", "requireProofKeyForCodeExchange", "cibaPollingInterval", "cibaRequireSignedRequests", "requestPolicyRef", "tokenExchangeProcessorPolicyRef", "rotateClientSecret", "rotateRegistrationAccessToken", "allowClientDelete", "disableRegistrationAccessTokens", "refreshTokenRollingGracePeriodType", "refreshTokenRollingGracePeriod", "retainClientSecret", "clientSecretRetentionPeriodType", "clientSecretRetentionPeriodOverride", "requireJwtSecuredAuthorizationResponseMode"]:
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
