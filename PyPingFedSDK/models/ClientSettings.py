class ClientSettings():
    """The client settings.

    Attributes
    ----------
    clientMetadata : array
        The client metadata.    dynamicClientRegistration : str
        Dynamic client registration settings.
    """

    __slots__ = ["clientMetadata", "dynamicClientRegistration"]

    def __init__(self, clientMetadata=None, dynamicClientRegistration=None):
        self.clientMetadata: list = clientMetadata
        self.dynamicClientRegistration: str = dynamicClientRegistration

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ClientSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.clientMetadata, self.dynamicClientRegistration))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["clientMetadata", "dynamicClientRegistration"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__