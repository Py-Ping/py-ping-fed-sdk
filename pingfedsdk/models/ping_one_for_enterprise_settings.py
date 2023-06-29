from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink


class PingOneForEnterpriseSettings(Model):
    """PingOne for Enterprise Settings

    Attributes
    ----------
    connectedToPingOneForEnterprise: bool
        A read only field indicating whether PingFederate is connected to PingOne for Enterprise.

    pingOneSsoConnection: ResourceLink
        A read only reference to the SP connection configured for PingOne SSO.

    companyName: str
        A read only field indicating the company name.

    enableAdminConsoleSso: bool
        Indicates whether single sign on from PingOne for Enterprise to the PingFederate admin console is enabled. The default is false.

    enableMonitoring: bool
        Indicates whether monitoring of PingFederate from PingOne for Enterprise is enabled. The default is true.

    currentAuthnKeyCreationTime: str
        A read only field indicating the creation time of the current authentication key.

    previousAuthnKeyCreationTime: str
        A read only field indicating the creation time of the previous authentication key.

    identityRepositoryUpdateRequired: bool
        A read-only field indicating whether changes were made in the current PingFederate configuration that might affect your connection with PingOne for Enterprise. For example, if you modified the attribute contract of your SSO configuration. Update the identity repository to keep your PingFederate and PingOne for Enterprise settings synchronized.

    """

    def __init__(self, connectedToPingOneForEnterprise: bool = None, pingOneSsoConnection: ResourceLink = None, companyName: str = None, enableAdminConsoleSso: bool = None, enableMonitoring: bool = None, currentAuthnKeyCreationTime: str = None, previousAuthnKeyCreationTime: str = None, identityRepositoryUpdateRequired: bool = None) -> None:
        self.connectedToPingOneForEnterprise = connectedToPingOneForEnterprise
        self.pingOneSsoConnection = pingOneSsoConnection
        self.companyName = companyName
        self.enableAdminConsoleSso = enableAdminConsoleSso
        self.enableMonitoring = enableMonitoring
        self.currentAuthnKeyCreationTime = currentAuthnKeyCreationTime
        self.previousAuthnKeyCreationTime = previousAuthnKeyCreationTime
        self.identityRepositoryUpdateRequired = identityRepositoryUpdateRequired

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, PingOneForEnterpriseSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.connectedToPingOneForEnterprise, self.pingOneSsoConnection, self.companyName, self.enableAdminConsoleSso, self.enableMonitoring, self.currentAuthnKeyCreationTime, self.previousAuthnKeyCreationTime, self.identityRepositoryUpdateRequired]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["connectedToPingOneForEnterprise", "pingOneSsoConnection", "companyName", "enableAdminConsoleSso", "enableMonitoring", "currentAuthnKeyCreationTime", "previousAuthnKeyCreationTime", "identityRepositoryUpdateRequired"] and v is not None:
                if k == "connectedToPingOneForEnterprise":
                    valid_data[k] = bool(v)
                if k == "pingOneSsoConnection":
                    valid_data[k] = ResourceLink(**v)
                if k == "companyName":
                    valid_data[k] = str(v)
                if k == "enableAdminConsoleSso":
                    valid_data[k] = bool(v)
                if k == "enableMonitoring":
                    valid_data[k] = bool(v)
                if k == "currentAuthnKeyCreationTime":
                    valid_data[k] = str(v)
                if k == "previousAuthnKeyCreationTime":
                    valid_data[k] = str(v)
                if k == "identityRepositoryUpdateRequired":
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
            if k in ["connectedToPingOneForEnterprise", "pingOneSsoConnection", "companyName", "enableAdminConsoleSso", "enableMonitoring", "currentAuthnKeyCreationTime", "previousAuthnKeyCreationTime", "identityRepositoryUpdateRequired"]:
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
