class AuthenticationPolicy():
    """An authentication policy.

    Attributes
    ----------
    authnSelectionTrees : array
 The list of authentication policy trees.
    defaultAuthenticationSources : array
 The default authentication sources.
    failIfNoSelection : boolean
 Fail if policy finds no authentication source.
    trackedHttpParameters : array
 The HTTP request parameters to track and make available to authentication sources, selectors, and contract mappings throughout the authentication policy.

    """

<<<<<<< HEAD
    def __init__(self, authnSelectionTrees=None, defaultAuthenticationSources=None, failIfNoSelection=None, trackedHttpParameters=None) -> None:
        self.authnSelectionTrees = authnSelectionTrees
        self.defaultAuthenticationSources = defaultAuthenticationSources
        self.failIfNoSelection = failIfNoSelection
        self.trackedHttpParameters = trackedHttpParameters
=======
    def __init__(self, authnSelectionTrees=None, defaultAuthenticationSources=None, failIfNoSelection=None, trackedHttpParameters=None):
        self.authnSelectionTrees: list = authnSelectionTrees
        self.defaultAuthenticationSources: list = defaultAuthenticationSources
        self.failIfNoSelection: bool = failIfNoSelection
        self.trackedHttpParameters: list = trackedHttpParameters
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthenticationPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.authnSelectionTrees, self.defaultAuthenticationSources, self.failIfNoSelection, self.trackedHttpParameters))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["authnSelectionTrees", "defaultAuthenticationSources", "failIfNoSelection", "trackedHttpParameters"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
