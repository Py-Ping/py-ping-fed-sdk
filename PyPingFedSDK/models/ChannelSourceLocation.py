class ChannelSourceLocation():
    """The location settings that includes a DN and a LDAP filter.

    Attributes
    ----------
    filter : string
 An LDAP filter.
    groupDN : string
 The group DN for users or groups.
    nestedSearch : boolean
 Indicates whether the search is nested.

    """

<<<<<<< HEAD
    def __init__(self, filter=None, groupDN=None, nestedSearch=None) -> None:
        self.filter = filter
        self.groupDN = groupDN
        self.nestedSearch = nestedSearch
=======
    def __init__(self, filter=None, groupDN=None, nestedSearch=None):
        self.filter: str = filter
        self.groupDN: str = groupDN
        self.nestedSearch: bool = nestedSearch
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ChannelSourceLocation):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.filter, self.groupDN, self.nestedSearch))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["filter", "groupDN", "nestedSearch"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
