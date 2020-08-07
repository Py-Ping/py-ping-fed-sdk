class Action():
    """A read-only plugin action that either represents a file download or an arbitrary invocation performed by the plugin.

    Attributes
    ----------
    description : string
 The description of this action.
    download : boolean
 Whether this action will trigger a download or invoke an internal action that will return a string result.
    id : string
 The ID of this action.
    invocationRef : str
 Whether this action will trigger a download or invoke an internal action that will return a string result.
    name : string
 The name of this action.

    """

    def __init__(self, description=None, download=None, var_id=None, invocationRef=None, name=None) -> None:
        self.description = description
        self.download = download
        self.var_id = var_id
        self.invocationRef = invocationRef
        self.name = name

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Action):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.description, self.download, self.var_id, self.invocationRef, self.name))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["description", "download", "var_id", "invocationRef", "name"]}

        return cls(**valid_data)