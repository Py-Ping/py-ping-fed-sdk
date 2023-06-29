from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.models.jwks_settings import JwksSettings
from pingfedsdk.models.client_auth import ClientAuth
from pingfedsdk.models.client_o_i_d_c_policy import ClientOIDCPolicy
from pingfedsdk.enums import TokenIntrospectionSigningAlgorithm
from pingfedsdk.enums import RefreshTokenRollingGracePeriodType
from pingfedsdk.enums import PersistentGrantLifetimeType
from pingfedsdk.enums import RefreshRolling
from pingfedsdk.enums import ObjectSigningAlgorithm
from pingfedsdk.enums import JwtSecuredAuthorizationResponseModeEncryptionAlgorithm
from pingfedsdk.enums import JwtSecuredAuthorizationResponseModeContentEncryptionAlgorithm
from pingfedsdk.enums import ClientSecretRetentionPeriodType
from pingfedsdk.enums import TokenIntrospectionContentEncryptionAlgorithm
from pingfedsdk.enums import TimeUnit
from pingfedsdk.enums import JwtSecuredAuthorizationResponseModeSigningAlgorithm
from pingfedsdk.enums import CibaDeliveryMode
from pingfedsdk.enums import DeviceFlowSettingType
from pingfedsdk.enums import TokenIntrospectionEncryptionAlgorithm


