class ProxySettings():
    """Proxy settings.

    Attributes
    ----------
    host : string
 Host name.
    port : integer
 Port number.

    """

<<<<<<< HEAD
    def __init__(self, host=None, port=None) -> None:
        self.host = host
        self.port = port
=======
    def __init__(self, host=None, port=None):
        self.host: str = host
        self.port: str = port
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ProxySettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.host, self.port))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["host", "port"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
