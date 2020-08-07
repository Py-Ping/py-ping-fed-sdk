class ConnectionCredentials():
    """The certificates and settings for encryption, signing, and signature verification.

    Attributes
    ----------
    blockEncryptionAlgorithm : string
        The algorithm used to encrypt assertions sent to this partner. AES_128, AES_256 and Triple_DES are also supported. Default is AES_128    certs : array
        The certificates used for signature verification and XML encryption.    decryptionKeyPairRef : str
        The ID of the primary key pair used to decrypt message content received from this partner. The ID of the key pair is also known as the alias and can be found by viewing the corresponding certificate under 'Signing & Decryption Keys & Certificates' in the PingFederate Administrative Console.    inboundBackChannelAuth : str
        The SOAP authentication method(s) to use when you receive a message using SOAP back channel.    keyTransportAlgorithm : string
        The algorithm used to transport keys to this partner. RSA_OAEP and RSA_v15 are supported. Default is RSA_OAEP    outboundBackChannelAuth : str
        The SOAP authentication method(s) to use when you send a message using SOAP back channel.    secondaryDecryptionKeyPairRef : str
        The ID of the secondary key pair used to decrypt message content received from this partner.    signingSettings : str
        Settings related to the manner in which messages sent to the partner are digitally signed. Required for SP Connections.    verificationIssuerDN : string
        If a verification Subject DN is provided, you can optionally restrict the issuer to a specific trusted CA by specifying its DN in this field.    verificationSubjectDN : string
        If this property is set, the verification trust model is Anchored. The verification certificate must be signed by a trusted CA and included in the incoming message, and the subject DN of the expected certificate is specified in this property. If this property is not set, then a primary verification certificate must be specified in the certs array.
    """

    __slots__ = ["blockEncryptionAlgorithm", "certs", "decryptionKeyPairRef", "inboundBackChannelAuth", "keyTransportAlgorithm", "outboundBackChannelAuth", "secondaryDecryptionKeyPairRef", "signingSettings", "verificationIssuerDN", "verificationSubjectDN"]

    def __init__(self, blockEncryptionAlgorithm=None, certs=None, decryptionKeyPairRef=None, inboundBackChannelAuth=None, keyTransportAlgorithm=None, outboundBackChannelAuth=None, secondaryDecryptionKeyPairRef=None, signingSettings=None, verificationIssuerDN=None, verificationSubjectDN=None):
        self.blockEncryptionAlgorithm: str = blockEncryptionAlgorithm
        self.certs: list = certs
        self.decryptionKeyPairRef: str = decryptionKeyPairRef
        self.inboundBackChannelAuth: str = inboundBackChannelAuth
        self.keyTransportAlgorithm: str = keyTransportAlgorithm
        self.outboundBackChannelAuth: str = outboundBackChannelAuth
        self.secondaryDecryptionKeyPairRef: str = secondaryDecryptionKeyPairRef
        self.signingSettings: str = signingSettings
        self.verificationIssuerDN: str = verificationIssuerDN
        self.verificationSubjectDN: str = verificationSubjectDN

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ConnectionCredentials):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.blockEncryptionAlgorithm, self.certs, self.decryptionKeyPairRef, self.inboundBackChannelAuth, self.keyTransportAlgorithm, self.outboundBackChannelAuth, self.secondaryDecryptionKeyPairRef, self.signingSettings, self.verificationIssuerDN, self.verificationSubjectDN))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["blockEncryptionAlgorithm", "certs", "decryptionKeyPairRef", "inboundBackChannelAuth", "keyTransportAlgorithm", "outboundBackChannelAuth", "secondaryDecryptionKeyPairRef", "signingSettings", "verificationIssuerDN", "verificationSubjectDN"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__