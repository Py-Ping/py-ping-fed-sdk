class DataSourceTag():
    """

    Attributes
    ----------
    defaultSource : boolean
    tags : string
    tagsHashSet : str

    """

    __slots__ = ["defaultSource", "tags", "tagsHashSet"]

    def __init__(self, defaultSource=None, tags=None, tagsHashSet=None):
        self.defaultSource: bool = defaultSource
        self.tags: str = tags
        self.tagsHashSet: str = tagsHashSet

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, DataSourceTag):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.defaultSource, self.tags, self.tagsHashSet))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["defaultSource", "tags", "tagsHashSet"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__