class ProfileConfig():
    """ A local identity profile management configuration.

    Attributes
    ----------
    deleteIdentityEnabled : boolean
        Whether the end user is allowed to use delete functionality.
    templateName : string
        The template name for end-user profile management.

    """

    __slots__ = ["deleteIdentityEnabled", "templateName"]
    def __init__(self, templateName, deleteIdentityEnabled=None):
            self.deleteIdentityEnabled = deleteIdentityEnabled
            self.templateName = templateName
    
    def _validate(self):
        return any(x for x in ['templateName'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ProfileConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((deleteIdentityEnabled, templateName))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
