class AtmAccessControlSettings():
    """Access control settings for an access token management plugin instance.

    Attributes
    ----------
    allowedClients : array
        If 'restrictClients' is true, this field defines the list of OAuth clients that are allowed to access the token manager.    inherited : boolean
        If this token manager has a parent, this flag determines whether access control settings are inherited from the parent. When set to true, the other fields in this model become read-only. The default value is false.    restrictClients : boolean
        Determines whether access to this token manager is restricted to specific OAuth clients. If false, the 'allowedClients' field is ignored. The default value is false.
    """

    __slots__ = ["allowedClients", "inherited", "restrictClients"]

    def __init__(self, allowedClients=None, inherited=None, restrictClients=None):
        self.allowedClients: list = allowedClients
        self.inherited: bool = inherited
        self.restrictClients: bool = restrictClients

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AtmAccessControlSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.allowedClients, self.inherited, self.restrictClients))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["allowedClients", "inherited", "restrictClients"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__