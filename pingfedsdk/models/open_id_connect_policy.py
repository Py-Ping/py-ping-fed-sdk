from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.attribute_mapping import AttributeMapping
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.models.open_id_connect_attribute_contract import OpenIdConnectAttributeContract


class OpenIdConnectPolicy(Model):
    """The set of attributes used to configure an OpenID Connect policy.

    Attributes
    ----------
    id: str
        The policy ID used internally.

    name: str
        The name used for display in UI screens.

    accessTokenManagerRef: ResourceLink
        The access token manager associated with this Open ID Connect policy.

    idTokenLifetime: int
        The ID Token Lifetime, in minutes. The default value is 5.

    includeSriInIdToken: bool
        Determines whether a Session Reference Identifier is included in the ID token.

    includeUserInfoInIdToken: bool
        Determines whether the User Info is always included in the ID token.

    includeSHashInIdToken: bool
        Determines whether the State Hash should be included in the ID token.

    returnIdTokenOnRefreshGrant: bool
        Determines whether an ID Token should be returned when refresh grant is requested or not.

    reissueIdTokenInHybridFlow: bool
        Determines whether a new ID Token should be returned during token request of the hybrid flow.

    attributeContract: OpenIdConnectAttributeContract
        The list of attributes that will be returned to OAuth clients in response to requests received at the PingFederate UserInfo endpoint.

    attributeMapping: AttributeMapping
        The attributes mapping from attribute sources to attribute targets.

    scopeAttributeMappings: object
        The attribute scope mappings from scopes to attribute names.

    """

    def __init__(self, accessTokenManagerRef: ResourceLink, attributeContract: OpenIdConnectAttributeContract, attributeMapping: AttributeMapping, id: str, name: str, idTokenLifetime: int = None, includeSriInIdToken: bool = None, includeUserInfoInIdToken: bool = None, includeSHashInIdToken: bool = None, returnIdTokenOnRefreshGrant: bool = None, reissueIdTokenInHybridFlow: bool = None, scopeAttributeMappings: object = None) -> None:
        self.id = id
        self.name = name
        self.accessTokenManagerRef = accessTokenManagerRef
        self.idTokenLifetime = idTokenLifetime
        self.includeSriInIdToken = includeSriInIdToken
        self.includeUserInfoInIdToken = includeUserInfoInIdToken
        self.includeSHashInIdToken = includeSHashInIdToken
        self.returnIdTokenOnRefreshGrant = returnIdTokenOnRefreshGrant
        self.reissueIdTokenInHybridFlow = reissueIdTokenInHybridFlow
        self.attributeContract = attributeContract
        self.attributeMapping = attributeMapping
        self.scopeAttributeMappings = scopeAttributeMappings

    def _validate(self) -> bool:
        return any(x for x in ["accessTokenManagerRef", "attributeContract", "attributeMapping", "id", "name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OpenIdConnectPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.name, self.accessTokenManagerRef, self.idTokenLifetime, self.includeSriInIdToken, self.includeUserInfoInIdToken, self.includeSHashInIdToken, self.returnIdTokenOnRefreshGrant, self.reissueIdTokenInHybridFlow, self.attributeContract, self.attributeMapping, self.scopeAttributeMappings]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "name", "accessTokenManagerRef", "idTokenLifetime", "includeSriInIdToken", "includeUserInfoInIdToken", "includeSHashInIdToken", "returnIdTokenOnRefreshGrant", "reissueIdTokenInHybridFlow", "attributeContract", "attributeMapping", "scopeAttributeMappings"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "accessTokenManagerRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "idTokenLifetime":
                    valid_data[k] = int(v)
                if k == "includeSriInIdToken":
                    valid_data[k] = bool(v)
                if k == "includeUserInfoInIdToken":
                    valid_data[k] = bool(v)
                if k == "includeSHashInIdToken":
                    valid_data[k] = bool(v)
                if k == "returnIdTokenOnRefreshGrant":
                    valid_data[k] = bool(v)
                if k == "reissueIdTokenInHybridFlow":
                    valid_data[k] = bool(v)
                if k == "attributeContract":
                    valid_data[k] = OpenIdConnectAttributeContract(**v)
                if k == "attributeMapping":
                    valid_data[k] = AttributeMapping(**v)
                if k == "scopeAttributeMappings":
                    valid_data[k] = object(**v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "name", "accessTokenManagerRef", "idTokenLifetime", "includeSriInIdToken", "includeUserInfoInIdToken", "includeSHashInIdToken", "returnIdTokenOnRefreshGrant", "reissueIdTokenInHybridFlow", "attributeContract", "attributeMapping", "scopeAttributeMappings"]:
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
