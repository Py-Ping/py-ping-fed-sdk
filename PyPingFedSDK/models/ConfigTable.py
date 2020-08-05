class ConfigTable():
    """ A plugin configuration table populated with values.

    Attributes
    ----------
    inherited : boolean
        Whether this table is inherited from its parent instance. If true, the rows become read-only. The default value is false.
    name : string
        The name of the table.
    rows : array
        List of table rows.

    """

    __slots__ = ["inherited", "name", "rows"]
    def __init__(self, name, inherited=None, rows=None):
            self.inherited = inherited
            self.name = name
            self.rows = rows
    
    def _validate(self):
        return any(x for x in ['name'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ConfigTable):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((inherited, name, rows))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
