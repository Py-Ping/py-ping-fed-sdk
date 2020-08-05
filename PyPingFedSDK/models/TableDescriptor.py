class TableDescriptor():
    """ Defines a plugin configuration table.

    Attributes
    ----------
    columns : array
        Get the columns in the table.
    description : string
        Description for the table.
    label : string
        Label for the table to be displayed in the administrative console.
    name : string
        The name of the table.
    requireDefaultRow : boolean
        Configure whether this table requires default row to be set.

    """

    __slots__ = ["columns", "description", "label", "name", "requireDefaultRow"]
    def __init__(self, columns=None, description=None, label=None, name=None, requireDefaultRow=None):
            self.columns = columns
            self.description = description
            self.label = label
            self.name = name
            self.requireDefaultRow = requireDefaultRow
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, TableDescriptor):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((columns, description, label, name, requireDefaultRow))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
