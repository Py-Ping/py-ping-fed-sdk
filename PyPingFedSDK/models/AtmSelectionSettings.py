class AtmSelectionSettings():
    """Selection settings for an access token management plugin instance.

    Attributes
    ----------
    inherited : boolean
        If this token manager has a parent, this flag determines whether selection settings, such as resource URI's, are inherited from the parent. When set to true, the other fields in this model become read-only. The default value is false.    resourceUris : array
        The list of base resource URI's which map to this token manager. A resource URI, specified via the 'aud' parameter, can be used to select a specific token manager for an OAuth request.
    """

    __slots__ = ["inherited", "resourceUris"]

    def __init__(self, inherited=None, resourceUris=None):
        self.inherited = inherited
        self.resourceUris = resourceUris

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AtmSelectionSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.inherited, self.resourceUris))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["inherited", "resourceUris"]}

        return cls(**valid_data)
