class ProfileConfig():
    """A local identity profile management configuration.

    Attributes
    ----------
    deleteIdentityEnabled : boolean
 Whether the end user is allowed to use delete functionality.
    templateName : string
 The template name for end-user profile management.

    """

<<<<<<< HEAD
    def __init__(self, templateName, deleteIdentityEnabled=None) -> None:
        self.deleteIdentityEnabled = deleteIdentityEnabled
        self.templateName = templateName
=======
    def __init__(self, templateName, deleteIdentityEnabled=None):
        self.deleteIdentityEnabled: bool = deleteIdentityEnabled
        self.templateName: str = templateName
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["templateName"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ProfileConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.deleteIdentityEnabled, self.templateName))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["deleteIdentityEnabled", "templateName"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
