class LicenseView():
    """PingFederate License details.

    Attributes
    ----------
    enforcementType : string
 The enforcement type is a 3-bit binary value, expressed as a decimal digit. The bits from left to right are: <br>1: Shutdown on expire <br>2: Notify on expire <br>4: Enforce minor version <br>if all three enforcements are active, the enforcement type will be 7 (1 + 2 + 4); if only the first two are active, you have an enforcement type of 3 (1 + 2).
    expirationDate : string
 The expiration date value from the license file (if applicable).
    gracePeriod : integer
 Number of days provided as grace period, past the expiration date (if applicable).
    id : string
 Unique identifier of a license.
    issueDate : string
 The issue date value from the license file.
    licenseGroups : array
 License connection groups, if applicable.
    maxConnections : integer
 Maximum number of connections that can be created under this license (if applicable).
    name : string
 Name of the person the license was issued to.
    nodeLimit : integer
 Maximum number of clustered nodes allowed under this license (if applicable).
    oauthEnabled : boolean
 Indicates whether OAuth role is enabled for this license.
    organization : string
 The organization value from the license file.
    product : string
 The Ping Identity product value from the license file.
    provisioningEnabled : boolean
 Indicates whether Provisioning role is enabled for this license.
    tier : string
 The tier value from the license file. The possible values are FREE, PERPETUAL or SUBSCRIPTION.
    version : string
 The Ping Identity product version from the license file.
    wsTrustEnabled : boolean
 Indicates whether WS-Trust role is enabled for this license.

    """

    def __init__(self, enforcementType=None, expirationDate=None, gracePeriod=None, var_id=None, issueDate=None, licenseGroups=None, maxConnections=None, name=None, nodeLimit=None, oauthEnabled=None, organization=None, product=None, provisioningEnabled=None, tier=None, version=None, wsTrustEnabled=None) -> None:
        self.enforcementType = enforcementType
        self.expirationDate = expirationDate
        self.gracePeriod = gracePeriod
        self.var_id = var_id
        self.issueDate = issueDate
        self.licenseGroups = licenseGroups
        self.maxConnections = maxConnections
        self.name = name
        self.nodeLimit = nodeLimit
        self.oauthEnabled = oauthEnabled
        self.organization = organization
        self.product = product
        self.provisioningEnabled = provisioningEnabled
        self.tier = tier
        self.version = version
        self.wsTrustEnabled = wsTrustEnabled

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, LicenseView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.enforcementType, self.expirationDate, self.gracePeriod, self.var_id, self.issueDate, self.licenseGroups, self.maxConnections, self.name, self.nodeLimit, self.oauthEnabled, self.organization, self.product, self.provisioningEnabled, self.tier, self.version, self.wsTrustEnabled))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["enforcementType", "expirationDate", "gracePeriod", "var_id", "issueDate", "licenseGroups", "maxConnections", "name", "nodeLimit", "oauthEnabled", "organization", "product", "provisioningEnabled", "tier", "version", "wsTrustEnabled"]}

        return cls(**valid_data)