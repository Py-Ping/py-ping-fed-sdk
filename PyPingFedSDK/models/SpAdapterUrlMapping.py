class SpAdapterUrlMapping():
    """SP Adapter URL Mapping

    Attributes
    ----------
    adapterRef : str
        The adapter instance mapped for this URL.
    url : string
        The URL that will be compared against the target URL. Use a wildcard (*) to match multiple URLs to the same adapter instance.

    """

    def __init__(self, adapterRef=None, url:str=None) -> None:
        self.adapterRef = adapterRef
        self.url = url

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SpAdapterUrlMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.adapterRef, self.url]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["adapterRef", "url"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__