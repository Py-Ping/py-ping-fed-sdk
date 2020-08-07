class LdapTagConfig():
    """An LDAP data store's hostnames and tags configuration. This is required if no default hostname is specified.

    Attributes
    ----------
    defaultSource : boolean
 Whether this is the default connection. Defaults to false if not specified.
    hostnames : array
 The LDAP host names.
    tags : string
 Tags associated with this data source.

    """

    def __init__(self, hostnames, defaultSource=None, tags=None) -> None:
        self.defaultSource = defaultSource
        self.hostnames = hostnames
        self.tags = tags

    def _validate(self) -> bool:
        return any(x for x in ["hostnames"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, LdapTagConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.defaultSource, self.hostnames, self.tags))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["defaultSource", "hostnames", "tags"]}

        return cls(**valid_data)