class ConvertMetadataRequest():
    """A request for converting SAML connection metadata into a JSON connection.

    Attributes
    ----------
    connectionType : str
 The expected connection type to convert.
    expectedEntityId : string
 The entity ID of the connection to be obtained from the input SAML Metadata. Required if the SAML Metadata has more than one connection defined.
    expectedProtocol : str
 The expected browser-based SSO protocol to convert. In this case the protocol is restricted to SAML.
    samlMetadata : string
 The base-64 encoded XML SAML metadata.
    templateConnection : str
 The template connection to overlay the metadata on.
    verificationCertificate : string
 The certificate to validate the metadata signature against. The certificate can be in PEM format or base-64 encoded DER format.

    """

    def __init__(self, connectionType, expectedProtocol, samlMetadata:str, expectedEntityId:str=None, templateConnection=None, verificationCertificate:str=None) -> None:
        self.connectionType = connectionType
        self.expectedEntityId = expectedEntityId
        self.expectedProtocol = expectedProtocol
        self.samlMetadata = samlMetadata
        self.templateConnection = templateConnection
        self.verificationCertificate = verificationCertificate

    def _validate(self) -> bool:
        return any(x for x in ["connectionType", "expectedProtocol", "samlMetadata"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ConvertMetadataRequest):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.connectionType, self.expectedEntityId, self.expectedProtocol, self.samlMetadata, self.templateConnection, self.verificationCertificate))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["connectionType", "expectedEntityId", "expectedProtocol", "samlMetadata", "templateConnection", "verificationCertificate"]}

        return cls(**valid_data)