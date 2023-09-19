from enum import Enum

from pingfedsdk.model import Model


class FederationInfo(Model):
    """Federation Info.

    Attributes
    ----------
    baseUrl: str
        The fully qualified host name, port, and path (if applicable) on which the PingFederate server runs.

    saml2EntityId: str
        This ID defines your organization as the entity operating the server for SAML 2.0 transactions. It is usually defined as an organization's URL or a DNS address; for example: pingidentity.com. The SAML SourceID used for artifact resolution is derived from this ID using SHA1.

    autoConnectEntityId: str
        This property has been deprecated and no longer used

    saml1xIssuerId: str
        This ID identifies your federation server for SAML 1.x transactions. As with SAML 2.0, it is usually defined as an organization's URL or a DNS address. The SourceID used for artifact resolution is derived from this ID using SHA1.

    saml1xSourceId: str
        If supplied, the Source ID value entered here is used for SAML 1.x, instead of being derived from the SAML 1.x Issuer/Audience.

    wsfedRealm: str
        The URI of the realm associated with the PingFederate server. A realm represents a single unit of security administration or trust.

    """
    def __init__(self, baseUrl: str = None, saml2EntityId: str = None, autoConnectEntityId: str = None, saml1xIssuerId: str = None, saml1xSourceId: str = None, wsfedRealm: str = None) -> None:
        self.baseUrl = baseUrl
        self.saml2EntityId = saml2EntityId
        self.autoConnectEntityId = autoConnectEntityId
        self.saml1xIssuerId = saml1xIssuerId
        self.saml1xSourceId = saml1xSourceId
        self.wsfedRealm = wsfedRealm

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, FederationInfo):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.baseUrl, self.saml2EntityId, self.autoConnectEntityId, self.saml1xIssuerId, self.saml1xSourceId, self.wsfedRealm]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["baseUrl", "saml2EntityId", "autoConnectEntityId", "saml1xIssuerId", "saml1xSourceId", "wsfedRealm"] and v is not None:
                if k == "baseUrl":
                    valid_data[k] = str(v)
                if k == "saml2EntityId":
                    valid_data[k] = str(v)
                if k == "autoConnectEntityId":
                    valid_data[k] = str(v)
                if k == "saml1xIssuerId":
                    valid_data[k] = str(v)
                if k == "saml1xSourceId":
                    valid_data[k] = str(v)
                if k == "wsfedRealm":
                    valid_data[k] = str(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["baseUrl", "saml2EntityId", "autoConnectEntityId", "saml1xIssuerId", "saml1xSourceId", "wsfedRealm"]:
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
