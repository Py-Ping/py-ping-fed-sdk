from enum import Enum

from pingfedsdk.enums import CertTrustStatus
from pingfedsdk.enums import SignatureStatus
from pingfedsdk.model import Model
from pingfedsdk.models.connection import Connection


class ConvertMetadataResponse(Model):
    """A response from converting SAML connection metadata into a JSON connection. It includes the converted connection and the authenticity information of the metadata.

    Attributes
    ----------
    signatureStatus: SignatureStatus
        The metadata's digital signature status.

    certTrustStatus: CertTrustStatus
        The metadata certificate's trust status, i.e. If the partner's certificate can be trusted or not.

    certSubjectDn: str
        The metadata certificate's subject DN.

    certSerialNumber: str
        The metadata certificate's serial number.

    certExpiration: str
        The metadata certificate's expiry date.

    connection: Connection
        The converted API connection.

    """
    def __init__(self, signatureStatus: SignatureStatus = None, certTrustStatus: CertTrustStatus = None, certSubjectDn: str = None, certSerialNumber: str = None, certExpiration: str = None, connection: Connection = None) -> None:
        self.signatureStatus = signatureStatus
        self.certTrustStatus = certTrustStatus
        self.certSubjectDn = certSubjectDn
        self.certSerialNumber = certSerialNumber
        self.certExpiration = certExpiration
        self.connection = connection

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ConvertMetadataResponse):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.signatureStatus, self.certTrustStatus, self.certSubjectDn, self.certSerialNumber, self.certExpiration, self.connection]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["signatureStatus", "certTrustStatus", "certSubjectDn", "certSerialNumber", "certExpiration", "connection"] and v is not None:
                if k == "signatureStatus":
                    valid_data[k] = SignatureStatus[v]
                if k == "certTrustStatus":
                    valid_data[k] = CertTrustStatus[v]
                if k == "certSubjectDn":
                    valid_data[k] = str(v)
                if k == "certSerialNumber":
                    valid_data[k] = str(v)
                if k == "certExpiration":
                    valid_data[k] = str(v)
                if k == "connection":
                    valid_data[k] = Connection.from_dict(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["signatureStatus", "certTrustStatus", "certSubjectDn", "certSerialNumber", "certExpiration", "connection"]:
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
