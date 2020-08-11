class ConfigTable():
    """A plugin configuration table populated with values.

    Attributes
    ----------
    inherited : boolean
        Whether this table is inherited from its parent instance. If true, the rows become read-only. The default value is false.
    name : string
        The name of the table.
    rows : array
        List of table rows.

    """

    def __init__(self, name:str, inherited:bool=None, rows:list=None) -> None:
        self.inherited = inherited
        self.name = name
        self.rows = rows

    def _validate(self) -> bool:
        return any(x for x in ["name"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ConfigTable):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.inherited, self.name, self.rows))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["inherited", "name", "rows"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__