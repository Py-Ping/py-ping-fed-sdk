from enum import Enum, auto


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class FieldDescriptorType(AutoName):
    RADIO_GROUP = auto()
    SELECT = auto()
    FILTERABLE_SELECT = auto()
    CHECK_BOX = auto()
    TEXT_AREA = auto()
    TEXT = auto()
    UPLOAD_FILE = auto()
    HASHED_TEXT = auto()


class DataStoreType(AutoName):
    LDAP = auto()
    JDBC = auto()
    CUSTOM = auto()


class LdapAttrEncodingType(AutoName):
    BASE64 = auto()
    HEX = auto()
    SID = auto()


class ConditionType(AutoName):
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


class LdapSearchScope(AutoName):
    OBJECT = auto()
    ONE_LEVEL = auto()
    SUBTREE = auto()


class SourceType(AutoName):
    TOKEN_EXCHANGE_PROCESSOR_POLICY = auto()
    ACCOUNT_LINK = auto()
    ADAPTER = auto()
    ASSERTION = auto()
    CONTEXT = auto()
    CUSTOM_DATA_STORE = auto()
    EXPRESSION = auto()
    JDBC_DATA_STORE = auto()
    LDAP_DATA_STORE = auto()
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


class ForwardedHeaderIndex(AutoName):
    FIRST = auto()
    LAST = auto()


class Type(AutoName):
    STRING = auto()
    LIST = auto()
    MAP = auto()


class CryptoProvider(AutoName):
    LOCAL = auto()
    HSM = auto()


class CertificateValidity(AutoName):
    VALID = auto()
    EXPIRED = auto()
    NOT_YET_VALID = auto()
    REVOKED = auto()


class TargetUrlSource(AutoName):
    SP_ADAPTER = auto()
    SP_CONNECTION = auto()


class SaasAccountStatusAlgorithm(AutoName):
    ACCOUNT_STATUS_ALGORITHM_AD = auto()
    ACCOUNT_STATUS_ALGORITHM_FLAG = auto()


class BackChannelAuthType(AutoName):
    INBOUND = auto()
    OUTBOUND = auto()


class SaasChangedUsersAlgorithm(AutoName):
    ACTIVE_DIRECTORY_USN = auto()
    TIMESTAMP = auto()
    TIMESTAMP_NO_NEGATION = auto()


class LoggingMode(AutoName):
    NONE = auto()
    STANDARD = auto()
    ENHANCED = auto()
    FULL = auto()


class ConnectionType(AutoName):
    IDP = auto()
    SP = auto()


class IdpIdentityMapping(AutoName):
    ACCOUNT_MAPPING = auto()
    ACCOUNT_LINKING = auto()
    NONE = auto()


class Protocol(AutoName):
    SAML20 = auto()
    WSFED = auto()
    SAML11 = auto()
    SAML10 = auto()
    OIDC = auto()


class Binding(AutoName):
    ARTIFACT = auto()
    POST = auto()
    REDIRECT = auto()
    SOAP = auto()


class OIDCAuthenticationScheme(AutoName):
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


class OIDCLoginType(AutoName):
    CODE = auto()
    POST = auto()
    POST_AT = auto()


class CharacterCase(AutoName):
    LOWER = auto()
    UPPER = auto()
    NONE = auto()


class SaasFieldParsing(AutoName):
    EXTRACT_CN_FROM_DN = auto()
    EXTRACT_USERNAME_FROM_EMAIL = auto()
    NONE = auto()


class SpSamlIdentityMapping(AutoName):
    PSEUDONYM = auto()
    STANDARD = auto()
    TRANSIENT = auto()


class SpWsFedIdentityMapping(AutoName):
    EMAIL_ADDRESS = auto()
    USER_PRINCIPLE_NAME = auto()
    COMMON_NAME = auto()


class WsFedTokenType(AutoName):
    SAML11 = auto()
    SAML20 = auto()
    JWT = auto()


class WsTrustVersion(AutoName):
    WSTRUST12 = auto()
    WSTRUST13 = auto()


class SamlTokenType(AutoName):
    SAML20 = auto()
    SAML11 = auto()
    SAML11_O365 = auto()


class ConfigOperationType(AutoName):
    SAVE = auto()
    DELETE = auto()


