from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.service_model import ServiceModel


class ServiceAuthentication(Model):
    """Service Authentication Settings.

    Attributes
    ----------
    attributeQuery: ServiceModel
        SAML2.0 attribute query service. Remove the JSON field to deactivate the attribute query service.

    jmx: ServiceModel
        JMX application management and monitoring service. Remove the JSON field to deactivate the JMX service.

    connectionManagement: ServiceModel
        (Deprecated) Connection management service. Remove the JSON field to deactivate the connection management service.

    ssoDirectoryService: ServiceModel
        (Deprecated) SSO directory service. Remove the JSON field to deactivate the SSO Directory service.

    """

    def __init__(self, attributeQuery: ServiceModel = None, jmx: ServiceModel = None, connectionManagement: ServiceModel = None, ssoDirectoryService: ServiceModel = None) -> None:
        self.attributeQuery = attributeQuery
        self.jmx = jmx
        self.connectionManagement = connectionManagement
        self.ssoDirectoryService = ssoDirectoryService

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ServiceAuthentication):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.attributeQuery, self.jmx, self.connectionManagement, self.ssoDirectoryService]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["attributeQuery", "jmx", "connectionManagement", "ssoDirectoryService"] and v is not None:
                if k == "attributeQuery":
                    valid_data[k] = ServiceModel(**v)
                if k == "jmx":
                    valid_data[k] = ServiceModel(**v)
                if k == "connectionManagement":
                    valid_data[k] = ServiceModel(**v)
                if k == "ssoDirectoryService":
                    valid_data[k] = ServiceModel(**v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["attributeQuery", "jmx", "connectionManagement", "ssoDirectoryService"]:
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
