class AccessTokenManagementSettings():
    """General access token management settings.

    Attributes
    ----------
    defaultAccessTokenManagerRef : str
 Reference to the default access token manager, if one is defined.

    """

    def __init__(self, defaultAccessTokenManagerRef=None) -> None:
        self.defaultAccessTokenManagerRef = defaultAccessTokenManagerRef

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AccessTokenManagementSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.defaultAccessTokenManagerRef))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["defaultAccessTokenManagerRef"]}

        return cls(**valid_data)