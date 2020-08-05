class PluginConfiguration():
    """Configuration settings for a plugin instance.

    Attributes
    ----------
    fields : array
        List of configuration fields.    tables : array
        List of configuration tables.
    """

    __slots__ = ["fields", "tables"]

    def __init__(self, fields=None, tables=None):
        self.fields = fields
        self.tables = tables

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, PluginConfiguration):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.fields, self.tables))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["fields", "tables"]}

        return cls(**valid_data)