class AuthenticationPolicySelectionActionType(AutoName):
    APC_MAPPING = auto()
    LOCAL_IDENTITY_MAPPING = auto()
    AUTHN_SELECTOR = auto()
    AUTHN_SOURCE = auto()
    DONE = auto()
    CONTINUE = auto()
    RESTART = auto()


class AuthenticationSourceType(AutoName):
    IDP_ADAPTER = auto()
    IDP_CONNECTION = auto()


class LdapType(AutoName):
    ACTIVE_DIRECTORY = auto()
    ORACLE_DIRECTORY_SERVER = auto()
    ORACLE_UNIFIED_DIRECTORY = auto()
    UNBOUNDID_DS = auto()
    PING_DIRECTORY = auto()
    GENERIC = auto()


class LocalIdentityFieldType(AutoName):
    CHECKBOX = auto()
    CHECKBOX_GROUP = auto()
    DATE = auto()
    DROP_DOWN = auto()
    EMAIL = auto()
    PHONE = auto()
    TEXT = auto()
    HIDDEN = auto()


class SessionTimeUnit(AutoName):
    MINUTES = auto()
    HOURS = auto()
    DAYS = auto()


class PersistentGrantLifetimeUnit(AutoName):
    MINUTES = auto()
    DAYS = auto()
    HOURS = auto()


class UserAuthorizationConsentPageSetting(AutoName):
    INTERNAL = auto()
    ADAPTER = auto()


class CibaDeliveryMode(AutoName):
    POLL = auto()
    PING = auto()


class CibaRequestObjectSigningAlgorithm(AutoName):
    RS256 = auto()
    RS384 = auto()
    RS512 = auto()
    ES256 = auto()
    ES384 = auto()
    ES512 = auto()
    PS256 = auto()
    PS384 = auto()
    PS512 = auto()


class DeviceFlowSettingType(AutoName):
    SERVER_DEFAULT = auto()
    OVERRIDE_SERVER_DEFAULT = auto()


class PersistentGrantLifetimeType(AutoName):
    INDEFINITE_EXPIRY = auto()
    SERVER_DEFAULT = auto()
    OVERRIDE_SERVER_DEFAULT = auto()


class RefreshRollingType(AutoName):
    SERVER_DEFAULT = auto()
    DONT_ROLL = auto()
    ROLL = auto()


class RequestObjectSigningAlgorithm(AutoName):
    RS256 = auto()
    RS384 = auto()
    RS512 = auto()
    ES256 = auto()
    ES384 = auto()
    ES512 = auto()
    PS256 = auto()
    PS384 = auto()
    PS512 = auto()


class TokenEndpointAuthSigningAlgorithm(AutoName):
    RS256 = auto()
    RS384 = auto()
    RS512 = auto()
    ES256 = auto()
    ES384 = auto()
    ES512 = auto()
    PS256 = auto()
    PS384 = auto()
    PS512 = auto()


class ClientAuthType(AutoName):
    NONE = auto()
    SECRET = auto()
    CERTIFICATE = auto()
    PRIVATE_KEY_JWT = auto()


class ContentEncryptionAlgorithm(AutoName):
    AES_128_CBC_HMAC_SHA_256 = auto()
    AES_192_CBC_HMAC_SHA_384 = auto()
    AES_256_CBC_HMAC_SHA_512 = auto()
    AES_128_GCM = auto()
    AES_192_GCM = auto()
    AES_256_GCM = auto()


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


class ClientCertificateIssuerType(AutoName):
    NONE = auto()
    TRUST_ANY = auto()
    CERTIFICATE = auto()


class AccessTokenMappingType(AutoName):
    DEFAULT = auto()
    PCV = auto()
    IDP_CONNECTION = auto()
    IDP_ADAPTER = auto()
    AUTHENTICATION_POLICY_CONTRACT = auto()
    CLIENT_CREDENTIALS = auto()
    TOKEN_EXCHANGE_PROCESSOR_POLICY = auto()


class DeploymentMode(AutoName):
    CLUSTERED_ENGINE = auto()
    CLUSTERED_CONSOLE = auto()
    CLUSTERED_DUAL = auto()
    STANDALONE = auto()


class MetadataProtocol(AutoName):
    SAML20 = auto()
    SAML11 = auto()
    SAML10 = auto()


class MetadataCertificateTrustStatus(AutoName):
    TRUSTED = auto()
    NOT_TRUSTED = auto()


class MetadataSignatureStatus(AutoName):
    SIGNED = auto()
    UNSIGNED = auto()


