class LocalIdentityAuthSourceUpdatePolicy():
    """Settings to determine whether to store attributes that came from third-party authentication sources.

    Attributes
    ----------
    retainAttributes : boolean
        Whether or not to keep attributes after user disconnects.    storeAttributes : boolean
        Whether or not to store attributes that came from authentication sources.    updateAttributes : boolean
        Whether or not to update attributes when users authenticate.    updateInterval : number
        The minimum number of days between updates.
    """

    __slots__ = ["retainAttributes", "storeAttributes", "updateAttributes", "updateInterval"]

    def __init__(self, retainAttributes=None, storeAttributes=None, updateAttributes=None, updateInterval=None):
        self.retainAttributes = retainAttributes
        self.storeAttributes = storeAttributes
        self.updateAttributes = updateAttributes
        self.updateInterval = updateInterval

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, LocalIdentityAuthSourceUpdatePolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.retainAttributes, self.storeAttributes, self.updateAttributes, self.updateInterval))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["retainAttributes", "storeAttributes", "updateAttributes", "updateInterval"]}

        return cls(**valid_data)
