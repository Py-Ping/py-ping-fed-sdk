class ServiceModel():
    """Service Model.

    Attributes
    ----------
    encryptedSharedSecret : string
        Encrypted shared secret for the service.
    id : string
        Id of the service.
    sharedSecret : string
        Shared secret for the service.

    """

    def __init__(self, encryptedSharedSecret:str=None, var_id:str=None, sharedSecret:str=None) -> None:
        self.encryptedSharedSecret = encryptedSharedSecret
        self.var_id = var_id
        self.sharedSecret = sharedSecret

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ServiceModel):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.encryptedSharedSecret, self.var_id, self.sharedSecret))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["encryptedSharedSecret", "var_id", "sharedSecret"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__