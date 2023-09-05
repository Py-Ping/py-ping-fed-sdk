from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.enums import LdapAttributeSourceType
from pingfedsdk.enums import SearchScope


class LdapAttributeSource(Model):
    """The configured settings used to look up attributes from a LDAP data store.

    Attributes
    ----------
    type: LdapAttributeSourceType
        The data store type of this attribute source.

    dataStoreRef: ResourceLink
        Reference to the associated data store.

    id: str
        The ID that defines this attribute source. Only alphanumeric characters allowed.
        Note: Required for OpenID Connect policy attribute sources, OAuth IdP adapter mappings, OAuth access token mappings and APC-to-SP Adapter Mappings. IdP Connections will ignore this property since it only allows one attribute source to be defined per mapping. IdP-to-SP Adapter Mappings can contain multiple attribute sources.

    description: str
        The description of this attribute source. The description needs to be unique amongst the attribute sources for the mapping.
        Note: Required for APC-to-SP Adapter Mappings

    attributeContractFulfillment: object
        A list of mappings from attribute names to their fulfillment values. This field is only valid for the SP Connection's Browser SSO mappings

    baseDn: str
        The base DN to search from. If not specified, the search will start at the LDAP's root.

    searchScope: SearchScope
        Determines the node depth of the query.

    searchFilter: str
        The LDAP filter that will be used to lookup the objects from the directory.

    searchAttributes: list
        A list of LDAP attributes returned from search and available for mapping.

    binaryAttributeSettings: object
        The advanced settings for binary LDAP attributes.

    memberOfNestedGroup: bool
        Set this to true to return transitive group memberships for the 'memberOf' attribute.  This only applies for Active Directory data sources.  All other data sources will be set to false.

    """

    def __init__(self, searchFilter: str, searchScope: SearchScope, type: LdapAttributeSourceType = None, dataStoreRef: ResourceLink = None, id: str = None, description: str = None, attributeContractFulfillment: object = None, baseDn: str = None, searchAttributes: list = None, binaryAttributeSettings: object = None, memberOfNestedGroup: bool = None) -> None:
        self.type = type
        self.dataStoreRef = dataStoreRef
        self.id = id
        self.description = description
        self.attributeContractFulfillment = attributeContractFulfillment
        self.baseDn = baseDn
        self.searchScope = searchScope
        self.searchFilter = searchFilter
        self.searchAttributes = searchAttributes
        self.binaryAttributeSettings = binaryAttributeSettings
        self.memberOfNestedGroup = memberOfNestedGroup

    def _validate(self) -> bool:
        return any(x for x in ["searchFilter", "searchScope"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, LdapAttributeSource):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.dataStoreRef, self.id, self.description, self.attributeContractFulfillment, self.baseDn, self.searchScope, self.searchFilter, self.searchAttributes, self.binaryAttributeSettings, self.memberOfNestedGroup]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "dataStoreRef", "id", "description", "attributeContractFulfillment", "baseDn", "searchScope", "searchFilter", "searchAttributes", "binaryAttributeSettings", "memberOfNestedGroup"] and v is not None:
                if k == "type":
                    valid_data[k] = LdapAttributeSourceType[v]
                if k == "dataStoreRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "id":
                    valid_data[k] = str(v)
                if k == "description":
                    valid_data[k] = str(v)
                if k == "attributeContractFulfillment":
                    valid_data[k] = object(**v)
                if k == "baseDn":
                    valid_data[k] = str(v)
                if k == "searchScope":
                    valid_data[k] = SearchScope[v]
                if k == "searchFilter":
                    valid_data[k] = str(v)
                if k == "searchAttributes":
                    valid_data[k] = [str(x) for x in v]
                if k == "binaryAttributeSettings":
                    valid_data[k] = object(**v)
                if k == "memberOfNestedGroup":
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
            if k in ["type", "dataStoreRef", "id", "description", "attributeContractFulfillment", "baseDn", "searchScope", "searchFilter", "searchAttributes", "binaryAttributeSettings", "memberOfNestedGroup"]:
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
