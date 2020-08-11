class Schema():
    """Custom SCIM Attributes configuration.

    Attributes
    ----------
    attributes : array
    namespace : string

    """

    def __init__(self, attributes:list=None, namespace:str=None) -> None:
        self.attributes = attributes
        self.namespace = namespace

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Schema):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.attributes, self.namespace))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributes", "namespace"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__