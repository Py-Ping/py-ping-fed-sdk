class ConvertMetadataRequest():
    """A request for converting SAML connection metadata into a JSON connection.

    Attributes
    ----------
    connectionType : str
        The expected connection type to convert.    expectedEntityId : string
        The entity ID of the connection to be obtained from the input SAML Metadata. Required if the SAML Metadata has more than one connection defined.    expectedProtocol : str
        The expected browser-based SSO protocol to convert. In this case the protocol is restricted to SAML.    samlMetadata : string
        The base-64 encoded XML SAML metadata.    templateConnection : str
        The template connection to overlay the metadata on.    verificationCertificate : string
        The certificate to validate the metadata signature against. The certificate can be in PEM format or base-64 encoded DER format.
    """

    __slots__ = ["connectionType", "expectedEntityId", "expectedProtocol", "samlMetadata", "templateConnection", "verificationCertificate"]

    def __init__(self, connectionType, expectedProtocol, samlMetadata, expectedEntityId=None, templateConnection=None, verificationCertificate=None):
        self.connectionType: str = connectionType
        self.expectedEntityId: str = expectedEntityId
        self.expectedProtocol: str = expectedProtocol
        self.samlMetadata: str = samlMetadata
        self.templateConnection: str = templateConnection
        self.verificationCertificate: str = verificationCertificate

    def _validate(self):
        return any(x for x in ['connectionType', 'expectedProtocol', 'samlMetadata'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ConvertMetadataRequest):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.connectionType, self.expectedEntityId, self.expectedProtocol, self.samlMetadata, self.templateConnection, self.verificationCertificate))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["connectionType", "expectedEntityId", "expectedProtocol", "samlMetadata", "templateConnection", "verificationCertificate"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__