class AuthnContextMapping():
    """The authentication context mapping between local and remote values.

    Attributes
    ----------
    local : string
        The local authentication context value.    remote : string
        The remote authentication context value.
    """

    __slots__ = ["local", "remote"]

    def __init__(self, local=None, remote=None):
        self.local = local
        self.remote = remote

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AuthnContextMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.local, self.remote))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["local", "remote"]}

        return cls(**valid_data)
