class ResourceLink():
    """A reference to a resource.

    Attributes
    ----------
    id : string
        The ID of the resource.    location : string
        A read-only URL that references the resource. If the resource is not currently URL-accessible, this property will be null.
    """

    __slots__ = ["id", "location"]

    def __init__(self, id, location=None):
        self.id = id
        self.location = location

    def _validate(self):
        return any(x for x in ['id'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ResourceLink):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.id, self.location))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["id", "location"]}

        return cls(**valid_data)
