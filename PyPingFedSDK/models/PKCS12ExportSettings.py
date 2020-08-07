class PKCS12ExportSettings():
    """Settings for exporting a PKCS12 file from the system.

    Attributes
    ----------
    password : string
        The password for the PKCS12 file that is created.
    """

    __slots__ = ["password"]

    def __init__(self, password):
        self.password: str = password

    def _validate(self):
        return any(x for x in ['password'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, PKCS12ExportSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.password))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["password"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__