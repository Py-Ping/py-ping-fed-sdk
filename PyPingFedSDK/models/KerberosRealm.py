class KerberosRealm():
    """

    Attributes
    ----------
    id : string
 The persistent, unique ID for the Kerberos Realm. It can be any combination of [a-z0-9._-]. This property is system-assigned if not specified.
    kerberosEncryptedPassword : string
 For GET requests, this field contains the encrypted Domain/Realm password, if one exists. For POST and PUT requests, if you wish to reuse the existing password, this field should be passed back unchanged.
    kerberosPassword : string
 The Domain/Realm password. GETs will not return this attribute. To update this field, specify the new value in this attribute.
    kerberosRealmName : string
 The Domain/Realm name used for display in UI screens.
    kerberosUsername : string
 The Domain/Realm username.
    keyDistributionCenters : array
 The Domain Controller/Key Distribution Center Host Action Names.
    suppressDomainNameConcatenation : boolean
 Controls whether the KDC hostnames and the realm name are concatenated in the auto-generated krb5.conf file. Default is false.

    """

<<<<<<< HEAD
    def __init__(self, kerberosRealmName, kerberosUsername, var_id=None, kerberosEncryptedPassword=None, kerberosPassword=None, keyDistributionCenters=None, suppressDomainNameConcatenation=None) -> None:
        self.var_id = var_id
        self.kerberosEncryptedPassword = kerberosEncryptedPassword
        self.kerberosPassword = kerberosPassword
        self.kerberosRealmName = kerberosRealmName
        self.kerberosUsername = kerberosUsername
        self.keyDistributionCenters = keyDistributionCenters
        self.suppressDomainNameConcatenation = suppressDomainNameConcatenation
=======
    def __init__(self, kerberosRealmName, kerberosUsername, id=None, kerberosEncryptedPassword=None, kerberosPassword=None, keyDistributionCenters=None, suppressDomainNameConcatenation=None):
        self.id: str = id
        self.kerberosEncryptedPassword: str = kerberosEncryptedPassword
        self.kerberosPassword: str = kerberosPassword
        self.kerberosRealmName: str = kerberosRealmName
        self.kerberosUsername: str = kerberosUsername
        self.keyDistributionCenters: list = keyDistributionCenters
        self.suppressDomainNameConcatenation: bool = suppressDomainNameConcatenation
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["kerberosRealmName", "kerberosUsername"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, KerberosRealm):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.var_id, self.kerberosEncryptedPassword, self.kerberosPassword, self.kerberosRealmName, self.kerberosUsername, self.keyDistributionCenters, self.suppressDomainNameConcatenation))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["var_id", "kerberosEncryptedPassword", "kerberosPassword", "kerberosRealmName", "kerberosUsername", "keyDistributionCenters", "suppressDomainNameConcatenation"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
