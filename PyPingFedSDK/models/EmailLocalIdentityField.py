class EmailLocalIdentityField():
    """ An email type field.

    Attributes
    ----------
    attributes : str
        Attributes of the local identity field.
    id : string
        Id of the local identity field.
    label : string
        Label of the local identity field.
    profilePageField : boolean
        Whether this is a profile page field or not.
    registrationPageField : boolean
        Whether this is a registration page field or not.
    type : str
        The type of the local identity field.

    """

    __slots__ = ["attributes", "id", "label", "profilePageField", "registrationPageField", "type"]
    def __init__(self, type, id, label, attributes=None, profilePageField=None, registrationPageField=None):
            self.attributes = attributes
            self.id = id
            self.label = label
            self.profilePageField = profilePageField
            self.registrationPageField = registrationPageField
            self.type = type
    
    def _validate(self):
        return any(x for x in ['type', 'id', 'label'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, EmailLocalIdentityField):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((attributes, id, label, profilePageField, registrationPageField, type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
