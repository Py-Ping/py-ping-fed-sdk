class IdpSsoServiceEndpoint():
    """The settings that define an endpoint to an IdP SSO service.

    Attributes
    ----------
    binding : str
        The binding of this endpoint, if applicable - usually only required for SAML 2.0 endpoints.    url : string
        The absolute or relative URL of the endpoint. A relative URL can be specified if a base URL for the connection has been defined.
    """

    __slots__ = ["binding", "url"]

    def __init__(self, binding, url):
        self.binding: str = binding
        self.url: str = url

    def _validate(self):
        return any(x for x in ['binding', 'url'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, IdpSsoServiceEndpoint):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.binding, self.url))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["binding", "url"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__