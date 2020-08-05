class ExportMetadataRequest():
    """ The request for exporting a SAML connection's metadata file for a partner.

    Attributes
    ----------
    connectionId : string
        The ID of the connection to export.
    connectionType : str
        The type of connection to export.
    signingSettings : str
        The signing settings to sign the metadata with. If null, the metadata will not be signed
    useSecondaryPortForSoap : boolean
        If PingFederate's secondary SSL port is configured and you want to use it for the SOAP channel, set to true. If client-certificate authentication is configured for the SOAP channel, the secondary port is required and this must be set to true.
    virtualHostName : string
        The virtual host name to be used as the base url.
    virtualServerId : string
        The virtual server ID to export the metadata with. If null, the connection's default will be used.

    """

    __slots__ = ["connectionId", "connectionType", "signingSettings", "useSecondaryPortForSoap", "virtualHostName", "virtualServerId"]
    def __init__(self, connectionType, connectionId, signingSettings=None, useSecondaryPortForSoap=None, virtualHostName=None, virtualServerId=None):
            self.connectionId = connectionId
            self.connectionType = connectionType
            self.signingSettings = signingSettings
            self.useSecondaryPortForSoap = useSecondaryPortForSoap
            self.virtualHostName = virtualHostName
            self.virtualServerId = virtualServerId
    
    def _validate(self):
        return any(x for x in ['connectionType', 'connectionId'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ExportMetadataRequest):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((connectionId, connectionType, signingSettings, useSecondaryPortForSoap, virtualHostName, virtualServerId))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
