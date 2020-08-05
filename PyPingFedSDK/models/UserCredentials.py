class UserCredentials():
    """Credentials for an administrator account.

    Attributes
    ----------
    currentPassword : string
        Current password. Required only during Password Change and not applicable for Password Reset.    newPassword : string
        A new password.
    """

    __slots__ = ["currentPassword", "newPassword"]

    def __init__(self, newPassword, currentPassword=None):
        self.currentPassword = currentPassword
        self.newPassword = newPassword

    def _validate(self):
        return any(x for x in ['newPassword'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, UserCredentials):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.currentPassword, self.newPassword))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["currentPassword", "newPassword"]}

        return cls(**valid_data)
