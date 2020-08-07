class LdapAttributeSource():
    """The configured settings used to look up attributes from a LDAP data store.

    Attributes
    ----------
    attributeContractFulfillment : str
        A list of mappings from attribute names to their fulfillment values. This field is only valid for the SP Connection's Browser SSO mappings    baseDn : string
        The base DN to search from. If not specified, the search will start at the LDAP's root.    binaryAttributeSettings : str
        The advanced settings for binary LDAP attributes.    dataStoreRef : str
        Reference to the associated data store.    description : string
        The description of this attribute source. The description needs to be unique amongst the attribute sources for the mapping.<br>Note: Required for APC-to-SP Adapter Mappings    id : string
        The ID that defines this attribute source. Only alphanumeric characters allowed.<br>Note: Required for OpenID Connect policy attribute sources, OAuth IdP adapter mappings, OAuth access token mappings and APC-to-SP Adapter Mappings. IdP Connections will ignore this property since it only allows one attribute source to be defined per mapping. IdP-to-SP Adapter Mappings can contain multiple attribute sources.    memberOfNestedGroup : boolean
        Set this to true to return transitive group memberships for the 'memberOf' attribute.  This only applies for Active Directory data sources.  All other data sources will be set to false.    searchFilter : string
        The LDAP filter that will be used to lookup the objects from the directory.    searchScope : str
        Determines the node depth of the query.    type : str
        The data store type of this attribute source.
    """

    __slots__ = ["attributeContractFulfillment", "baseDn", "binaryAttributeSettings", "dataStoreRef", "description", "id", "memberOfNestedGroup", "searchFilter", "searchScope", "type"]

    def __init__(self, type, dataStoreRef, searchScope, searchFilter, attributeContractFulfillment=None, baseDn=None, binaryAttributeSettings=None, description=None, id=None, memberOfNestedGroup=None):
        self.attributeContractFulfillment: str = attributeContractFulfillment
        self.baseDn: str = baseDn
        self.binaryAttributeSettings: str = binaryAttributeSettings
        self.dataStoreRef: str = dataStoreRef
        self.description: str = description
        self.id: str = id
        self.memberOfNestedGroup: bool = memberOfNestedGroup
        self.searchFilter: str = searchFilter
        self.searchScope: str = searchScope
        self.type: str = type

    def _validate(self):
        return any(x for x in ['type', 'dataStoreRef', 'searchScope', 'searchFilter'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, LdapAttributeSource):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.attributeContractFulfillment, self.baseDn, self.binaryAttributeSettings, self.dataStoreRef, self.description, self.id, self.memberOfNestedGroup, self.searchFilter, self.searchScope, self.type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeContractFulfillment", "baseDn", "binaryAttributeSettings", "dataStoreRef", "description", "id", "memberOfNestedGroup", "searchFilter", "searchScope", "type"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__