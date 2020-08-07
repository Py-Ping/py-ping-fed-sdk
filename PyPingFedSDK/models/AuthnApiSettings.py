class AuthnApiSettings():
    """Authentication API Application Settings.

    Attributes
    ----------
    apiEnabled : boolean
 Specifies whether the authentication API is enabled. The default value is false.
    defaultApplicationRef : str
 Application for non authentication policy use cases.
    enableApiDescriptions : boolean
 Enable the API Descriptions endpoint.

    """

<<<<<<< HEAD
    def __init__(self, apiEnabled=None, defaultApplicationRef=None, enableApiDescriptions=None) -> None:
        self.apiEnabled = apiEnabled
        self.defaultApplicationRef = defaultApplicationRef
        self.enableApiDescriptions = enableApiDescriptions
=======
    def __init__(self, apiEnabled=None, defaultApplicationRef=None, enableApiDescriptions=None):
        self.apiEnabled: bool = apiEnabled
        self.defaultApplicationRef: str = defaultApplicationRef
        self.enableApiDescriptions: bool = enableApiDescriptions
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthnApiSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.apiEnabled, self.defaultApplicationRef, self.enableApiDescriptions))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["apiEnabled", "defaultApplicationRef", "enableApiDescriptions"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
