from enum import Enum, auto


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class DataStoreType(AutoName):
    LDAP = auto()
    PING_ONE_LDAP_GATEWAY = auto()
    JDBC = auto()
    CUSTOM = auto()


class BinaryEncoding(AutoName):
    BASE64 = auto()
    HEX = auto()
    SID = auto()


class Condition(AutoName):
    EQUALS = auto()
    EQUALS_CASE_INSENSITIVE = auto()
    EQUALS_DN = auto()
    NOT_EQUAL = auto()
    NOT_EQUAL_CASE_INSENSITIVE = auto()
    NOT_EQUAL_DN = auto()
    MULTIVALUE_CONTAINS = auto()
    MULTIVALUE_CONTAINS_CASE_INSENSITIVE = auto()
    MULTIVALUE_CONTAINS_DN = auto()
    MULTIVALUE_DOES_NOT_CONTAIN = auto()
    MULTIVALUE_DOES_NOT_CONTAIN_CASE_INSENSITIVE = auto()
    MULTIVALUE_DOES_NOT_CONTAIN_DN = auto()


class SearchScope(AutoName):
    OBJECT = auto()
    ONE_LEVEL = auto()
    SUBTREE = auto()


class SourceTypeIdKeyType(AutoName):
    TOKEN_EXCHANGE_PROCESSOR_POLICY = auto()
    ACCOUNT_LINK = auto()
    ADAPTER = auto()
    ASSERTION = auto()
    CONTEXT = auto()
    CUSTOM_DATA_STORE = auto()
    EXPRESSION = auto()
    JDBC_DATA_STORE = auto()
    LDAP_DATA_STORE = auto()
    PING_ONE_LDAP_GATEWAY_DATA_STORE = auto()
    MAPPED_ATTRIBUTES = auto()
    NO_MAPPING = auto()
    TEXT = auto()
    TOKEN = auto()
    REQUEST = auto()
    OAUTH_PERSISTENT_GRANT = auto()
    SUBJECT_TOKEN = auto()
    ACTOR_TOKEN = auto()
    PASSWORD_CREDENTIAL_VALIDATOR = auto()
    IDP_CONNECTION = auto()
    AUTHENTICATION_POLICY_CONTRACT = auto()
    CLAIMS = auto()
    LOCAL_IDENTITY_PROFILE = auto()
    EXTENDED_CLIENT_METADATA = auto()
    EXTENDED_PROPERTIES = auto()
    TRACKED_HTTP_PARAMS = auto()
    FRAGMENT = auto()
    INPUTS = auto()
    ATTRIBUTE_QUERY = auto()


class FieldDescriptor(AutoName):
    RADIO_GROUP = auto()
    SELECT = auto()
    FILTERABLE_SELECT = auto()
    CHECK_BOX = auto()
    TEXT_AREA = auto()
    TEXT = auto()
    UPLOAD_FILE = auto()
    HASHED_TEXT = auto()


class AccessTokenMappingContextType(AutoName):
    DEFAULT = auto()
    PCV = auto()
    IDP_CONNECTION = auto()
    IDP_ADAPTER = auto()
    AUTHENTICATION_POLICY_CONTRACT = auto()
    CLIENT_CREDENTIALS = auto()
    TOKEN_EXCHANGE_PROCESSOR_POLICY = auto()


class Location(AutoName):
    START = auto()
    END = auto()
    BEFORE = auto()
    AFTER = auto()


class AuthenticationPolicySelectionActionType(AutoName):
    APC_MAPPING = auto()
    LOCAL_IDENTITY_MAPPING = auto()
    AUTHN_SELECTOR = auto()
    AUTHN_SOURCE = auto()
    DONE = auto()
    CONTINUE = auto()
    RESTART = auto()
    FRAGMENT = auto()


class AuthenticationSourceType(AutoName):
    IDP_ADAPTER = auto()
    IDP_CONNECTION = auto()


class TimeUnit(AutoName):
    MINUTES = auto()
    DAYS = auto()
    HOURS = auto()


