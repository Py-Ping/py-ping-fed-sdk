class ProxySettings():
    """Proxy settings.

    Attributes
    ----------
    host : string
        Host name.    port : integer
        Port number.
    """

    __slots__ = ["host", "port"]

    def __init__(self, host=None, port=None):
        self.host = host
        self.port = port

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ProxySettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.host, self.port))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["host", "port"]}

        return cls(**valid_data)
