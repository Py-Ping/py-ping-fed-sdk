class SpUrlMapping():
    """SP URL mapping

    Attributes
    ----------
    ref : str
        The adapter or connection instance mapped for this URL.    type : str
        The URL mapping type    url : string
        The URL that will be compared against the target URL. Use a wildcard (*) to match multiple URLs to the same adapter or connection instance.
    """

    __slots__ = ["ref", "type", "url"]

    def __init__(self, ref=None, type=None, url=None):
        self.ref: str = ref
        self.type: str = type
        self.url: str = url

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, SpUrlMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.ref, self.type, self.url))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["ref", "type", "url"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__