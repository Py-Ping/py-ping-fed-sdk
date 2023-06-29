from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.connection_credentials import ConnectionCredentials
from pingfedsdk.models.contact_info import ContactInfo
from pingfedsdk.models.connection_metadata_url import ConnectionMetadataUrl
from pingfedsdk.models.sp_attribute_query import SpAttributeQuery
from pingfedsdk.models.outbound_provision import OutboundProvision
from pingfedsdk.models.sp_browser_sso import SpBrowserSso
from pingfedsdk.models.sp_ws_trust import SpWsTrust
from pingfedsdk.models.additional_allowed_entities_configuration import AdditionalAllowedEntitiesConfiguration
from pingfedsdk.enums import ConnectionType
from pingfedsdk.enums import ConnectionTargetType
from pingfedsdk.enums import LoggingMode


class SpConnection(Model):
    """The set of attributes used to configure an SP connection.

    Attributes
    ----------
    type: ConnectionType
        The type of this connection. Default is 'IDP'.

    id: str
        The persistent, unique ID for the connection. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.

    entityId: str
        The partner's entity ID (connection ID) or issuer value (for OIDC Connections).

    name: str
        The connection name.

    modificationDate: str
        The time at which the connection was last changed. This property is read only and is ignored on PUT and POST requests.

    creationDate: str
        The time at which the connection was created. This property is read only and is ignored on PUT and POST requests.

    active: bool
        Specifies whether the connection is active and ready to process incoming requests. The default value is false.

    baseUrl: str
        The fully-qualified hostname and port on which your partner's federation deployment runs.

    defaultVirtualEntityId: str
        The default alternate entity ID that identifies the local server to this partner. It is required when virtualEntityIds is not empty and must be included in that list.

    virtualEntityIds: list
        List of alternate entity IDs that identifies the local server to this partner.

    metadataReloadSettings: ConnectionMetadataUrl
        Connection metadata automatic reload settings.

    credentials: ConnectionCredentials
        The certificates and settings for encryption, signing, and signature verification. It is required for  SAMLx.x and WS-Fed Connections.

    contactInfo: ContactInfo
        The contact information for this partner.

    licenseConnectionGroup: str
        The license connection group. If your PingFederate license is based on connection groups, each connection must be assigned to a group before it can be used.

    loggingMode: LoggingMode
        The level of transaction logging applicable for this connection. Default is STANDARD.

    additionalAllowedEntitiesConfiguration: AdditionalAllowedEntitiesConfiguration
        Additional allowed entities or issuers configuration. Currently only used in OIDC IdP (RP) connection.

    extendedProperties: object
        Extended Properties allows to store additional information for IdP/SP Connections. The names of these extended properties should be defined in /extendedProperties.

    spBrowserSso: SpBrowserSso
        The browser-based SSO settings used to communicate with your SP.

    attributeQuery: SpAttributeQuery
        The attribute query settings for supporting SPs in requesting user attributes.

    wsTrust: SpWsTrust
        The Ws-Trust settings.

    applicationName: str
        The application name.

    applicationIconUrl: str
        The application icon url.

    outboundProvision: OutboundProvision
        The Outbound Provision settings.

    connectionTargetType: ConnectionTargetType
        The connection target type. This field is intended for bulk import/export usage. Changing its value may result in unexpected behavior.

    """

    def __init__(self, entityId: str, name: str, type: ConnectionType = None , id: str = None , modificationDate: str = None , creationDate: str = None , active: bool = None , baseUrl: str = None , defaultVirtualEntityId: str = None , virtualEntityIds: list = None , metadataReloadSettings: ConnectionMetadataUrl = None , credentials: ConnectionCredentials = None , contactInfo: ContactInfo = None , licenseConnectionGroup: str = None , loggingMode: LoggingMode = None , additionalAllowedEntitiesConfiguration: AdditionalAllowedEntitiesConfiguration = None , extendedProperties: object = None , spBrowserSso: SpBrowserSso = None , attributeQuery: SpAttributeQuery = None , wsTrust: SpWsTrust = None , applicationName: str = None , applicationIconUrl: str = None , outboundProvision: OutboundProvision = None , connectionTargetType: ConnectionTargetType = None ) -> None:
        self.type = type
        self.id = id
        self.entityId = entityId
        self.name = name
        self.modificationDate = modificationDate
        self.creationDate = creationDate
        self.active = active
        self.baseUrl = baseUrl
        self.defaultVirtualEntityId = defaultVirtualEntityId
        self.virtualEntityIds = virtualEntityIds
        self.metadataReloadSettings = metadataReloadSettings
        self.credentials = credentials
        self.contactInfo = contactInfo
        self.licenseConnectionGroup = licenseConnectionGroup
        self.loggingMode = loggingMode
        self.additionalAllowedEntitiesConfiguration = additionalAllowedEntitiesConfiguration
        self.extendedProperties = extendedProperties
        self.spBrowserSso = spBrowserSso
        self.attributeQuery = attributeQuery
        self.wsTrust = wsTrust
        self.applicationName = applicationName
        self.applicationIconUrl = applicationIconUrl
        self.outboundProvision = outboundProvision
        self.connectionTargetType = connectionTargetType

    def _validate(self) -> bool:
        return any(x for x in ["entityId", "name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SpConnection):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.id, self.entityId, self.name, self.modificationDate, self.creationDate, self.active, self.baseUrl, self.defaultVirtualEntityId, self.virtualEntityIds, self.metadataReloadSettings, self.credentials, self.contactInfo, self.licenseConnectionGroup, self.loggingMode, self.additionalAllowedEntitiesConfiguration, self.extendedProperties, self.spBrowserSso, self.attributeQuery, self.wsTrust, self.applicationName, self.applicationIconUrl, self.outboundProvision, self.connectionTargetType]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "id", "entityId", "name", "modificationDate", "creationDate", "active", "baseUrl", "defaultVirtualEntityId", "virtualEntityIds", "metadataReloadSettings", "credentials", "contactInfo", "licenseConnectionGroup", "loggingMode", "additionalAllowedEntitiesConfiguration", "extendedProperties", "spBrowserSso", "attributeQuery", "wsTrust", "applicationName", "applicationIconUrl", "outboundProvision", "connectionTargetType"] and v is not None:
                if k == "type":
                    valid_data[k] = ConnectionType[v]
                if k == "id":
                    valid_data[k] = str(v)
                if k == "entityId":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "modificationDate":
                    valid_data[k] = str(v)
                if k == "creationDate":
                    valid_data[k] = str(v)
                if k == "active":
                    valid_data[k] = bool(v)
                if k == "baseUrl":
                    valid_data[k] = str(v)
                if k == "defaultVirtualEntityId":
                    valid_data[k] = str(v)
                if k == "virtualEntityIds":
                    valid_data[k] = [str(x) for x in v]
                if k == "metadataReloadSettings":
                    valid_data[k] = ConnectionMetadataUrl(**v)
                if k == "credentials":
                    valid_data[k] = ConnectionCredentials(**v)
                if k == "contactInfo":
                    valid_data[k] = ContactInfo(**v)
                if k == "licenseConnectionGroup":
                    valid_data[k] = str(v)
                if k == "loggingMode":
                    valid_data[k] = LoggingMode[v]
                if k == "additionalAllowedEntitiesConfiguration":
                    valid_data[k] = AdditionalAllowedEntitiesConfiguration(**v)
                if k == "extendedProperties":
                    valid_data[k] = object(**v)
                if k == "spBrowserSso":
                    valid_data[k] = SpBrowserSso(**v)
                if k == "attributeQuery":
                    valid_data[k] = SpAttributeQuery(**v)
                if k == "wsTrust":
                    valid_data[k] = SpWsTrust(**v)
                if k == "applicationName":
                    valid_data[k] = str(v)
                if k == "applicationIconUrl":
                    valid_data[k] = str(v)
                if k == "outboundProvision":
                    valid_data[k] = OutboundProvision(**v)
                if k == "connectionTargetType":
                    valid_data[k] = ConnectionTargetType[v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["type", "id", "entityId", "name", "modificationDate", "creationDate", "active", "baseUrl", "defaultVirtualEntityId", "virtualEntityIds", "metadataReloadSettings", "credentials", "contactInfo", "licenseConnectionGroup", "loggingMode", "additionalAllowedEntitiesConfiguration", "extendedProperties", "spBrowserSso", "attributeQuery", "wsTrust", "applicationName", "applicationIconUrl", "outboundProvision", "connectionTargetType"]:
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
