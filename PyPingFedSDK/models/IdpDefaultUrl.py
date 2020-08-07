class IdpDefaultUrl():
    """IDP Default URL settings.

    Attributes
    ----------
    confirmIdpSlo : boolean
 Prompt user to confirm Single Logout (SLO).
    idpErrorMsg : string
 Provide the error text displayed in a user's browser when an SSO operation fails.
    idpSloSuccessUrl : string
 Provide the default URL you would like to send the user to when Single Logout has succeeded.

    """

    def __init__(self, idpErrorMsg, confirmIdpSlo=None, idpSloSuccessUrl=None) -> None:
        self.confirmIdpSlo = confirmIdpSlo
        self.idpErrorMsg = idpErrorMsg
        self.idpSloSuccessUrl = idpSloSuccessUrl

    def _validate(self) -> bool:
        return any(x for x in ["idpErrorMsg"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpDefaultUrl):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.confirmIdpSlo, self.idpErrorMsg, self.idpSloSuccessUrl))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["confirmIdpSlo", "idpErrorMsg", "idpSloSuccessUrl"]}

        return cls(**valid_data)