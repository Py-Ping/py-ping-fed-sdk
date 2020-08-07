class FederationInfo():
    """Federation Info.

    Attributes
    ----------
    autoConnectEntityId : string
 This property has been deprecated and no longer used
    baseUrl : string
 The fully qualified host name, port, and path (if applicable) on which the PingFederate server runs.
    saml1xIssuerId : string
 This ID identifies your federation server for SAML 1.x transactions. As with SAML 2.0, it is usually defined as an organization's URL or a DNS address. The SourceID used for artifact resolution is derived from this ID using SHA1.
    saml1xSourceId : string
 If supplied, the Source ID value entered here is used for SAML 1.x, instead of being derived from the SAML 1.x Issuer/Audience.
    saml2EntityId : string
 This ID defines your organization as the entity operating the server for SAML 2.0 transactions. It is usually defined as an organization's URL or a DNS address; for example: pingidentity.com. The SAML SourceID used for artifact resolution is derived from this ID using SHA1.
    wsfedRealm : string
 The URI of the realm associated with the PingFederate server. A realm represents a single unit of security administration or trust.

    """

<<<<<<< HEAD
    def __init__(self, autoConnectEntityId=None, baseUrl=None, saml1xIssuerId=None, saml1xSourceId=None, saml2EntityId=None, wsfedRealm=None) -> None:
        self.autoConnectEntityId = autoConnectEntityId
        self.baseUrl = baseUrl
        self.saml1xIssuerId = saml1xIssuerId
        self.saml1xSourceId = saml1xSourceId
        self.saml2EntityId = saml2EntityId
        self.wsfedRealm = wsfedRealm
=======
    def __init__(self, autoConnectEntityId=None, baseUrl=None, saml1xIssuerId=None, saml1xSourceId=None, saml2EntityId=None, wsfedRealm=None):
        self.autoConnectEntityId: str = autoConnectEntityId
        self.baseUrl: str = baseUrl
        self.saml1xIssuerId: str = saml1xIssuerId
        self.saml1xSourceId: str = saml1xSourceId
        self.saml2EntityId: str = saml2EntityId
        self.wsfedRealm: str = wsfedRealm
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, FederationInfo):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.autoConnectEntityId, self.baseUrl, self.saml1xIssuerId, self.saml1xSourceId, self.saml2EntityId, self.wsfedRealm))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["autoConnectEntityId", "baseUrl", "saml1xIssuerId", "saml1xSourceId", "saml2EntityId", "wsfedRealm"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
