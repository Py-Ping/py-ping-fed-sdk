class VirtualHostNameSettings():
    """Settings for virtual host names.

    Attributes
    ----------
    virtualHostNames : array
        List of virtual host names.
    """

    __slots__ = ["virtualHostNames"]

    def __init__(self, virtualHostNames=None):
        self.virtualHostNames = virtualHostNames

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, VirtualHostNameSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.virtualHostNames))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["virtualHostNames"]}

        return cls(**valid_data)
