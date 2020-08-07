class SslServerSettings():
    """Settings for the SSL Server certificate configuration.

    Attributes
    ----------
    activeAdminConsoleCerts : array
        The active SSL Server Certificate Key pairs for PF Administrator Console.    activeRuntimeServerCerts : array
        The active SSL Server Certificate Key pairs for Runtime Server.    adminConsoleCertRef : str
        Reference to the default SSL Server Certificate Key pair active for PF Administrator Console.    runtimeServerCertRef : str
        Reference to the default SSL Server Certificate Key pair active for Runtime Server.
    """

    __slots__ = ["activeAdminConsoleCerts", "activeRuntimeServerCerts", "adminConsoleCertRef", "runtimeServerCertRef"]

    def __init__(self, runtimeServerCertRef, adminConsoleCertRef, activeAdminConsoleCerts=None, activeRuntimeServerCerts=None):
        self.activeAdminConsoleCerts: list = activeAdminConsoleCerts
        self.activeRuntimeServerCerts: list = activeRuntimeServerCerts
        self.adminConsoleCertRef: str = adminConsoleCertRef
        self.runtimeServerCertRef: str = runtimeServerCertRef

    def _validate(self):
        return any(x for x in ['runtimeServerCertRef', 'adminConsoleCertRef'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, SslServerSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.activeAdminConsoleCerts, self.activeRuntimeServerCerts, self.adminConsoleCertRef, self.runtimeServerCertRef))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["activeAdminConsoleCerts", "activeRuntimeServerCerts", "adminConsoleCertRef", "runtimeServerCertRef"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__