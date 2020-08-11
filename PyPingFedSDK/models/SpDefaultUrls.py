class SpDefaultUrls():
    """SP Default URLs.

    Attributes
    ----------
    confirmSlo : boolean
        Determines whether the user is prompted to confirm Single Logout (SLO). The default is false.
    sloSuccessUrl : string
        Provide the default URL you would like to send the user to when Single Logout (SLO) has succeeded.
    ssoSuccessUrl : string
        Provide the default URL you would like to send the user to when Single Sign On (SSO) has succeeded.

    """

    def __init__(self, confirmSlo:bool=None, sloSuccessUrl:str=None, ssoSuccessUrl:str=None) -> None:
        self.confirmSlo = confirmSlo
        self.sloSuccessUrl = sloSuccessUrl
        self.ssoSuccessUrl = ssoSuccessUrl

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SpDefaultUrls):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.confirmSlo, self.sloSuccessUrl, self.ssoSuccessUrl]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["confirmSlo", "sloSuccessUrl", "ssoSuccessUrl"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__