class UserCredentials():
    """Credentials for an administrator account.

    Attributes
    ----------
    currentPassword : string
 Current password. Required only during Password Change and not applicable for Password Reset.
    newPassword : string
 A new password.

    """

    def __init__(self, newPassword:str, currentPassword:str=None) -> None:
        self.currentPassword = currentPassword
        self.newPassword = newPassword

    def _validate(self) -> bool:
        return any(x for x in ["newPassword"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, UserCredentials):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.currentPassword, self.newPassword))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["currentPassword", "newPassword"]}

        return cls(**valid_data)