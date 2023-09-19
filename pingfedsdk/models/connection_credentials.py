from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.connection_cert import ConnectionCert
from pingfedsdk.models.inbound_back_channel_auth import InboundBackChannelAuth
from pingfedsdk.models.outbound_back_channel_auth import OutboundBackChannelAuth
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.models.signing_settings import SigningSettings


class ConnectionCredentials(Model):
    """The certificates and settings for encryption, signing, and signature verification.

    Attributes
    ----------
    verificationSubjectDN: str
        If this property is set, the verification trust model is Anchored. The verification certificate must be signed by a trusted CA and included in the incoming message, and the subject DN of the expected certificate is specified in this property. If this property is not set, then a primary verification certificate must be specified in the certs array.

    verificationIssuerDN: str
        If a verification Subject DN is provided, you can optionally restrict the issuer to a specific trusted CA by specifying its DN in this field.

    certs: list
        The certificates used for signature verification and XML encryption.

    blockEncryptionAlgorithm: str
        The algorithm used to encrypt assertions sent to this partner. AES_128, AES_256, AES_128_GCM, AES_192_GCM, AES_256_GCM and Triple_DES are also supported. Default is AES_128

    keyTransportAlgorithm: str
        The algorithm used to transport keys to this partner. RSA_OAEP and RSA_v15 are supported. Default is RSA_OAEP

    signingSettings: SigningSettings
        Settings related to the manner in which messages sent to the partner are digitally signed. Required for SP Connections.

    decryptionKeyPairRef: ResourceLink
        The ID of the primary key pair used to decrypt message content received from this partner. The ID of the key pair is also known as the alias and can be found by viewing the corresponding certificate under 'Signing & Decryption Keys & Certificates' in the PingFederate Administrative Console.

    secondaryDecryptionKeyPairRef: ResourceLink
        The ID of the secondary key pair used to decrypt message content received from this partner.

    outboundBackChannelAuth: OutboundBackChannelAuth
        The SOAP authentication method(s) to use when you send a message using SOAP back channel.

    inboundBackChannelAuth: InboundBackChannelAuth
        The SOAP authentication method(s) to use when you receive a message using SOAP back channel.

    """
    def __init__(self, verificationSubjectDN: str = None, verificationIssuerDN: str = None, certs: list = None, blockEncryptionAlgorithm: str = None, keyTransportAlgorithm: str = None, signingSettings: SigningSettings = None, decryptionKeyPairRef: ResourceLink = None, secondaryDecryptionKeyPairRef: ResourceLink = None, outboundBackChannelAuth: OutboundBackChannelAuth = None, inboundBackChannelAuth: InboundBackChannelAuth = None) -> None:
        self.verificationSubjectDN = verificationSubjectDN
        self.verificationIssuerDN = verificationIssuerDN
        self.certs = certs
        self.blockEncryptionAlgorithm = blockEncryptionAlgorithm
        self.keyTransportAlgorithm = keyTransportAlgorithm
        self.signingSettings = signingSettings
        self.decryptionKeyPairRef = decryptionKeyPairRef
        self.secondaryDecryptionKeyPairRef = secondaryDecryptionKeyPairRef
        self.outboundBackChannelAuth = outboundBackChannelAuth
        self.inboundBackChannelAuth = inboundBackChannelAuth

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ConnectionCredentials):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.verificationSubjectDN, self.verificationIssuerDN, self.certs, self.blockEncryptionAlgorithm, self.keyTransportAlgorithm, self.signingSettings, self.decryptionKeyPairRef, self.secondaryDecryptionKeyPairRef, self.outboundBackChannelAuth, self.inboundBackChannelAuth]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["verificationSubjectDN", "verificationIssuerDN", "certs", "blockEncryptionAlgorithm", "keyTransportAlgorithm", "signingSettings", "decryptionKeyPairRef", "secondaryDecryptionKeyPairRef", "outboundBackChannelAuth", "inboundBackChannelAuth"] and v is not None:
                if k == "verificationSubjectDN":
                    valid_data[k] = str(v)
                if k == "verificationIssuerDN":
                    valid_data[k] = str(v)
                if k == "certs":
                    valid_data[k] = [ConnectionCert.from_dict(x) for x in v]
                if k == "blockEncryptionAlgorithm":
                    valid_data[k] = str(v)
                if k == "keyTransportAlgorithm":
                    valid_data[k] = str(v)
                if k == "signingSettings":
                    valid_data[k] = SigningSettings.from_dict(v)
                if k == "decryptionKeyPairRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "secondaryDecryptionKeyPairRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "outboundBackChannelAuth":
                    valid_data[k] = OutboundBackChannelAuth.from_dict(v)
                if k == "inboundBackChannelAuth":
                    valid_data[k] = InboundBackChannelAuth.from_dict(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["verificationSubjectDN", "verificationIssuerDN", "certs", "blockEncryptionAlgorithm", "keyTransportAlgorithm", "signingSettings", "decryptionKeyPairRef", "secondaryDecryptionKeyPairRef", "outboundBackChannelAuth", "inboundBackChannelAuth"]:
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