class Client(Model):
    """OAuth client.

    Attributes
    ----------
    clientId: str
        A unique identifier the client provides to the Resource Server to identify itself. This identifier is included with every request the client makes. For PUT requests, this field is optional and it will be overridden by the 'id' parameter of the PUT request.

    enabled: bool
        Specifies whether the client is enabled. The default value is true.

    redirectUris: list
        URIs to which the OAuth AS may redirect the resource owner's user agent after authorization is obtained. A redirection URI is used with the Authorization Code and Implicit grant types. Wildcards are allowed. However, for security reasons, make the URL as restrictive as possible.For example: https://*.company.com/* Important: If more than one URI is added or if a single URI uses wildcards, then Authorization Code grant and token requests must contain a specific matching redirect uri parameter.

    grantTypes: list
        The grant types allowed for this client. The EXTENSION grant type applies to SAML/JWT assertion grants.

    name: str
        A descriptive name for the client instance. This name appears when the user is prompted for authorization.

    description: str
        A description of what the client application does. This description appears when the user is prompted for authorization.

    logoUrl: str
        The location of the logo used on user-facing OAuth grant authorization and revocation pages.

    defaultAccessTokenManagerRef: ResourceLink
        The default access token manager for this client.

    restrictToDefaultAccessTokenManager: bool
        Determines whether the client is restricted to using only its default access token manager. The default is false.

    validateUsingAllEligibleAtms: bool
        Validates token using all eligible access token managers for the client. This setting is ignored if 'restrictToDefaultAccessTokenManager' is set to true.

    refreshRolling: RefreshRolling
        Use ROLL or DONT_ROLL to override the Roll Refresh Token Values setting on the Authorization Server Settings. SERVER_DEFAULT will default to the Roll Refresh Token Values setting on the Authorization Server Setting screen. Defaults to SERVER_DEFAULT.

    refreshTokenRollingIntervalType: DeviceFlowSettingType
        Use OVERRIDE_SERVER_DEFAULT to override the Refresh Token Rolling Interval value on the Authorization Server Settings. SERVER_DEFAULT will default to the Refresh Token Rolling Interval value on the Authorization Server Setting. Defaults to SERVER_DEFAULT.

    refreshTokenRollingInterval: int
        The minimum interval to roll refresh tokens, in hours. This value will override the Refresh Token Rolling Interval Value on the Authorization Server Settings.

    persistentGrantExpirationType: PersistentGrantLifetimeType
        Allows an administrator to override the Persistent Grant Lifetime set globally for the OAuth AS. Defaults to SERVER_DEFAULT.

    persistentGrantExpirationTime: int
        The persistent grant expiration time. -1 indicates an indefinite amount of time.

    persistentGrantExpirationTimeUnit: TimeUnit
        The persistent grant expiration time unit.

    persistentGrantIdleTimeoutType: PersistentGrantLifetimeType
        Allows an administrator to override the Persistent Grant Idle Timeout set globally for the OAuth AS. Defaults to SERVER_DEFAULT.

    persistentGrantIdleTimeout: int
        The persistent grant idle timeout.

    persistentGrantIdleTimeoutTimeUnit: TimeUnit
        The persistent grant idle timeout time unit.

    persistentGrantReuseType: DeviceFlowSettingType
        Allows and administrator to override the Reuse Existing Persistent Access Grants for Grant Types set globally for OAuth AS. Defaults to SERVER_DEFAULT.

    persistentGrantReuseGrantTypes: list
        The grant types that the OAuth AS can reuse rather than creating a new grant for each request. This value will override the Reuse Existing Persistent Access Grants for Grant Types on the Authorization Server Settings. Only 'IMPLICIT' or 'AUTHORIZATION_CODE' or 'RESOURCE_OWNER_CREDENTIALS' are valid grant types.

    allowAuthenticationApiInit: bool
        Set to true to allow this client to initiate the authentication API redirectless flow.

    bypassApprovalPage: bool
        Use this setting, for example, when you want to deploy a trusted application and authenticate end users via an IdP adapter or IdP connection.

    restrictScopes: bool
        Restricts this client's access to specific scopes.

    restrictedScopes: list
        The scopes available for this client.

    exclusiveScopes: list
        The exclusive scopes available for this client.

    restrictedResponseTypes: list
        The response types allowed for this client. If omitted all response types are available to the client.

    requirePushedAuthorizationRequests: bool
        Determines whether pushed authorization requests are required when initiating an authorization request. The default is false.

    requireJwtSecuredAuthorizationResponseMode: bool
        Determines whether JWT Secured authorization response mode is required when initiating an authorization request. The default is false.

    requireSignedRequests: bool
        Determines whether signed requests are required for this client

    requestObjectSigningAlgorithm: ObjectSigningAlgorithm
        The JSON Web Signature [JWS] algorithm that must be used to sign the Request Object. All signing algorithms are allowed if value is not present
        RS256 - RSA using SHA-256
        RS384 - RSA using SHA-384
        RS512 - RSA using SHA-512
        ES256 - ECDSA using P256 Curve and SHA-256
        ES384 - ECDSA using P384 Curve and SHA-384
        ES512 - ECDSA using P521 Curve and SHA-512
        PS256 - RSASSA-PSS using SHA-256 and MGF1 padding with SHA-256
        PS384 - RSASSA-PSS using SHA-384 and MGF1 padding with SHA-384
        PS512 - RSASSA-PSS using SHA-512 and MGF1 padding with SHA-512
        RSASSA-PSS is only supported with SafeNet Luna, Thales nCipher or Java 11.

    oidcPolicy: ClientOIDCPolicy
        Open ID Connect Policy settings.  This is included in the message only when OIDC is enabled.

    clientAuth: ClientAuth
        Client authentication settings.  If this model is null, it indicates that no client authentication will be used.

    jwksSettings: JwksSettings
        JSON Web Key Set Settings of the OAuth client. Required if private key JWT client authentication or signed requests is enabled.

    extendedParameters: object
        OAuth Client Metadata can be extended to use custom Client Metadata Parameters. The names of these custom parameters should be defined in /extendedProperties.

    deviceFlowSettingType: DeviceFlowSettingType
        Allows an administrator to override the Device Authorization Settings set globally for the OAuth AS. Defaults to SERVER_DEFAULT.

    userAuthorizationUrlOverride: str
        The URL used as 'verification_url' and 'verification_url_complete' values in a Device Authorization request. This property overrides the 'userAuthorizationUrl' value present in Authorization Server Settings.

    pendingAuthorizationTimeoutOverride: int
        The 'device_code' and 'user_code' timeout, in seconds. This overrides the 'pendingAuthorizationTimeout' value present in Authorization Server Settings.

    devicePollingIntervalOverride: int
        The amount of time client should wait between polling requests, in seconds. This overrides the 'devicePollingInterval' value present in Authorization Server Settings.

    bypassActivationCodeConfirmationOverride: bool
        Indicates if the Activation Code Confirmation page should be bypassed if 'verification_url_complete' is used by the end user to authorize a device. This overrides the 'bypassUseCodeConfirmation' value present in Authorization Server Settings.

    requireProofKeyForCodeExchange: bool
        Determines whether Proof Key for Code Exchange (PKCE) is required for this client.

    cibaDeliveryMode: CibaDeliveryMode
        The token delivery mode for the client.  The default value is 'POLL'.

    cibaNotificationEndpoint: str
        The endpoint the OP will call after a successful or failed end-user authentication.

    cibaPollingInterval: int
        The minimum amount of time in seconds that the Client must wait between polling requests to the token endpoint. The default is 3 seconds.

    cibaRequireSignedRequests: bool
        Determines whether CIBA signed requests are required for this client.

    cibaRequestObjectSigningAlgorithm: ObjectSigningAlgorithm
        The JSON Web Signature [JWS] algorithm that must be used to sign the CIBA Request Object. All signing algorithms are allowed if value is not present
        RS256 - RSA using SHA-256
        RS384 - RSA using SHA-384
        RS512 - RSA using SHA-512
        ES256 - ECDSA using P256 Curve and SHA-256
        ES384 - ECDSA using P384 Curve and SHA-384
        ES512 - ECDSA using P521 Curve and SHA-512
        PS256 - RSASSA-PSS using SHA-256 and MGF1 padding with SHA-256
        PS384 - RSASSA-PSS using SHA-384 and MGF1 padding with SHA-384
        PS512 - RSASSA-PSS using SHA-512 and MGF1 padding with SHA-512
        RSASSA-PSS is only supported with SafeNet Luna, Thales nCipher or Java 11.

    cibaUserCodeSupported: bool
        Determines whether CIBA user code is supported for this client.

    requestPolicyRef: ResourceLink
        The CIBA request policy.

    tokenExchangeProcessorPolicyRef: ResourceLink
        The Token Exchange Processor policy.

    refreshTokenRollingGracePeriodType: RefreshTokenRollingGracePeriodType
        When specified, it overrides the global Refresh Token Grace Period defined in the Authorization Server Settings. The default value is SERVER_DEFAULT

    refreshTokenRollingGracePeriod: int
        The grace period that a rolled refresh token remains valid in seconds.

    clientSecretRetentionPeriodType: ClientSecretRetentionPeriodType
        Use OVERRIDE_SERVER_DEFAULT to override the Client Secret Retention Period value on the Authorization Server Settings. SERVER_DEFAULT will default to the Client Secret Retention Period value on the Authorization Server Setting. Defaults to SERVER_DEFAULT.

    clientSecretRetentionPeriod: int
        The length of time in minutes that client secrets will be retained as secondary secrets after secret change. The default value is 0, which will disable secondary client secret retention. This value will override the Client Secret Retention Period value on the Authorization Server Settings.

    clientSecretChangedTime: str
        The time at which the client secret was last changed. This property is read only and is ignored on PUT and POST requests.

    tokenIntrospectionSigningAlgorithm: TokenIntrospectionSigningAlgorithm
        The JSON Web Signature [JWS] algorithm required to sign the Token Introspection Response.
        HS256 - HMAC using SHA-256
        HS384 - HMAC using SHA-384
        HS512 - HMAC using SHA-512
        RS256 - RSA using SHA-256
        RS384 - RSA using SHA-384
        RS512 - RSA using SHA-512
        ES256 - ECDSA using P256 Curve and SHA-256
        ES384 - ECDSA using P384 Curve and SHA-384
        ES512 - ECDSA using P521 Curve and SHA-512
        PS256 - RSASSA-PSS using SHA-256 and MGF1 padding with SHA-256
        PS384 - RSASSA-PSS using SHA-384 and MGF1 padding with SHA-384
        PS512 - RSASSA-PSS using SHA-512 and MGF1 padding with SHA-512
        A null value will represent the default algorithm which is RS256.
        RSASSA-PSS is only supported with SafeNet Luna, Thales nCipher or Java 11

    tokenIntrospectionEncryptionAlgorithm: TokenIntrospectionEncryptionAlgorithm
        The JSON Web Encryption [JWE] encryption algorithm used to encrypt the content-encryption key of the Token Introspection Response.
        DIR - Direct Encryption with symmetric key
        A128KW - AES-128 Key Wrap
        A192KW - AES-192 Key Wrap
        A256KW - AES-256 Key Wrap
        A128GCMKW - AES-GCM-128 key encryption
        A192GCMKW - AES-GCM-192 key encryption
        A256GCMKW - AES-GCM-256 key encryption
        ECDH_ES - ECDH-ES
        ECDH_ES_A128KW - ECDH-ES with AES-128 Key Wrap
        ECDH_ES_A192KW - ECDH-ES with AES-192 Key Wrap
        ECDH_ES_A256KW - ECDH-ES with AES-256 Key Wrap
        RSA_OAEP - RSAES OAEP
        RSA_OAEP_256 - RSAES OAEP using SHA-256 and MGF1 with SHA-256

    tokenIntrospectionContentEncryptionAlgorithm: TokenIntrospectionContentEncryptionAlgorithm
        The JSON Web Encryption [JWE] content-encryption algorithm for the Token Introspection Response.
        AES_128_CBC_HMAC_SHA_256 - Composite AES-CBC-128 HMAC-SHA-256
        AES_192_CBC_HMAC_SHA_384 - Composite AES-CBC-192 HMAC-SHA-384
        AES_256_CBC_HMAC_SHA_512 - Composite AES-CBC-256 HMAC-SHA-512
        AES_128_GCM - AES-GCM-128
        AES_192_GCM - AES-GCM-192
        AES_256_GCM - AES-GCM-256

    jwtSecuredAuthorizationResponseModeSigningAlgorithm: JwtSecuredAuthorizationResponseModeSigningAlgorithm
        The JSON Web Signature [JWS] algorithm required to sign the JWT Secured Authorization Response.
        HS256 - HMAC using SHA-256
        HS384 - HMAC using SHA-384
        HS512 - HMAC using SHA-512
        RS256 - RSA using SHA-256
        RS384 - RSA using SHA-384
        RS512 - RSA using SHA-512
        ES256 - ECDSA using P256 Curve and SHA-256
        ES384 - ECDSA using P384 Curve and SHA-384
        ES512 - ECDSA using P521 Curve and SHA-512
        PS256 - RSASSA-PSS using SHA-256 and MGF1 padding with SHA-256
        PS384 - RSASSA-PSS using SHA-384 and MGF1 padding with SHA-384
        PS512 - RSASSA-PSS using SHA-512 and MGF1 padding with SHA-512
        A null value will represent the default algorithm which is RS256.
        RSASSA-PSS is only supported with SafeNet Luna, Thales nCipher or Java 11

    jwtSecuredAuthorizationResponseModeEncryptionAlgorithm: JwtSecuredAuthorizationResponseModeEncryptionAlgorithm
        The JSON Web Encryption [JWE] encryption algorithm used to encrypt the content-encryption key of the JWT Secured Authorization Response.
        DIR - Direct Encryption with symmetric key
        A128KW - AES-128 Key Wrap
        A192KW - AES-192 Key Wrap
        A256KW - AES-256 Key Wrap
        A128GCMKW - AES-GCM-128 key encryption
        A192GCMKW - AES-GCM-192 key encryption
        A256GCMKW - AES-GCM-256 key encryption
        ECDH_ES - ECDH-ES
        ECDH_ES_A128KW - ECDH-ES with AES-128 Key Wrap
        ECDH_ES_A192KW - ECDH-ES with AES-192 Key Wrap
        ECDH_ES_A256KW - ECDH-ES with AES-256 Key Wrap
        RSA_OAEP - RSAES OAEP
        RSA_OAEP_256 - RSAES OAEP using SHA-256 and MGF1 with SHA-256

    jwtSecuredAuthorizationResponseModeContentEncryptionAlgorithm: JwtSecuredAuthorizationResponseModeContentEncryptionAlgorithm
        The JSON Web Encryption [JWE] content-encryption algorithm for the JWT Secured Authorization Response.
        AES_128_CBC_HMAC_SHA_256 - Composite AES-CBC-128 HMAC-SHA-256
        AES_192_CBC_HMAC_SHA_384 - Composite AES-CBC-192 HMAC-SHA-384
        AES_256_CBC_HMAC_SHA_512 - Composite AES-CBC-256 HMAC-SHA-512
        AES_128_GCM - AES-GCM-128
        AES_192_GCM - AES-GCM-192
        AES_256_GCM - AES-GCM-256

    """

    def __init__(self, clientId: str, grantTypes: list, name: str, enabled: bool = None, redirectUris: list = None, description: str = None, logoUrl: str = None, defaultAccessTokenManagerRef: ResourceLink = None, restrictToDefaultAccessTokenManager: bool = None, validateUsingAllEligibleAtms: bool = None, refreshRolling: RefreshRolling = None, refreshTokenRollingIntervalType: DeviceFlowSettingType = None, refreshTokenRollingInterval: int = None, persistentGrantExpirationType: PersistentGrantLifetimeType = None, persistentGrantExpirationTime: int = None, persistentGrantExpirationTimeUnit: TimeUnit = None, persistentGrantIdleTimeoutType: PersistentGrantLifetimeType = None, persistentGrantIdleTimeout: int = None, persistentGrantIdleTimeoutTimeUnit: TimeUnit = None, persistentGrantReuseType: DeviceFlowSettingType = None, persistentGrantReuseGrantTypes: list = None, allowAuthenticationApiInit: bool = None, bypassApprovalPage: bool = None, restrictScopes: bool = None, restrictedScopes: list = None, exclusiveScopes: list = None, restrictedResponseTypes: list = None, requirePushedAuthorizationRequests: bool = None, requireJwtSecuredAuthorizationResponseMode: bool = None, requireSignedRequests: bool = None, requestObjectSigningAlgorithm: ObjectSigningAlgorithm = None, oidcPolicy: ClientOIDCPolicy = None, clientAuth: ClientAuth = None, jwksSettings: JwksSettings = None, extendedParameters: object = None, deviceFlowSettingType: DeviceFlowSettingType = None, userAuthorizationUrlOverride: str = None, pendingAuthorizationTimeoutOverride: int = None, devicePollingIntervalOverride: int = None, bypassActivationCodeConfirmationOverride: bool = None, requireProofKeyForCodeExchange: bool = None, cibaDeliveryMode: CibaDeliveryMode = None, cibaNotificationEndpoint: str = None, cibaPollingInterval: int = None, cibaRequireSignedRequests: bool = None, cibaRequestObjectSigningAlgorithm: ObjectSigningAlgorithm = None, cibaUserCodeSupported: bool = None, requestPolicyRef: ResourceLink = None, tokenExchangeProcessorPolicyRef: ResourceLink = None, refreshTokenRollingGracePeriodType: RefreshTokenRollingGracePeriodType = None, refreshTokenRollingGracePeriod: int = None, clientSecretRetentionPeriodType: ClientSecretRetentionPeriodType = None, clientSecretRetentionPeriod: int = None, clientSecretChangedTime: str = None, tokenIntrospectionSigningAlgorithm: TokenIntrospectionSigningAlgorithm = None, tokenIntrospectionEncryptionAlgorithm: TokenIntrospectionEncryptionAlgorithm = None, tokenIntrospectionContentEncryptionAlgorithm: TokenIntrospectionContentEncryptionAlgorithm = None, jwtSecuredAuthorizationResponseModeSigningAlgorithm: JwtSecuredAuthorizationResponseModeSigningAlgorithm = None, jwtSecuredAuthorizationResponseModeEncryptionAlgorithm: JwtSecuredAuthorizationResponseModeEncryptionAlgorithm = None, jwtSecuredAuthorizationResponseModeContentEncryptionAlgorithm: JwtSecuredAuthorizationResponseModeContentEncryptionAlgorithm = None) -> None:
        self.clientId = clientId
        self.enabled = enabled
        self.redirectUris = redirectUris
        self.grantTypes = grantTypes
        self.name = name
        self.description = description
        self.logoUrl = logoUrl
        self.defaultAccessTokenManagerRef = defaultAccessTokenManagerRef
        self.restrictToDefaultAccessTokenManager = restrictToDefaultAccessTokenManager
        self.validateUsingAllEligibleAtms = validateUsingAllEligibleAtms
        self.refreshRolling = refreshRolling
        self.refreshTokenRollingIntervalType = refreshTokenRollingIntervalType
        self.refreshTokenRollingInterval = refreshTokenRollingInterval
        self.persistentGrantExpirationType = persistentGrantExpirationType
        self.persistentGrantExpirationTime = persistentGrantExpirationTime
        self.persistentGrantExpirationTimeUnit = persistentGrantExpirationTimeUnit
        self.persistentGrantIdleTimeoutType = persistentGrantIdleTimeoutType
        self.persistentGrantIdleTimeout = persistentGrantIdleTimeout
        self.persistentGrantIdleTimeoutTimeUnit = persistentGrantIdleTimeoutTimeUnit
        self.persistentGrantReuseType = persistentGrantReuseType
        self.persistentGrantReuseGrantTypes = persistentGrantReuseGrantTypes
        self.allowAuthenticationApiInit = allowAuthenticationApiInit
        self.bypassApprovalPage = bypassApprovalPage
        self.restrictScopes = restrictScopes
        self.restrictedScopes = restrictedScopes
        self.exclusiveScopes = exclusiveScopes
        self.restrictedResponseTypes = restrictedResponseTypes
        self.requirePushedAuthorizationRequests = requirePushedAuthorizationRequests
        self.requireJwtSecuredAuthorizationResponseMode = requireJwtSecuredAuthorizationResponseMode
        self.requireSignedRequests = requireSignedRequests
        self.requestObjectSigningAlgorithm = requestObjectSigningAlgorithm
        self.oidcPolicy = oidcPolicy
        self.clientAuth = clientAuth
        self.jwksSettings = jwksSettings
        self.extendedParameters = extendedParameters
        self.deviceFlowSettingType = deviceFlowSettingType
        self.userAuthorizationUrlOverride = userAuthorizationUrlOverride
        self.pendingAuthorizationTimeoutOverride = pendingAuthorizationTimeoutOverride
        self.devicePollingIntervalOverride = devicePollingIntervalOverride
        self.bypassActivationCodeConfirmationOverride = bypassActivationCodeConfirmationOverride
        self.requireProofKeyForCodeExchange = requireProofKeyForCodeExchange
        self.cibaDeliveryMode = cibaDeliveryMode
        self.cibaNotificationEndpoint = cibaNotificationEndpoint
        self.cibaPollingInterval = cibaPollingInterval
        self.cibaRequireSignedRequests = cibaRequireSignedRequests
        self.cibaRequestObjectSigningAlgorithm = cibaRequestObjectSigningAlgorithm
        self.cibaUserCodeSupported = cibaUserCodeSupported
        self.requestPolicyRef = requestPolicyRef
        self.tokenExchangeProcessorPolicyRef = tokenExchangeProcessorPolicyRef
        self.refreshTokenRollingGracePeriodType = refreshTokenRollingGracePeriodType
        self.refreshTokenRollingGracePeriod = refreshTokenRollingGracePeriod
        self.clientSecretRetentionPeriodType = clientSecretRetentionPeriodType
        self.clientSecretRetentionPeriod = clientSecretRetentionPeriod
        self.clientSecretChangedTime = clientSecretChangedTime
        self.tokenIntrospectionSigningAlgorithm = tokenIntrospectionSigningAlgorithm
        self.tokenIntrospectionEncryptionAlgorithm = tokenIntrospectionEncryptionAlgorithm
        self.tokenIntrospectionContentEncryptionAlgorithm = tokenIntrospectionContentEncryptionAlgorithm
        self.jwtSecuredAuthorizationResponseModeSigningAlgorithm = jwtSecuredAuthorizationResponseModeSigningAlgorithm
        self.jwtSecuredAuthorizationResponseModeEncryptionAlgorithm = jwtSecuredAuthorizationResponseModeEncryptionAlgorithm
        self.jwtSecuredAuthorizationResponseModeContentEncryptionAlgorithm = jwtSecuredAuthorizationResponseModeContentEncryptionAlgorithm

    def _validate(self) -> bool:
        return any(x for x in ["clientId", "grantTypes", "name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, Client):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.clientId, self.enabled, self.redirectUris, self.grantTypes, self.name, self.description, self.logoUrl, self.defaultAccessTokenManagerRef, self.restrictToDefaultAccessTokenManager, self.validateUsingAllEligibleAtms, self.refreshRolling, self.refreshTokenRollingIntervalType, self.refreshTokenRollingInterval, self.persistentGrantExpirationType, self.persistentGrantExpirationTime, self.persistentGrantExpirationTimeUnit, self.persistentGrantIdleTimeoutType, self.persistentGrantIdleTimeout, self.persistentGrantIdleTimeoutTimeUnit, self.persistentGrantReuseType, self.persistentGrantReuseGrantTypes, self.allowAuthenticationApiInit, self.bypassApprovalPage, self.restrictScopes, self.restrictedScopes, self.exclusiveScopes, self.restrictedResponseTypes, self.requirePushedAuthorizationRequests, self.requireJwtSecuredAuthorizationResponseMode, self.requireSignedRequests, self.requestObjectSigningAlgorithm, self.oidcPolicy, self.clientAuth, self.jwksSettings, self.extendedParameters, self.deviceFlowSettingType, self.userAuthorizationUrlOverride, self.pendingAuthorizationTimeoutOverride, self.devicePollingIntervalOverride, self.bypassActivationCodeConfirmationOverride, self.requireProofKeyForCodeExchange, self.cibaDeliveryMode, self.cibaNotificationEndpoint, self.cibaPollingInterval, self.cibaRequireSignedRequests, self.cibaRequestObjectSigningAlgorithm, self.cibaUserCodeSupported, self.requestPolicyRef, self.tokenExchangeProcessorPolicyRef, self.refreshTokenRollingGracePeriodType, self.refreshTokenRollingGracePeriod, self.clientSecretRetentionPeriodType, self.clientSecretRetentionPeriod, self.clientSecretChangedTime, self.tokenIntrospectionSigningAlgorithm, self.tokenIntrospectionEncryptionAlgorithm, self.tokenIntrospectionContentEncryptionAlgorithm, self.jwtSecuredAuthorizationResponseModeSigningAlgorithm, self.jwtSecuredAuthorizationResponseModeEncryptionAlgorithm, self.jwtSecuredAuthorizationResponseModeContentEncryptionAlgorithm]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["clientId", "enabled", "redirectUris", "grantTypes", "name", "description", "logoUrl", "defaultAccessTokenManagerRef", "restrictToDefaultAccessTokenManager", "validateUsingAllEligibleAtms", "refreshRolling", "refreshTokenRollingIntervalType", "refreshTokenRollingInterval", "persistentGrantExpirationType", "persistentGrantExpirationTime", "persistentGrantExpirationTimeUnit", "persistentGrantIdleTimeoutType", "persistentGrantIdleTimeout", "persistentGrantIdleTimeoutTimeUnit", "persistentGrantReuseType", "persistentGrantReuseGrantTypes", "allowAuthenticationApiInit", "bypassApprovalPage", "restrictScopes", "restrictedScopes", "exclusiveScopes", "restrictedResponseTypes", "requirePushedAuthorizationRequests", "requireJwtSecuredAuthorizationResponseMode", "requireSignedRequests", "requestObjectSigningAlgorithm", "oidcPolicy", "clientAuth", "jwksSettings", "extendedParameters", "deviceFlowSettingType", "userAuthorizationUrlOverride", "pendingAuthorizationTimeoutOverride", "devicePollingIntervalOverride", "bypassActivationCodeConfirmationOverride", "requireProofKeyForCodeExchange", "cibaDeliveryMode", "cibaNotificationEndpoint", "cibaPollingInterval", "cibaRequireSignedRequests", "cibaRequestObjectSigningAlgorithm", "cibaUserCodeSupported", "requestPolicyRef", "tokenExchangeProcessorPolicyRef", "refreshTokenRollingGracePeriodType", "refreshTokenRollingGracePeriod", "clientSecretRetentionPeriodType", "clientSecretRetentionPeriod", "clientSecretChangedTime", "tokenIntrospectionSigningAlgorithm", "tokenIntrospectionEncryptionAlgorithm", "tokenIntrospectionContentEncryptionAlgorithm", "jwtSecuredAuthorizationResponseModeSigningAlgorithm", "jwtSecuredAuthorizationResponseModeEncryptionAlgorithm", "jwtSecuredAuthorizationResponseModeContentEncryptionAlgorithm"] and v is not None:
                if k == "clientId":
                    valid_data[k] = str(v)
                if k == "enabled":
                    valid_data[k] = bool(v)
                if k == "redirectUris":
                    valid_data[k] = [str(x) for x in v]
                if k == "grantTypes":
                    valid_data[k] = [str(x) for x in v]
                if k == "name":
                    valid_data[k] = str(v)
                if k == "description":
                    valid_data[k] = str(v)
                if k == "logoUrl":
                    valid_data[k] = str(v)
                if k == "defaultAccessTokenManagerRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "restrictToDefaultAccessTokenManager":
                    valid_data[k] = bool(v)
                if k == "validateUsingAllEligibleAtms":
                    valid_data[k] = bool(v)
                if k == "refreshRolling":
                    valid_data[k] = RefreshRolling[v]
                if k == "refreshTokenRollingIntervalType":
                    valid_data[k] = DeviceFlowSettingType[v]
                if k == "refreshTokenRollingInterval":
                    valid_data[k] = int(v)
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
                if k == "persistentGrantReuseType":
                    valid_data[k] = DeviceFlowSettingType[v]
                if k == "persistentGrantReuseGrantTypes":
                    valid_data[k] = [str(x) for x in v]
                if k == "allowAuthenticationApiInit":
                    valid_data[k] = bool(v)
                if k == "bypassApprovalPage":
                    valid_data[k] = bool(v)
                if k == "restrictScopes":
                    valid_data[k] = bool(v)
                if k == "restrictedScopes":
                    valid_data[k] = [str(x) for x in v]
                if k == "exclusiveScopes":
                    valid_data[k] = [str(x) for x in v]
                if k == "restrictedResponseTypes":
                    valid_data[k] = [str(x) for x in v]
                if k == "requirePushedAuthorizationRequests":
                    valid_data[k] = bool(v)
                if k == "requireJwtSecuredAuthorizationResponseMode":
                    valid_data[k] = bool(v)
                if k == "requireSignedRequests":
                    valid_data[k] = bool(v)
                if k == "requestObjectSigningAlgorithm":
                    valid_data[k] = ObjectSigningAlgorithm[v]
                if k == "oidcPolicy":
                    valid_data[k] = ClientOIDCPolicy(**v)
                if k == "clientAuth":
                    valid_data[k] = ClientAuth(**v)
                if k == "jwksSettings":
                    valid_data[k] = JwksSettings(**v)
                if k == "extendedParameters":
                    valid_data[k] = object(**v)
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
                if k == "cibaDeliveryMode":
                    valid_data[k] = CibaDeliveryMode[v]
                if k == "cibaNotificationEndpoint":
                    valid_data[k] = str(v)
                if k == "cibaPollingInterval":
                    valid_data[k] = int(v)
                if k == "cibaRequireSignedRequests":
                    valid_data[k] = bool(v)
                if k == "cibaRequestObjectSigningAlgorithm":
                    valid_data[k] = ObjectSigningAlgorithm[v]
                if k == "cibaUserCodeSupported":
                    valid_data[k] = bool(v)
                if k == "requestPolicyRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "tokenExchangeProcessorPolicyRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "refreshTokenRollingGracePeriodType":
                    valid_data[k] = RefreshTokenRollingGracePeriodType[v]
                if k == "refreshTokenRollingGracePeriod":
                    valid_data[k] = int(v)
                if k == "clientSecretRetentionPeriodType":
                    valid_data[k] = ClientSecretRetentionPeriodType[v]
                if k == "clientSecretRetentionPeriod":
                    valid_data[k] = int(v)
                if k == "clientSecretChangedTime":
                    valid_data[k] = str(v)
                if k == "tokenIntrospectionSigningAlgorithm":
                    valid_data[k] = TokenIntrospectionSigningAlgorithm[v]
                if k == "tokenIntrospectionEncryptionAlgorithm":
                    valid_data[k] = TokenIntrospectionEncryptionAlgorithm[v]
                if k == "tokenIntrospectionContentEncryptionAlgorithm":
                    valid_data[k] = TokenIntrospectionContentEncryptionAlgorithm[v]
                if k == "jwtSecuredAuthorizationResponseModeSigningAlgorithm":
                    valid_data[k] = JwtSecuredAuthorizationResponseModeSigningAlgorithm[v]
                if k == "jwtSecuredAuthorizationResponseModeEncryptionAlgorithm":
                    valid_data[k] = JwtSecuredAuthorizationResponseModeEncryptionAlgorithm[v]
                if k == "jwtSecuredAuthorizationResponseModeContentEncryptionAlgorithm":
                    valid_data[k] = JwtSecuredAuthorizationResponseModeContentEncryptionAlgorithm[v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["clientId", "enabled", "redirectUris", "grantTypes", "name", "description", "logoUrl", "defaultAccessTokenManagerRef", "restrictToDefaultAccessTokenManager", "validateUsingAllEligibleAtms", "refreshRolling", "refreshTokenRollingIntervalType", "refreshTokenRollingInterval", "persistentGrantExpirationType", "persistentGrantExpirationTime", "persistentGrantExpirationTimeUnit", "persistentGrantIdleTimeoutType", "persistentGrantIdleTimeout", "persistentGrantIdleTimeoutTimeUnit", "persistentGrantReuseType", "persistentGrantReuseGrantTypes", "allowAuthenticationApiInit", "bypassApprovalPage", "restrictScopes", "restrictedScopes", "exclusiveScopes", "restrictedResponseTypes", "requirePushedAuthorizationRequests", "requireJwtSecuredAuthorizationResponseMode", "requireSignedRequests", "requestObjectSigningAlgorithm", "oidcPolicy", "clientAuth", "jwksSettings", "extendedParameters", "deviceFlowSettingType", "userAuthorizationUrlOverride", "pendingAuthorizationTimeoutOverride", "devicePollingIntervalOverride", "bypassActivationCodeConfirmationOverride", "requireProofKeyForCodeExchange", "cibaDeliveryMode", "cibaNotificationEndpoint", "cibaPollingInterval", "cibaRequireSignedRequests", "cibaRequestObjectSigningAlgorithm", "cibaUserCodeSupported", "requestPolicyRef", "tokenExchangeProcessorPolicyRef", "refreshTokenRollingGracePeriodType", "refreshTokenRollingGracePeriod", "clientSecretRetentionPeriodType", "clientSecretRetentionPeriod", "clientSecretChangedTime", "tokenIntrospectionSigningAlgorithm", "tokenIntrospectionEncryptionAlgorithm", "tokenIntrospectionContentEncryptionAlgorithm", "jwtSecuredAuthorizationResponseModeSigningAlgorithm", "jwtSecuredAuthorizationResponseModeEncryptionAlgorithm", "jwtSecuredAuthorizationResponseModeContentEncryptionAlgorithm"]:
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
