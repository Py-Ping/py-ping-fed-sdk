class DataSourceTag():
    """

    Attributes
    ----------
    defaultSource : boolean
    tags : string
    tagsHashSet : str

    """

    def __init__(self, defaultSource:bool=None, tags:str=None, tagsHashSet=None) -> None:
        self.defaultSource = defaultSource
        self.tags = tags
        self.tagsHashSet = tagsHashSet

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, DataSourceTag):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.defaultSource, self.tags, self.tagsHashSet]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["defaultSource", "tags", "tagsHashSet"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__