from enum import Enum

from pingfedsdk.model import Model


class AdministrativeAccount(Model):
    """A PingFederate administrator account.

    Attributes
    ----------
    username: str
        Username for the Administrative Account.

    password: str
        Password for the Account. This field is only applicable during a POST operation.

    encryptedPassword: str
        For GET requests, this field contains the encrypted account password. For POST and PUT requests, if you wish to re-use the password from an API response to this endpoint, this field should be passed back unchanged.

    active: bool
        Indicates whether the account is active or not.

    description: str
        Description of the account.

    auditor: bool
        Indicates whether the account belongs to an Auditor. An Auditor has View-only permissions for all administrative functions. An Auditor cannot have any administrative roles.

    phoneNumber: str
        Phone number associated with the account.

    emailAddress: str
        Email address associated with the account.

    department: str
        The Department name of account user.

    roles: list
        Roles available for an administrator.
        USER_ADMINISTRATOR - Can create, deactivate or delete accounts and reset passwords. Additionally, install replacement license keys.
         CRYPTO_ADMINISTRATOR - Can manage local keys and certificates.
         ADMINISTRATOR - Can configure partner connections and most system settings (except the management of native accounts and the handling of local keys and certificates.
        EXPRESSION_ADMINISTRATOR - Can add and update OGNL expressions.

    """
    def __init__(self, username: str, password: str = None, encryptedPassword: str = None, active: bool = None, description: str = None, auditor: bool = None, phoneNumber: str = None, emailAddress: str = None, department: str = None, roles: list = None) -> None:
        self.username = username
        self.password = password
        self.encryptedPassword = encryptedPassword
        self.active = active
        self.description = description
        self.auditor = auditor
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.department = department
        self.roles = roles

    def _validate(self) -> bool:
        return any(x for x in ["username"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AdministrativeAccount):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.username, self.password, self.encryptedPassword, self.active, self.description, self.auditor, self.phoneNumber, self.emailAddress, self.department, self.roles]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["username", "password", "encryptedPassword", "active", "description", "auditor", "phoneNumber", "emailAddress", "department", "roles"] and v is not None:
                if k == "username":
                    valid_data[k] = str(v)
                if k == "password":
                    valid_data[k] = str(v)
                if k == "encryptedPassword":
                    valid_data[k] = str(v)
                if k == "active":
                    valid_data[k] = bool(v)
                if k == "description":
                    valid_data[k] = str(v)
                if k == "auditor":
                    valid_data[k] = bool(v)
                if k == "phoneNumber":
                    valid_data[k] = str(v)
                if k == "emailAddress":
                    valid_data[k] = str(v)
                if k == "department":
                    valid_data[k] = str(v)
                if k == "roles":
                    valid_data[k] = [str(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["username", "password", "encryptedPassword", "active", "description", "auditor", "phoneNumber", "emailAddress", "department", "roles"]:
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
