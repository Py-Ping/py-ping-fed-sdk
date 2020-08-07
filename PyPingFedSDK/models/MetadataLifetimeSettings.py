class MetadataLifetimeSettings():
    """Metadata lifetime settings.

    Attributes
    ----------
    cacheDuration : integer
        This field adjusts the validity of your metadata in minutes. The default value is 1440 (1 day).    reloadDelay : integer
        This field adjusts the frequency of automatic reloading of SAML metadata in minutes. The default value is 1440 (1 day).
    """

    __slots__ = ["cacheDuration", "reloadDelay"]

    def __init__(self, cacheDuration=None, reloadDelay=None):
        self.cacheDuration: str = cacheDuration
        self.reloadDelay: str = reloadDelay

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, MetadataLifetimeSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.cacheDuration, self.reloadDelay))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["cacheDuration", "reloadDelay"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__