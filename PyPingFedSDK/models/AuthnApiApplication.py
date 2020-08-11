class AuthnApiApplication():
    """Authentication API Application.

    Attributes
    ----------
    additionalAllowedOrigins : array
        The domain in the redirect URL is always whitelisted. This field contains a list of additional allowed origin URL's for cross-origin resource sharing.
    description : string
        The Authentication API Application description.
    id : string
        The persistent, unique ID for the Authentication API application. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.
    name : string
        The Authentication API Application Name. Name must be unique.
    url : string
        The Authentication API Application redirect URL.

    """

    def __init__(self, var_id:str, name:str, url:str, additionalAllowedOrigins:list=None, description:str=None) -> None:
        self.additionalAllowedOrigins = additionalAllowedOrigins
        self.description = description
        self.var_id = var_id
        self.name = name
        self.url = url

    def _validate(self) -> bool:
        return any(x for x in ["var_id", "name", "url"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthnApiApplication):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.additionalAllowedOrigins, self.description, self.var_id, self.name, self.url))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["additionalAllowedOrigins", "description", "var_id", "name", "url"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__