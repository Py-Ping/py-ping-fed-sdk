class AuthenticationPolicy():
    """An authentication policy.

    Attributes
    ----------
    authnSelectionTrees : array
        The list of authentication policy trees.    defaultAuthenticationSources : array
        The default authentication sources.    failIfNoSelection : boolean
        Fail if policy finds no authentication source.    trackedHttpParameters : array
        The HTTP request parameters to track and make available to authentication sources, selectors, and contract mappings throughout the authentication policy.
    """

    __slots__ = ["authnSelectionTrees", "defaultAuthenticationSources", "failIfNoSelection", "trackedHttpParameters"]

    def __init__(self, authnSelectionTrees=None, defaultAuthenticationSources=None, failIfNoSelection=None, trackedHttpParameters=None):
        self.authnSelectionTrees = authnSelectionTrees
        self.defaultAuthenticationSources = defaultAuthenticationSources
        self.failIfNoSelection = failIfNoSelection
        self.trackedHttpParameters = trackedHttpParameters

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AuthenticationPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.authnSelectionTrees, self.defaultAuthenticationSources, self.failIfNoSelection, self.trackedHttpParameters))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["authnSelectionTrees", "defaultAuthenticationSources", "failIfNoSelection", "trackedHttpParameters"]}

        return cls(**valid_data)
