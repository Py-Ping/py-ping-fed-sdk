class PKCS12ExportSettings():
    """ Settings for exporting a PKCS12 file from the system.

    Attributes
    ----------
    password : string
        The password for the PKCS12 file that is created.

    """

    __slots__ = ["password"]
    def __init__(self, password):
            self.password = password
    
    def _validate(self):
        return any(x for x in ['password'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, PKCS12ExportSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((password))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
