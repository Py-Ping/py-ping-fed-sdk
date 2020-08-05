class LdapTagConfig():
    """ An LDAP data store's hostnames and tags configuration. This is required if no default hostname is specified.

    Attributes
    ----------
    defaultSource : boolean
        Whether this is the default connection. Defaults to false if not specified.
    hostnames : array
        The LDAP host names.
    tags : string
        Tags associated with this data source.

    """

    __slots__ = ["defaultSource", "hostnames", "tags"]
    def __init__(self, hostnames, defaultSource=None, tags=None):
            self.defaultSource = defaultSource
            self.hostnames = hostnames
            self.tags = tags
    
    def _validate(self):
        return any(x for x in ['hostnames'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, LdapTagConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((defaultSource, hostnames, tags))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
