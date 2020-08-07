class LocalIdentityAuthSource():
    """An authentication source name.

    Attributes
    ----------
    id : string
 The persistent, unique ID for the local identity authentication source. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.
    source : string
 The local identity authentication source. Source is unique.

    """

    def __init__(self, var_id=None, source=None) -> None:
        self.var_id = var_id
        self.source = source

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, LocalIdentityAuthSource):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.var_id, self.source))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["var_id", "source"]}

        return cls(**valid_data)