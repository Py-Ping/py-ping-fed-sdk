class SpUrlMapping():
    """SP URL mapping

    Attributes
    ----------
    ref : str
        The adapter or connection instance mapped for this URL.
    type : str
        The URL mapping type
    url : string
        The URL that will be compared against the target URL. Use a wildcard (*) to match multiple URLs to the same adapter or connection instance.

    """

    def __init__(self, ref=None, var_type=None, url:str=None) -> None:
        self.ref = ref
        self.var_type = var_type
        self.url = url

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SpUrlMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.ref, self.var_type, self.url]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["ref", "var_type", "url"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__