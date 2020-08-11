class AuthenticationPolicyTree():
    """An authentication policy tree.

    Attributes
    ----------
    authenticationApiApplicationRef : str
 Authentication API Application Id to be used in this policy branch. If the value is not specified, no Authentication API Application will be used.
    description : string
 A description for the authentication policy.
    enabled : boolean
 Whether or not this authentication policy tree is enabled. Default is true.
    name : string
 The authentication policy name. Name is unique.
    rootNode : str
 A node inside the authentication policy tree.

    """

    def __init__(self, authenticationApiApplicationRef=None, description:str=None, enabled:bool=None, name:str=None, rootNode=None) -> None:
        self.authenticationApiApplicationRef = authenticationApiApplicationRef
        self.description = description
        self.enabled = enabled
        self.name = name
        self.rootNode = rootNode

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthenticationPolicyTree):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.authenticationApiApplicationRef, self.description, self.enabled, self.name, self.rootNode))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["authenticationApiApplicationRef", "description", "enabled", "name", "rootNode"]}

        return cls(**valid_data)