class ActivationCodeCheckMode(AutoName):
    AFTER_AUTHENTICATION = auto()
    BEFORE_AUTHENTICATION = auto()


class UserAuthorizationConsentPageSetting(AutoName):
    INTERNAL = auto()
    ADAPTER = auto()


class ParStatus(AutoName):
    DISABLED = auto()
    ENABLED = auto()
    REQUIRED = auto()


class OperationType(AutoName):
    SAVE = auto()
    DELETE = auto()


class Status(AutoName):
    VALID = auto()
    EXPIRED = auto()
    NOT_YET_VALID = auto()
    REVOKED = auto()


class CryptoProvider(AutoName):
    LOCAL = auto()
    HSM = auto()


class Mode(AutoName):
    CLUSTERED_ENGINE = auto()
    CLUSTERED_CONSOLE = auto()
    CLUSTERED_DUAL = auto()
    STANDALONE = auto()


class ReplicationStatus(AutoName):
    RETRIEVING = auto()
    APPLYING = auto()
    FAILED = auto()
    SUCCEEDED = auto()
    OUT_OF_DATE = auto()


class ConfigStoreSettingType(AutoName):
    STRING = auto()
    LIST = auto()
    MAP = auto()


class ConnectionType(AutoName):
    DIRECT = auto()
    LDAP_GATEWAY = auto()


class AccountStatusAlgorithm(AutoName):
    ACCOUNT_STATUS_ALGORITHM_AD = auto()
    ACCOUNT_STATUS_ALGORITHM_FLAG = auto()


class BackChannelAuthType(AutoName):
    INBOUND = auto()
    OUTBOUND = auto()


class ChangedUsersAlgorithm(AutoName):
    ACTIVE_DIRECTORY_USN = auto()
    TIMESTAMP = auto()
    TIMESTAMP_NO_NEGATION = auto()


class LoggingMode(AutoName):
    NONE = auto()
    STANDARD = auto()
    ENHANCED = auto()
    FULL = auto()


class SignatureStatus(AutoName):
    SIGNED = auto()
    UNSIGNED = auto()


class CertTrustStatus(AutoName):
    TRUSTED = auto()
    NOT_TRUSTED = auto()


class Protocol(AutoName):
    SAML20 = auto()
    WSFED = auto()
    SAML11 = auto()
    SAML10 = auto()
    OIDC = auto()


class IdpIdentityMapping(AutoName):
    ACCOUNT_MAPPING = auto()
    ACCOUNT_LINKING = auto()
    NONE = auto()


class Binding(AutoName):
    ARTIFACT = auto()
    POST = auto()
    REDIRECT = auto()
    SOAP = auto()


class EventTrigger(AutoName):
    NEW_USER_ONLY = auto()
    ALL_SAML_ASSERTIONS = auto()


class ErrorHandling(AutoName):
    CONTINUE_SSO = auto()
    ABORT_SSO = auto()


class LoginType(AutoName):
    CODE = auto()
    POST = auto()
    POST_AT = auto()


class AuthenticationScheme(AutoName):
    BASIC = auto()
    POST = auto()
    PRIVATE_KEY_JWT = auto()


class SigningAlgorithm(AutoName):
    NONE = auto()
    HS256 = auto()
    HS384 = auto()
    HS512 = auto()
    RS256 = auto()
    RS384 = auto()
    RS512 = auto()
    ES256 = auto()
    ES384 = auto()
    ES512 = auto()
    PS256 = auto()
    PS384 = auto()
    PS512 = auto()


class CharacterCase(AutoName):
    LOWER = auto()
    UPPER = auto()
    NONE = auto()


class Parser(AutoName):
    EXTRACT_CN_FROM_DN = auto()
    EXTRACT_USERNAME_FROM_EMAIL = auto()
    NONE = auto()


class WsFedTokenType(AutoName):
    SAML11 = auto()
    SAML20 = auto()
    JWT = auto()


class WsTrustVersion(AutoName):
    WSTRUST12 = auto()
    WSTRUST13 = auto()


class SpSamlIdentityMapping(AutoName):
    PSEUDONYM = auto()
    STANDARD = auto()
    TRANSIENT = auto()


