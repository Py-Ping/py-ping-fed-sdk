class ServiceModel():
    """Service Model.

    Attributes
    ----------
    encryptedSharedSecret : string
<<<<<<< HEAD
 Encrypted shared secret for the service.
    id : string
 Id of the service.
    sharedSecret : string
 Shared secret for the service.

    """

    def __init__(self, encryptedSharedSecret=None, var_id=None, sharedSecret=None) -> None:
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
=======
        Encrypted shared secret for the service.    id : string
        Id of the service.    sharedSecret : string
        Shared secret for the service.
    """

    __slots__ = ["encryptedSharedSecret", "id", "sharedSecret"]

    def __init__(self, encryptedSharedSecret=None, id=None, sharedSecret=None):
        self.encryptedSharedSecret: str = encryptedSharedSecret
        self.id: str = id
        self.sharedSecret: str = sharedSecret

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
>>>>>>> Baseline Sphinx generation
        if isinstance(other, ServiceModel):
            return self.__dict__ == other.__dict__
        return NotImplemented

<<<<<<< HEAD
    def __hash__(self) -> int:
        return hash((self.encryptedSharedSecret, self.var_id, self.sharedSecret))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["encryptedSharedSecret", "var_id", "sharedSecret"]}

        return cls(**valid_data)
=======
    def __hash__(self):
        return hash((self.encryptedSharedSecret, self.id, self.sharedSecret))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["encryptedSharedSecret", "id", "sharedSecret"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
