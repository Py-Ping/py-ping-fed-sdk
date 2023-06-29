from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.models.alternative_login_hint_token_issuer import AlternativeLoginHintTokenIssuer
from pingfedsdk.models.attribute_mapping import AttributeMapping
from pingfedsdk.models.identity_hint_contract import IdentityHintContract


class RequestPolicy(Model):
    """The set of attributes used to configure a CIBA request policy.

    Attributes
    ----------
    id: str
        The request policy ID. ID is unique.

    name: str
        The request policy name. Name is unique.

    authenticatorRef: ResourceLink
        Reference to the associated authenticator.

    userCodePcvRef: ResourceLink
        Reference to the associated password credential validator.

    transactionLifetime: int
        The transaction lifetime in seconds.

    allowUnsignedLoginHintToken: bool
        Allow unsigned login hint token.

    requireTokenForIdentityHint: bool
        Require token for identity hint.

    alternativeLoginHintTokenIssuers: list
        Alternative login hint token issuers.

    identityHintContract: IdentityHintContract
        Identity hint attribute contract.

    identityHintContractFulfillment: AttributeMapping
        Identity hint attribute contract fulfillment.

    identityHintMapping: AttributeMapping
        Identity hint contract to request policy mapping.

    """

    def __init__(self, authenticatorRef: ResourceLink, id: str, identityHintContract: IdentityHintContract, name: str, userCodePcvRef: ResourceLink = None, transactionLifetime: int = None, allowUnsignedLoginHintToken: bool = None, requireTokenForIdentityHint: bool = None, alternativeLoginHintTokenIssuers: list = None, identityHintContractFulfillment: AttributeMapping = None, identityHintMapping: AttributeMapping = None) -> None:
        self.id = id
        self.name = name
        self.authenticatorRef = authenticatorRef
        self.userCodePcvRef = userCodePcvRef
        self.transactionLifetime = transactionLifetime
        self.allowUnsignedLoginHintToken = allowUnsignedLoginHintToken
        self.requireTokenForIdentityHint = requireTokenForIdentityHint
        self.alternativeLoginHintTokenIssuers = alternativeLoginHintTokenIssuers
        self.identityHintContract = identityHintContract
        self.identityHintContractFulfillment = identityHintContractFulfillment
        self.identityHintMapping = identityHintMapping

    def _validate(self) -> bool:
        return any(x for x in ["authenticatorRef", "id", "identityHintContract", "name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, RequestPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.name, self.authenticatorRef, self.userCodePcvRef, self.transactionLifetime, self.allowUnsignedLoginHintToken, self.requireTokenForIdentityHint, self.alternativeLoginHintTokenIssuers, self.identityHintContract, self.identityHintContractFulfillment, self.identityHintMapping]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "name", "authenticatorRef", "userCodePcvRef", "transactionLifetime", "allowUnsignedLoginHintToken", "requireTokenForIdentityHint", "alternativeLoginHintTokenIssuers", "identityHintContract", "identityHintContractFulfillment", "identityHintMapping"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "authenticatorRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "userCodePcvRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "transactionLifetime":
                    valid_data[k] = int(v)
                if k == "allowUnsignedLoginHintToken":
                    valid_data[k] = bool(v)
                if k == "requireTokenForIdentityHint":
                    valid_data[k] = bool(v)
                if k == "alternativeLoginHintTokenIssuers":
                    valid_data[k] = [AlternativeLoginHintTokenIssuer(**x) for x in v]
                if k == "identityHintContract":
                    valid_data[k] = IdentityHintContract(**v)
                if k == "identityHintContractFulfillment":
                    valid_data[k] = AttributeMapping(**v)
                if k == "identityHintMapping":
                    valid_data[k] = AttributeMapping(**v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "name", "authenticatorRef", "userCodePcvRef", "transactionLifetime", "allowUnsignedLoginHintToken", "requireTokenForIdentityHint", "alternativeLoginHintTokenIssuers", "identityHintContract", "identityHintContractFulfillment", "identityHintMapping"]:
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
