class AuthnApiSettings():
    """Authentication API Application Settings.

    Attributes
    ----------
    apiEnabled : boolean
        Specifies whether the authentication API is enabled. The default value is false.    defaultApplicationRef : str
        Application for non authentication policy use cases.    enableApiDescriptions : boolean
        Enable the API Descriptions endpoint.
    """

    __slots__ = ["apiEnabled", "defaultApplicationRef", "enableApiDescriptions"]

    def __init__(self, apiEnabled=None, defaultApplicationRef=None, enableApiDescriptions=None):
        self.apiEnabled = apiEnabled
        self.defaultApplicationRef = defaultApplicationRef
        self.enableApiDescriptions = enableApiDescriptions

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AuthnApiSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.apiEnabled, self.defaultApplicationRef, self.enableApiDescriptions))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["apiEnabled", "defaultApplicationRef", "enableApiDescriptions"]}

        return cls(**valid_data)
