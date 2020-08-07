class ResourceLink():
    """A reference to a resource.

    Attributes
    ----------
    id : string
 The ID of the resource.
    location : string
 A read-only URL that references the resource. If the resource is not currently URL-accessible, this property will be null.

    """

<<<<<<< HEAD
    def __init__(self, var_id, location=None) -> None:
        self.var_id = var_id
        self.location = location
=======
    def __init__(self, id, location=None):
        self.id: str = id
        self.location: str = location
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["var_id"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ResourceLink):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.var_id, self.location))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["var_id", "location"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
