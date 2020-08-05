class AuthnApiApplication():
    """Authentication API Application.

    Attributes
    ----------
    additionalAllowedOrigins : array
        The domain in the redirect URL is always whitelisted. This field contains a list of additional allowed origin URL's for cross-origin resource sharing.    description : string
        The Authentication API Application description.    id : string
        The persistent, unique ID for the Authentication API application. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.    name : string
        The Authentication API Application Name. Name must be unique.    url : string
        The Authentication API Application redirect URL.
    """

    __slots__ = ["additionalAllowedOrigins", "description", "id", "name", "url"]

    def __init__(self, id, name, url, additionalAllowedOrigins=None, description=None):
        self.additionalAllowedOrigins = additionalAllowedOrigins
        self.description = description
        self.id = id
        self.name = name
        self.url = url

    def _validate(self):
        return any(x for x in ['id', 'name', 'url'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AuthnApiApplication):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.additionalAllowedOrigins, self.description, self.id, self.name, self.url))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["additionalAllowedOrigins", "description", "id", "name", "url"]}

        return cls(**valid_data)
