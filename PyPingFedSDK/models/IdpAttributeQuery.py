class IdpAttributeQuery():
    """The attribute query profile supports local applications in requesting user attributes from an attribute authority.

    Attributes
    ----------
    nameMappings : array
        The attribute name mappings between the SP and the IdP.    policy : str
        The attribute query profile's security policy.    url : string
        The URL at your IdP partner's site where attribute queries are to be sent.
    """

    __slots__ = ["nameMappings", "policy", "url"]

    def __init__(self, url, nameMappings=None, policy=None):
        self.nameMappings = nameMappings
        self.policy = policy
        self.url = url

    def _validate(self):
        return any(x for x in ['url'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, IdpAttributeQuery):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.nameMappings, self.policy, self.url))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["nameMappings", "policy", "url"]}

        return cls(**valid_data)
