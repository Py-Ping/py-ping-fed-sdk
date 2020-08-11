class ConfigRow():
    """A row of configuration values for a plugin configuration table.

    Attributes
    ----------
    defaultRow : boolean
        Whether this row is the default.
    fields : array
        The configuration fields in the row.

    """

    def __init__(self, fields:list, defaultRow:bool=None) -> None:
        self.defaultRow = defaultRow
        self.fields = fields

    def _validate(self) -> bool:
        return any(x for x in ["fields"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ConfigRow):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.defaultRow, self.fields))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["defaultRow", "fields"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__