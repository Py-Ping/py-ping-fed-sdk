from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.resource_link import ResourceLink


class SslServerSettings(Model):
    """Settings for the SSL Server certificate configuration.

    Attributes
    ----------
    runtimeServerCertRef: ResourceLink
        Reference to the default SSL Server Certificate Key pair active for Runtime Server.

    adminConsoleCertRef: ResourceLink
        Reference to the default SSL Server Certificate Key pair active for PF Administrator Console.

    activeRuntimeServerCerts: list
        The active SSL Server Certificate Key pairs for Runtime Server.

    activeAdminConsoleCerts: list
        The active SSL Server Certificate Key pairs for PF Administrator Console.

    """

    def __init__(self, adminConsoleCertRef: ResourceLink, runtimeServerCertRef: ResourceLink, activeRuntimeServerCerts: list = None, activeAdminConsoleCerts: list = None) -> None:
        self.runtimeServerCertRef = runtimeServerCertRef
        self.adminConsoleCertRef = adminConsoleCertRef
        self.activeRuntimeServerCerts = activeRuntimeServerCerts
        self.activeAdminConsoleCerts = activeAdminConsoleCerts

    def _validate(self) -> bool:
        return any(x for x in ["adminConsoleCertRef", "runtimeServerCertRef"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SslServerSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.runtimeServerCertRef, self.adminConsoleCertRef, self.activeRuntimeServerCerts, self.activeAdminConsoleCerts]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["runtimeServerCertRef", "adminConsoleCertRef", "activeRuntimeServerCerts", "activeAdminConsoleCerts"] and v is not None:
                if k == "runtimeServerCertRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "adminConsoleCertRef":
                    valid_data[k] = ResourceLink(**v)
                if k == "activeRuntimeServerCerts":
                    valid_data[k] = [ResourceLink(**x) for x in v]
                if k == "activeAdminConsoleCerts":
                    valid_data[k] = [ResourceLink(**x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["runtimeServerCertRef", "adminConsoleCertRef", "activeRuntimeServerCerts", "activeAdminConsoleCerts"]:
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
