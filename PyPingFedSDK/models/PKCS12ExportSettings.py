class PKCS12ExportSettings():
    """Settings for exporting a PKCS12 file from the system.

    Attributes
    ----------
    password : string
 The password for the PKCS12 file that is created.

    """

<<<<<<< HEAD
    def __init__(self, password) -> None:
        self.password = password
=======
    def __init__(self, password):
        self.password: str = password
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["password"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, PKCS12ExportSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.password))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["password"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
