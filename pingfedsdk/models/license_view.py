from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.connection_group_license_view import ConnectionGroupLicenseView
from pingfedsdk.models.license_feature_view import LicenseFeatureView


class LicenseView(Model):
    """PingFederate License details.

    Attributes
    ----------
    name: str
        Name of the person the license was issued to.

    id: str
        Unique identifier of a license.

    maxConnections: int
        Maximum number of connections that can be created under this license (if applicable).

    usedConnections: int
        Number of used connections under this license.

    tier: str
        The tier value from the license file. The possible values are FREE, PERPETUAL or SUBSCRIPTION.

    issueDate: str
        The issue date value from the license file.

    expirationDate: str
        The expiration date value from the license file (if applicable).

    enforcementType: str
        The enforcement type is a 3-bit binary value, expressed as a decimal digit. The bits from left to right are:
        1: Shutdown on expire
        2: Notify on expire
        4: Enforce minor version
        if all three enforcements are active, the enforcement type will be 7 (1 + 2 + 4); if only the first two are active, you have an enforcement type of 3 (1 + 2).

    version: str
        The Ping Identity product version from the license file.

    product: str
        The Ping Identity product value from the license file.

    organization: str
        The organization value from the license file.

    gracePeriod: int
        Number of days provided as grace period, past the expiration date (if applicable).

    nodeLimit: int
        Maximum number of clustered nodes allowed under this license (if applicable).

    licenseGroups: list
        License connection groups, if applicable.

    oauthEnabled: bool
        Indicates whether OAuth role is enabled for this license.

    wsTrustEnabled: bool
        Indicates whether WS-Trust role is enabled for this license.

    provisioningEnabled: bool
        Indicates whether Provisioning role is enabled for this license.

    bridgeMode: bool
        Indicates whether this license is a bridge license or not.

    features: list
        Other licence features, if applicable.

    """
    def __init__(self, name: str = None, id: str = None, maxConnections: int = None, usedConnections: int = None, tier: str = None, issueDate: str = None, expirationDate: str = None, enforcementType: str = None, version: str = None, product: str = None, organization: str = None, gracePeriod: int = None, nodeLimit: int = None, licenseGroups: list = None, oauthEnabled: bool = None, wsTrustEnabled: bool = None, provisioningEnabled: bool = None, bridgeMode: bool = None, features: list = None) -> None:
        self.name = name
        self.id = id
        self.maxConnections = maxConnections
        self.usedConnections = usedConnections
        self.tier = tier
        self.issueDate = issueDate
        self.expirationDate = expirationDate
        self.enforcementType = enforcementType
        self.version = version
        self.product = product
        self.organization = organization
        self.gracePeriod = gracePeriod
        self.nodeLimit = nodeLimit
        self.licenseGroups = licenseGroups
        self.oauthEnabled = oauthEnabled
        self.wsTrustEnabled = wsTrustEnabled
        self.provisioningEnabled = provisioningEnabled
        self.bridgeMode = bridgeMode
        self.features = features

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, LicenseView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.name, self.id, self.maxConnections, self.usedConnections, self.tier, self.issueDate, self.expirationDate, self.enforcementType, self.version, self.product, self.organization, self.gracePeriod, self.nodeLimit, self.licenseGroups, self.oauthEnabled, self.wsTrustEnabled, self.provisioningEnabled, self.bridgeMode, self.features]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["name", "id", "maxConnections", "usedConnections", "tier", "issueDate", "expirationDate", "enforcementType", "version", "product", "organization", "gracePeriod", "nodeLimit", "licenseGroups", "oauthEnabled", "wsTrustEnabled", "provisioningEnabled", "bridgeMode", "features"] and v is not None:
                if k == "name":
                    valid_data[k] = str(v)
                if k == "id":
                    valid_data[k] = str(v)
                if k == "maxConnections":
                    valid_data[k] = int(v)
                if k == "usedConnections":
                    valid_data[k] = int(v)
                if k == "tier":
                    valid_data[k] = str(v)
                if k == "issueDate":
                    valid_data[k] = str(v)
                if k == "expirationDate":
                    valid_data[k] = str(v)
                if k == "enforcementType":
                    valid_data[k] = str(v)
                if k == "version":
                    valid_data[k] = str(v)
                if k == "product":
                    valid_data[k] = str(v)
                if k == "organization":
                    valid_data[k] = str(v)
                if k == "gracePeriod":
                    valid_data[k] = int(v)
                if k == "nodeLimit":
                    valid_data[k] = int(v)
                if k == "licenseGroups":
                    valid_data[k] = [ConnectionGroupLicenseView.from_dict(x) for x in v]
                if k == "oauthEnabled":
                    valid_data[k] = bool(v)
                if k == "wsTrustEnabled":
                    valid_data[k] = bool(v)
                if k == "provisioningEnabled":
                    valid_data[k] = bool(v)
                if k == "bridgeMode":
                    valid_data[k] = bool(v)
                if k == "features":
                    valid_data[k] = [LicenseFeatureView.from_dict(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["name", "id", "maxConnections", "usedConnections", "tier", "issueDate", "expirationDate", "enforcementType", "version", "product", "organization", "gracePeriod", "nodeLimit", "licenseGroups", "oauthEnabled", "wsTrustEnabled", "provisioningEnabled", "bridgeMode", "features"]:
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
