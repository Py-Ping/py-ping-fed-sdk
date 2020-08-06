class ServiceModel():
    """Service Model.

    Attributes
    ----------
    encryptedSharedSecret : string
        Encrypted shared secret for the service.    id : string
        Id of the service.    sharedSecret : string
        Shared secret for the service.
    """

    __slots__ = ["encryptedSharedSecret", "id", "sharedSecret"]

    def __init__(self, encryptedSharedSecret=None, id=None, sharedSecret=None):
        self.encryptedSharedSecret = encryptedSharedSecret
        self.id = id
        self.sharedSecret = sharedSecret

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ServiceModel):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.encryptedSharedSecret, self.id, self.sharedSecret))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["encryptedSharedSecret", "id", "sharedSecret"]}

        return cls(**valid_data)
