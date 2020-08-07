class IdpConnection():
    """The set of attributes used to configure an IdP connection.

    Attributes
    ----------
    active : boolean
        Specifies whether the connection is active and ready to process incoming requests. The default value is false.    additionalAllowedEntitiesConfiguration : str
        Additional allowed entities or issuers configuration. Currently only used in OIDC IdP (RP) connection.    attributeQuery : str
        The attribute query settings for requesting user attributes from an attribute authority.    baseUrl : string
        The fully-qualified hostname and port on which your partner's federation deployment runs.    contactInfo : str
        The contact information for this partner.    credentials : str
        The certificates and settings for encryption, signing, and signature verification. It is required for  SAMLx.x and WS-Fed Connections.    defaultVirtualEntityId : string
        The default alternate entity ID that identifies the local server to this partner. It is required when virtualEntityIds is not empty and must be included in that list.    entityId : string
        The partner's entity ID (connection ID) or issuer value (for OIDC Connections).    errorPageMsgId : string
        Identifier that specifies the message displayed on a user-facing error page.    extendedProperties : str
        Extended Properties allows to store additional information for IdP/SP Connections. The names of these extended properties should be defined in /extendedProperties.    id : string
        The persistent, unique ID for the connection. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.    idpBrowserSso : str
        The browser-based SSO settings used to communicate with your IdP.    idpOAuthGrantAttributeMapping : str
        The OAuth Assertion Grant settings used to map from your IdP.    licenseConnectionGroup : string
        The license connection group. If your PingFederate license is based on connection groups, each connection must be assigned to a group before it can be used.    loggingMode : str
        The level of transaction logging applicable for this connection. Default is STANDARD.    metadataReloadSettings : str
        Connection metadata automatic reload settings.    name : string
        The connection name.    oidcClientCredentials : str
        The OIDC client credentials. This is required for an OIDC connection.    type : str
        The type of this connection. Default is 'IDP'.    virtualEntityIds : array
        List of alternate entity IDs that identifies the local server to this partner.    wsTrust : str
        The Ws-Trust settings.
    """

    __slots__ = ["active", "additionalAllowedEntitiesConfiguration", "attributeQuery", "baseUrl", "contactInfo", "credentials", "defaultVirtualEntityId", "entityId", "errorPageMsgId", "extendedProperties", "id", "idpBrowserSso", "idpOAuthGrantAttributeMapping", "licenseConnectionGroup", "loggingMode", "metadataReloadSettings", "name", "oidcClientCredentials", "type", "virtualEntityIds", "wsTrust"]

    def __init__(self, entityId, name, active=None, additionalAllowedEntitiesConfiguration=None, attributeQuery=None, baseUrl=None, contactInfo=None, credentials=None, defaultVirtualEntityId=None, errorPageMsgId=None, extendedProperties=None, id=None, idpBrowserSso=None, idpOAuthGrantAttributeMapping=None, licenseConnectionGroup=None, loggingMode=None, metadataReloadSettings=None, oidcClientCredentials=None, type=None, virtualEntityIds=None, wsTrust=None):
        self.active: bool = active
        self.additionalAllowedEntitiesConfiguration: str = additionalAllowedEntitiesConfiguration
        self.attributeQuery: str = attributeQuery
        self.baseUrl: str = baseUrl
        self.contactInfo: str = contactInfo
        self.credentials: str = credentials
        self.defaultVirtualEntityId: str = defaultVirtualEntityId
        self.entityId: str = entityId
        self.errorPageMsgId: str = errorPageMsgId
        self.extendedProperties: str = extendedProperties
        self.id: str = id
        self.idpBrowserSso: str = idpBrowserSso
        self.idpOAuthGrantAttributeMapping: str = idpOAuthGrantAttributeMapping
        self.licenseConnectionGroup: str = licenseConnectionGroup
        self.loggingMode: str = loggingMode
        self.metadataReloadSettings: str = metadataReloadSettings
        self.name: str = name
        self.oidcClientCredentials: str = oidcClientCredentials
        self.type: str = type
        self.virtualEntityIds: list = virtualEntityIds
        self.wsTrust: str = wsTrust

    def _validate(self):
        return any(x for x in ['entityId', 'name'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, IdpConnection):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.active, self.additionalAllowedEntitiesConfiguration, self.attributeQuery, self.baseUrl, self.contactInfo, self.credentials, self.defaultVirtualEntityId, self.entityId, self.errorPageMsgId, self.extendedProperties, self.id, self.idpBrowserSso, self.idpOAuthGrantAttributeMapping, self.licenseConnectionGroup, self.loggingMode, self.metadataReloadSettings, self.name, self.oidcClientCredentials, self.type, self.virtualEntityIds, self.wsTrust))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["active", "additionalAllowedEntitiesConfiguration", "attributeQuery", "baseUrl", "contactInfo", "credentials", "defaultVirtualEntityId", "entityId", "errorPageMsgId", "extendedProperties", "id", "idpBrowserSso", "idpOAuthGrantAttributeMapping", "licenseConnectionGroup", "loggingMode", "metadataReloadSettings", "name", "oidcClientCredentials", "type", "virtualEntityIds", "wsTrust"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__