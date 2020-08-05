class SaasPluginDescriptors():
    """A collection of SaaS plugins.

    Attributes
    ----------
    items : array
        The actual list of SaaS plugins.
    """

    __slots__ = ["items"]

    def __init__(self, items=None):
        self.items = items

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, SaasPluginDescriptors):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.items))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["items"]}

        return cls(**valid_data)
