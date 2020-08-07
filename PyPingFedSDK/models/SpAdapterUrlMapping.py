class SpAdapterUrlMapping():
    """SP Adapter URL Mapping

    Attributes
    ----------
    adapterRef : str
        The adapter instance mapped for this URL.    url : string
        The URL that will be compared against the target URL. Use a wildcard (*) to match multiple URLs to the same adapter instance.
    """

    __slots__ = ["adapterRef", "url"]

    def __init__(self, adapterRef=None, url=None):
        self.adapterRef: str = adapterRef
        self.url: str = url

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, SpAdapterUrlMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.adapterRef, self.url))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["adapterRef", "url"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__