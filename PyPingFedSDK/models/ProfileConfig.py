class ProfileConfig():
    """A local identity profile management configuration.

    Attributes
    ----------
    deleteIdentityEnabled : boolean
 Whether the end user is allowed to use delete functionality.
    templateName : string
 The template name for end-user profile management.

    """

    def __init__(self, templateName:str, deleteIdentityEnabled:bool=None) -> None:
        self.deleteIdentityEnabled = deleteIdentityEnabled
        self.templateName = templateName

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

        return cls(**valid_data)