class StsRequestParametersContract():
    """ A Security Token Service request parameter contract.

    Attributes
    ----------
    id : string
        The ID of the Security Token Service request parameter contract.<br>Note: Ignored for PUT requests.
    name : string
        The name of the Security Token Service request parameter contract.<br>Note: Ignored for PUT requests.
    parameters : array
        The list of parameters within the Security  Token Service request parameter contract.

    """

    __slots__ = ["id", "name", "parameters"]
    def __init__(self, id, name, parameters):
            self.id = id
            self.name = name
            self.parameters = parameters
    
    def _validate(self):
        return any(x for x in ['id', 'name', 'parameters'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, StsRequestParametersContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((id, name, parameters))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
