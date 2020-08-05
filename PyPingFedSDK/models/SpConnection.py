class SpConnection():
    """ The set of attributes used to configure an SP connection.

    Attributes
    ----------
    active : boolean
        Specifies whether the connection is active and ready to process incoming requests. The default value is false.
    additionalAllowedEntitiesConfiguration : str
        Additional allowed entities or issuers configuration. Currently only used in OIDC IdP (RP) connection.
    applicationIconUrl : string
        The application icon url.
    applicationName : string
        The application name.
    attributeQuery : str
        The attribute query settings for supporting SPs in requesting user attributes.
    baseUrl : string
        The fully-qualified hostname and port on which your partner's federation deployment runs.
    contactInfo : str
        The contact information for this partner.
    credentials : str
        The certificates and settings for encryption, signing, and signature verification. It is required for  SAMLx.x and WS-Fed Connections.
    defaultVirtualEntityId : string
        The default alternate entity ID that identifies the local server to this partner. It is required when virtualEntityIds is not empty and must be included in that list.
    entityId : string
        The partner's entity ID (connection ID) or issuer value (for OIDC Connections).
    extendedProperties : str
        Extended Properties allows to store additional information for IdP/SP Connections. The names of these extended properties should be defined in /extendedProperties.
    id : string
        The persistent, unique ID for the connection. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.
    licenseConnectionGroup : string
        The license connection group. If your PingFederate license is based on connection groups, each connection must be assigned to a group before it can be used.
    loggingMode : str
        The level of transaction logging applicable for this connection. Default is STANDARD.
    metadataReloadSettings : str
        Connection metadata automatic reload settings.
    name : string
        The connection name.
    outboundProvision : str
        The Outbound Provision settings.
    spBrowserSso : str
        The browser-based SSO settings used to communicate with your SP.
    type : str
        The type of this connection. This must be set to 'SP'.
    virtualEntityIds : array
        List of alternate entity IDs that identifies the local server to this partner.
    wsTrust : str
        The Ws-Trust settings.

    """

    __slots__ = ["active", "additionalAllowedEntitiesConfiguration", "applicationIconUrl", "applicationName", "attributeQuery", "baseUrl", "contactInfo", "credentials", "defaultVirtualEntityId", "entityId", "extendedProperties", "id", "licenseConnectionGroup", "loggingMode", "metadataReloadSettings", "name", "outboundProvision", "spBrowserSso", "type", "virtualEntityIds", "wsTrust"]
    def __init__(self, type, entityId, name, active=None, additionalAllowedEntitiesConfiguration=None, applicationIconUrl=None, applicationName=None, attributeQuery=None, baseUrl=None, contactInfo=None, credentials=None, defaultVirtualEntityId=None, extendedProperties=None, id=None, licenseConnectionGroup=None, loggingMode=None, metadataReloadSettings=None, outboundProvision=None, spBrowserSso=None, virtualEntityIds=None, wsTrust=None):
            self.active = active
            self.additionalAllowedEntitiesConfiguration = additionalAllowedEntitiesConfiguration
            self.applicationIconUrl = applicationIconUrl
            self.applicationName = applicationName
            self.attributeQuery = attributeQuery
            self.baseUrl = baseUrl
            self.contactInfo = contactInfo
            self.credentials = credentials
            self.defaultVirtualEntityId = defaultVirtualEntityId
            self.entityId = entityId
            self.extendedProperties = extendedProperties
            self.id = id
            self.licenseConnectionGroup = licenseConnectionGroup
            self.loggingMode = loggingMode
            self.metadataReloadSettings = metadataReloadSettings
            self.name = name
            self.outboundProvision = outboundProvision
            self.spBrowserSso = spBrowserSso
            self.type = type
            self.virtualEntityIds = virtualEntityIds
            self.wsTrust = wsTrust
    
    def _validate(self):
        return any(x for x in ['type', 'entityId', 'name'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, SpConnection):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((active, additionalAllowedEntitiesConfiguration, applicationIconUrl, applicationName, attributeQuery, baseUrl, contactInfo, credentials, defaultVirtualEntityId, entityId, extendedProperties, id, licenseConnectionGroup, loggingMode, metadataReloadSettings, name, outboundProvision, spBrowserSso, type, virtualEntityIds, wsTrust))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
