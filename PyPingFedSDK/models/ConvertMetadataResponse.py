class ConvertMetadataResponse():
    """A response from converting SAML connection metadata into a JSON connection. It includes the converted connection and the authenticity information of the metadata.

    Attributes
    ----------
    certExpiration : string
        The metadata certificate's expiry date.    certSerialNumber : string
        The metadata certificate's serial number.    certSubjectDn : string
        The metadata certificate's subject DN.    certTrustStatus : str
        The metadata certificate's trust status, i.e. If the partner's certificate can be trusted or not.    connection : str
        The converted API connection.    signatureStatus : str
        The metadata's digital signature status.
    """

    __slots__ = ["certExpiration", "certSerialNumber", "certSubjectDn", "certTrustStatus", "connection", "signatureStatus"]

    def __init__(self, certExpiration=None, certSerialNumber=None, certSubjectDn=None, certTrustStatus=None, connection=None, signatureStatus=None):
        self.certExpiration = certExpiration
        self.certSerialNumber = certSerialNumber
        self.certSubjectDn = certSubjectDn
        self.certTrustStatus = certTrustStatus
        self.connection = connection
        self.signatureStatus = signatureStatus

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ConvertMetadataResponse):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.certExpiration, self.certSerialNumber, self.certSubjectDn, self.certTrustStatus, self.connection, self.signatureStatus))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["certExpiration", "certSerialNumber", "certSubjectDn", "certTrustStatus", "connection", "signatureStatus"]}

        return cls(**valid_data)
