from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.connection import Connection
from pingfedsdk.enums import ExpectedProtocol
from pingfedsdk.enums import ConnectionType


class ConvertMetadataRequest(Model):
    """A request for converting SAML connection metadata into a JSON connection.

    Attributes
    ----------
    connectionType: ConnectionType
        The expected connection type to convert.

    expectedProtocol: ExpectedProtocol
        The expected browser-based SSO protocol to convert. In this case the protocol is restricted to SAML.

    expectedEntityId: str
        The entity ID of the connection to be obtained from the input SAML Metadata. Required if the SAML Metadata has more than one connection defined.

    samlMetadata: str
        The base-64 encoded XML SAML metadata.

    verificationCertificate: str
        The certificate to validate the metadata signature against. The certificate can be in PEM format or base-64 encoded DER format.

    templateConnection: Connection
        The template connection to overlay the metadata on.

    """

    def __init__(self, connectionType: ConnectionType, expectedProtocol: ExpectedProtocol, samlMetadata: str, expectedEntityId: str = None, verificationCertificate: str = None, templateConnection: Connection = None) -> None:
        self.connectionType = connectionType
        self.expectedProtocol = expectedProtocol
        self.expectedEntityId = expectedEntityId
        self.samlMetadata = samlMetadata
        self.verificationCertificate = verificationCertificate
        self.templateConnection = templateConnection

    def _validate(self) -> bool:
        return any(x for x in ["connectionType", "expectedProtocol", "samlMetadata"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ConvertMetadataRequest):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.connectionType, self.expectedProtocol, self.expectedEntityId, self.samlMetadata, self.verificationCertificate, self.templateConnection]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["connectionType", "expectedProtocol", "expectedEntityId", "samlMetadata", "verificationCertificate", "templateConnection"] and v is not None:
                if k == "connectionType":
                    valid_data[k] = ConnectionType[v]
                if k == "expectedProtocol":
                    valid_data[k] = ExpectedProtocol[v]
                if k == "expectedEntityId":
                    valid_data[k] = str(v)
                if k == "samlMetadata":
                    valid_data[k] = str(v)
                if k == "verificationCertificate":
                    valid_data[k] = str(v)
                if k == "templateConnection":
                    valid_data[k] = Connection(**v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["connectionType", "expectedProtocol", "expectedEntityId", "samlMetadata", "verificationCertificate", "templateConnection"]:
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