class SpWsFedIdentityMapping(AutoName):
    EMAIL_ADDRESS = auto()
    USER_PRINCIPLE_NAME = auto()
    COMMON_NAME = auto()


class ConnectionTargetType(AutoName):
    STANDARD = auto()
    SALESFORCE = auto()
    SALESFORCE_CP = auto()
    SALESFORCE_PP = auto()
    PINGONE_SCIM11 = auto()


class DefaultTokenType(AutoName):
    SAML20 = auto()
    SAML11 = auto()
    SAML11_O365 = auto()


class ExpectedProtocol(AutoName):
    SAML20 = auto()
    SAML11 = auto()
    SAML10 = auto()


class LdapType(AutoName):
    ACTIVE_DIRECTORY = auto()
    ORACLE_DIRECTORY_SERVER = auto()
    ORACLE_UNIFIED_DIRECTORY = auto()
    UNBOUNDID_DS = auto()
    PING_DIRECTORY = auto()
    GENERIC = auto()


class ForwardedHeaderIndex(AutoName):
    FIRST = auto()
    LAST = auto()


class LocalIdentityFieldType(AutoName):
    CHECKBOX = auto()
    CHECKBOX_GROUP = auto()
    DATE = auto()
    DROP_DOWN = auto()
    EMAIL = auto()
    PHONE = auto()
    TEXT = auto()
    HIDDEN = auto()


class EmailVerificationType(AutoName):
    OTP = auto()
    OTL = auto()


class ExecuteWorkflow(AutoName):
    BEFORE_ACCOUNT_CREATION = auto()
    AFTER_ACCOUNT_CREATION = auto()


class RefreshRolling(AutoName):
    SERVER_DEFAULT = auto()
    DONT_ROLL = auto()
    ROLL = auto()


class DeviceFlowSettingType(AutoName):
    SERVER_DEFAULT = auto()
    OVERRIDE_SERVER_DEFAULT = auto()


class PersistentGrantLifetimeType(AutoName):
    INDEFINITE_EXPIRY = auto()
    SERVER_DEFAULT = auto()
    OVERRIDE_SERVER_DEFAULT = auto()


class ObjectSigningAlgorithm(AutoName):
    RS256 = auto()
    RS384 = auto()
    RS512 = auto()
    ES256 = auto()
    ES384 = auto()
    ES512 = auto()
    PS256 = auto()
    PS384 = auto()
    PS512 = auto()


class CibaDeliveryMode(AutoName):
    POLL = auto()
    PING = auto()


class RefreshTokenRollingGracePeriodType(AutoName):
    SERVER_DEFAULT = auto()
    OVERRIDE_SERVER_DEFAULT = auto()


class ClientSecretRetentionPeriodType(AutoName):
    SERVER_DEFAULT = auto()
    OVERRIDE_SERVER_DEFAULT = auto()


class TokenIntrospectionSigningAlgorithm(AutoName):
    RS256 = auto()
    RS384 = auto()
    RS512 = auto()
    HS256 = auto()
    HS384 = auto()
    HS512 = auto()
    ES256 = auto()
    ES384 = auto()
    ES512 = auto()
    PS256 = auto()
    PS384 = auto()
    PS512 = auto()


class TokenIntrospectionEncryptionAlgorithm(AutoName):
    DIR = auto()
    A128KW = auto()
    A192KW = auto()
    A256KW = auto()
    A128GCMKW = auto()
    A192GCMKW = auto()
    A256GCMKW = auto()
    ECDH_ES = auto()
    ECDH_ES_A128KW = auto()
    ECDH_ES_A192KW = auto()
    ECDH_ES_A256KW = auto()
    RSA_OAEP = auto()
    RSA_OAEP_256 = auto()


class TokenIntrospectionContentEncryptionAlgorithm(AutoName):
    AES_128_CBC_HMAC_SHA_256 = auto()
    AES_192_CBC_HMAC_SHA_384 = auto()
    AES_256_CBC_HMAC_SHA_512 = auto()
    AES_128_GCM = auto()
    AES_192_GCM = auto()
    AES_256_GCM = auto()


