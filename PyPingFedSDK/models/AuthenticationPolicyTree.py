class AuthenticationPolicyTree():
    """ An authentication policy tree.

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

    __slots__ = ["authenticationApiApplicationRef", "description", "enabled", "name", "rootNode"]
    def __init__(self, authenticationApiApplicationRef=None, description=None, enabled=None, name=None, rootNode=None):
            self.authenticationApiApplicationRef = authenticationApiApplicationRef
            self.description = description
            self.enabled = enabled
            self.name = name
            self.rootNode = rootNode
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AuthenticationPolicyTree):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((authenticationApiApplicationRef, description, enabled, name, rootNode))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
