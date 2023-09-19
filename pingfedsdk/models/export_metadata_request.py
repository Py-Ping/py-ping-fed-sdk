from enum import Enum

from pingfedsdk.enums import ConnectionType
from pingfedsdk.model import Model
from pingfedsdk.models.base_signing_settings import BaseSigningSettings


class ExportMetadataRequest(Model):
    """The request for exporting a SAML connection's metadata file for a partner.

    Attributes
    ----------
    connectionType: ConnectionType
        The type of connection to export.

    connectionId: str
        The ID of the connection to export.

    virtualServerId: str
        The virtual server ID to export the metadata with. If null, the connection's default will be used.

    signingSettings: BaseSigningSettings
        The signing settings to sign the metadata with. If null, the metadata will not be signed

    useSecondaryPortForSoap: bool
        If PingFederate's secondary SSL port is configured and you want to use it for the SOAP channel, set to true. If client-certificate authentication is configured for the SOAP channel, the secondary port is required and this must be set to true.

    virtualHostName: str
        The virtual host name to be used as the base url.

    """
    def __init__(self, connectionType: ConnectionType, connectionId: str, virtualServerId: str = None, signingSettings: BaseSigningSettings = None, useSecondaryPortForSoap: bool = None, virtualHostName: str = None) -> None:
        self.connectionType = connectionType
        self.connectionId = connectionId
        self.virtualServerId = virtualServerId
        self.signingSettings = signingSettings
        self.useSecondaryPortForSoap = useSecondaryPortForSoap
        self.virtualHostName = virtualHostName

    def _validate(self) -> bool:
        return any(x for x in ["connectionId", "connectionType"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ExportMetadataRequest):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.connectionType, self.connectionId, self.virtualServerId, self.signingSettings, self.useSecondaryPortForSoap, self.virtualHostName]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["connectionType", "connectionId", "virtualServerId", "signingSettings", "useSecondaryPortForSoap", "virtualHostName"] and v is not None:
                if k == "connectionType":
                    valid_data[k] = ConnectionType[v]
                if k == "connectionId":
                    valid_data[k] = str(v)
                if k == "virtualServerId":
                    valid_data[k] = str(v)
                if k == "signingSettings":
                    valid_data[k] = BaseSigningSettings.from_dict(v)
                if k == "useSecondaryPortForSoap":
                    valid_data[k] = bool(v)
                if k == "virtualHostName":
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
            if k in ["connectionType", "connectionId", "virtualServerId", "signingSettings", "useSecondaryPortForSoap", "virtualHostName"]:
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
