class ScopeEntry():
    """ A scope name and its description.

    Attributes
    ----------
    description : string
        The description of the scope that appears when the user is prompted for authorization.
    dynamic : boolean
        True if the scope is dynamic. (Defaults to false)
    name : string
        The name of the scope.

    """

    __slots__ = ["description", "dynamic", "name"]
    def __init__(self, name, description, dynamic=None):
            self.description = description
            self.dynamic = dynamic
            self.name = name
    
    def _validate(self):
        return any(x for x in ['name', 'description'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ScopeEntry):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((description, dynamic, name))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
