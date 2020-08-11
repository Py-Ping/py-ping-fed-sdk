class ClientSettings():
    """The client settings.

    Attributes
    ----------
    clientMetadata : array
        The client metadata.
    dynamicClientRegistration : str
        Dynamic client registration settings.

    """

    def __init__(self, clientMetadata:list=None, dynamicClientRegistration=None) -> None:
        self.clientMetadata = clientMetadata
        self.dynamicClientRegistration = dynamicClientRegistration

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ClientSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.clientMetadata, self.dynamicClientRegistration))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["clientMetadata", "dynamicClientRegistration"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__