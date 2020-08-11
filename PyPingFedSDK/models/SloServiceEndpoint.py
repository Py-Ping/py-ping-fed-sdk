class SloServiceEndpoint():
    """Where SLO logout messages are sent. Only applicable for SAML 2.0.

    Attributes
    ----------
    binding : str
 The binding of this endpoint, if applicable - usually only required for SAML 2.0 endpoints.
    responseUrl : string
 The absolute or relative URL to which logout responses are sent. A relative URL can be specified if a base URL for the connection has been defined.
    url : string
 The absolute or relative URL of the endpoint. A relative URL can be specified if a base URL for the connection has been defined.

    """

    def __init__(self, binding, url:str, responseUrl:str=None) -> None:
        self.binding = binding
        self.responseUrl = responseUrl
        self.url = url

    def _validate(self) -> bool:
        return any(x for x in ["binding", "url"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SloServiceEndpoint):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.binding, self.responseUrl, self.url))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["binding", "responseUrl", "url"]}

        return cls(**valid_data)