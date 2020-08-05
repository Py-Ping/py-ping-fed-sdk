class BulkConfigMetadata():
    """Model describing how bulk configuration data was generated.

    Attributes
    ----------
    pfVersion : string
        The version of PingFederate this config was generated from.
    """

    __slots__ = ["pfVersion"]

    def __init__(self, pfVersion):
        self.pfVersion = pfVersion

    def _validate(self):
        return any(x for x in ['pfVersion'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, BulkConfigMetadata):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.pfVersion))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["pfVersion"]}

        return cls(**valid_data)
