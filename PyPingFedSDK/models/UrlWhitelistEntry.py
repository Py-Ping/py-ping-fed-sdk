class UrlWhitelistEntry():
    """ Url domain and path to be used as whitelist in WS-Federation connection

    Attributes
    ----------
    allowQueryAndFragment : boolean
        Allow Any Query/Fragment
    requireHttps : boolean
        Require HTTPS
    validDomain : string
        Valid Domain Name (leading wildcard '*.' allowed)
    validPath : string
        Valid Path (leave blank to allow any path)

    """

    __slots__ = ["allowQueryAndFragment", "requireHttps", "validDomain", "validPath"]
    def __init__(self, allowQueryAndFragment=None, requireHttps=None, validDomain=None, validPath=None):
            self.allowQueryAndFragment = allowQueryAndFragment
            self.requireHttps = requireHttps
            self.validDomain = validDomain
            self.validPath = validPath
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, UrlWhitelistEntry):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((allowQueryAndFragment, requireHttps, validDomain, validPath))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
