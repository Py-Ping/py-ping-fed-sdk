class AdministrativeAccount():
    """A PingFederate administrator account.

    Attributes
    ----------
    active : boolean
 Indicates whether the account is active or not.
    auditor : boolean
 Indicates whether the account belongs to an Auditor. An Auditor has View-only permissions for all administrative functions. An Auditor cannot have any administrative roles.
    department : string
 The Department name of account user.
    description : string
 Description of the account.
    emailAddress : string
 Email address associated with the account.
    encryptedPassword : string
 For GET requests, this field contains the encrypted account password. For POST and PUT requests, if you wish to re-use the password from an API response to this endpoint, this field should be passed back unchanged.
    password : string
 Password for the Account. This field is only applicable during a POST operation.
    phoneNumber : string
 Phone number associated with the account.
    roles : str
 Roles available for an administrator. <br>USER_ADMINISTRATOR - Can create, deactivate or delete accounts and reset passwords. Additionally, install replacement license keys. <br> CRYPTO_ADMINISTRATOR - Can manage local keys and certificates. <br> ADMINISTRATOR - Can configure partner connections and most system settings (except the management of native accounts and the handling of local keys and certificates. <br>
    username : string
 Username for the Administrative Account.

    """

    def __init__(self, username:str, active:bool=None, auditor:bool=None, department:str=None, description:str=None, emailAddress:str=None, encryptedPassword:str=None, password:str=None, phoneNumber:str=None, roles=None) -> None:
        self.active = active
        self.auditor = auditor
        self.department = department
        self.description = description
        self.emailAddress = emailAddress
        self.encryptedPassword = encryptedPassword
        self.password = password
        self.phoneNumber = phoneNumber
        self.roles = roles
        self.username = username

    def _validate(self) -> bool:
        return any(x for x in ["username"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AdministrativeAccount):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.active, self.auditor, self.department, self.description, self.emailAddress, self.encryptedPassword, self.password, self.phoneNumber, self.roles, self.username))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["active", "auditor", "department", "description", "emailAddress", "encryptedPassword", "password", "phoneNumber", "roles", "username"]}

        return cls(**valid_data)