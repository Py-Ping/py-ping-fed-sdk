class BulkConfigMetadata():
    """Model describing how bulk configuration data was generated.

    Attributes
    ----------
    pfVersion : string
 The version of PingFederate this config was generated from.

    """

<<<<<<< HEAD
    def __init__(self, pfVersion) -> None:
        self.pfVersion = pfVersion
=======
    def __init__(self, pfVersion):
        self.pfVersion: str = pfVersion
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["pfVersion"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, BulkConfigMetadata):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.pfVersion))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["pfVersion"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
