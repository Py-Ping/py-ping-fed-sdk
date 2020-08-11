class IdpAttributeQuery():
    """The attribute query profile supports local applications in requesting user attributes from an attribute authority.

    Attributes
    ----------
    nameMappings : array
 The attribute name mappings between the SP and the IdP.
    policy : str
 The attribute query profile's security policy.
    url : string
 The URL at your IdP partner's site where attribute queries are to be sent.

    """

    def __init__(self, url:str, nameMappings:list=None, policy=None) -> None:
        self.nameMappings = nameMappings
        self.policy = policy
        self.url = url

    def _validate(self) -> bool:
        return any(x for x in ["url"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpAttributeQuery):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.nameMappings, self.policy, self.url))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["nameMappings", "policy", "url"]}

        return cls(**valid_data)