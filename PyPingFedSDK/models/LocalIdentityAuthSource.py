class LocalIdentityAuthSource():
    """An authentication source name.

    Attributes
    ----------
    id : string
        The persistent, unique ID for the local identity authentication source. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.    source : string
        The local identity authentication source. Source is unique.
    """

    __slots__ = ["id", "source"]

    def __init__(self, id=None, source=None):
        self.id: str = id
        self.source: str = source

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, LocalIdentityAuthSource):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.id, self.source))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["id", "source"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__