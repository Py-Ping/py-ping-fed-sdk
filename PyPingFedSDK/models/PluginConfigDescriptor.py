class PluginConfigDescriptor():
    """Defines the configuration fields available for a plugin.

    Attributes
    ----------
    actionDescriptors : array
        The available actions for this plugin.    description : string
        The description of this plugin.    fields : array
        The configuration fields available for this plugin.    tables : array
        Configuration tables available for this plugin.
    """

    __slots__ = ["actionDescriptors", "description", "fields", "tables"]

    def __init__(self, actionDescriptors=None, description=None, fields=None, tables=None):
        self.actionDescriptors: list = actionDescriptors
        self.description: str = description
        self.fields: list = fields
        self.tables: list = tables

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, PluginConfigDescriptor):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.actionDescriptors, self.description, self.fields, self.tables))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["actionDescriptors", "description", "fields", "tables"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__