class JwtSecuredAuthorizationResponseModeSigningAlgorithm(AutoName):
    RS256 = auto()
    RS384 = auto()
    RS512 = auto()
    HS256 = auto()
    HS384 = auto()
    HS512 = auto()
    ES256 = auto()
    ES384 = auto()
    ES512 = auto()
    PS256 = auto()
    PS384 = auto()
    PS512 = auto()


class JwtSecuredAuthorizationResponseModeEncryptionAlgorithm(AutoName):
    DIR = auto()
    A128KW = auto()
    A192KW = auto()
    A256KW = auto()
    A128GCMKW = auto()
    A192GCMKW = auto()
    A256GCMKW = auto()
    ECDH_ES = auto()
    ECDH_ES_A128KW = auto()
    ECDH_ES_A192KW = auto()
    ECDH_ES_A256KW = auto()
    RSA_OAEP = auto()
    RSA_OAEP_256 = auto()


class JwtSecuredAuthorizationResponseModeContentEncryptionAlgorithm(AutoName):
    AES_128_CBC_HMAC_SHA_256 = auto()
    AES_192_CBC_HMAC_SHA_384 = auto()
    AES_256_CBC_HMAC_SHA_512 = auto()
    AES_128_GCM = auto()
    AES_192_GCM = auto()
    AES_256_GCM = auto()


class ClientAuthType(AutoName):
    NONE = auto()
    SECRET = auto()
    CERTIFICATE = auto()
    PRIVATE_KEY_JWT = auto()


class EncryptionAlgorithm(AutoName):
    DIR = auto()
    A128KW = auto()
    A192KW = auto()
    A256KW = auto()
    A128GCMKW = auto()
    A192GCMKW = auto()
    A256GCMKW = auto()
    ECDH_ES = auto()
    ECDH_ES_A128KW = auto()
    ECDH_ES_A192KW = auto()
    ECDH_ES_A256KW = auto()
    RSA_OAEP = auto()
    RSA_OAEP_256 = auto()


class ContentEncryptionAlgorithm(AutoName):
    AES_128_CBC_HMAC_SHA_256 = auto()
    AES_192_CBC_HMAC_SHA_384 = auto()
    AES_256_CBC_HMAC_SHA_512 = auto()
    AES_128_GCM = auto()
    AES_192_GCM = auto()
    AES_256_GCM = auto()


class ClientCertIssuerType(AutoName):
    NONE = auto()
    TRUST_ANY = auto()
    CERTIFICATE = auto()


class PingOneCredentialStatus(AutoName):
    VALID = auto()
    INVALID = auto()
    UNKNOWN = auto()


class ResourceCategory(AutoName):
    IDP_CONNECTION = auto()
    SP_CONNECTION = auto()
    PASSWORD_CREDENTIAL_VALIDATOR = auto()
    AUTHENTICATION_SELECTOR = auto()
    IDP_ADAPTER = auto()
    SP_ADAPTER = auto()
    ACCESS_TOKEN_MGMT_PLUGIN = auto()
    TOKEN_PROCESSOR = auto()
    TOKEN_GENERATOR = auto()
    NOTIFICATION_PUBLISHER = auto()
    OOB_AUTH_PLUGIN = auto()
    DATA_STORE = auto()
    DYNAMIC_CLIENT_REGISTRATION_PLUGIN = auto()
    IDENTITY_STORE_PROVISIONER = auto()


class IdpConnectionTransactionLoggingOverride(AutoName):
    DONT_OVERRIDE = auto()
    NONE = auto()
    FULL = auto()
    STANDARD = auto()
    ENHANCED = auto()


class SpConnectionTransactionLoggingOverride(AutoName):
    DONT_OVERRIDE = auto()
    NONE = auto()
    FULL = auto()
    STANDARD = auto()
    ENHANCED = auto()


class Format(AutoName):
    PKCS12 = auto()
    PEM = auto()


class SpUrlMappingType(AutoName):
    SP_ADAPTER = auto()
    SP_CONNECTION = auto()
