class SpSsoServiceEndpoint():
    """The settings that define a service endpoint to a SP SSO service.

    Attributes
    ----------
    binding : str
 The binding of this endpoint, if applicable - usually only required for SAML 2.0 endpoints.  Supported bindings are Artifact and POST.
    index : integer
 The priority of the endpoint.
    isDefault : boolean
 Whether or not this endpoint is the default endpoint. Defaults to false.
    url : string
 The absolute or relative URL of the endpoint. A relative URL can be specified if a base URL for the connection has been defined.

    """

<<<<<<< HEAD
    def __init__(self, binding, url, index, isDefault=None) -> None:
        self.binding = binding
        self.index = index
        self.isDefault = isDefault
        self.url = url
=======
    def __init__(self, binding, url, index, isDefault=None):
        self.binding: str = binding
        self.index: str = index
        self.isDefault: bool = isDefault
        self.url: str = url
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["binding", "url", "index"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SpSsoServiceEndpoint):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.binding, self.index, self.isDefault, self.url))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["binding", "index", "isDefault", "url"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
