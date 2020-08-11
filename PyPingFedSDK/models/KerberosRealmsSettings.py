class KerberosRealmsSettings():
    """Settings for all of the Kerberos Realms.

    Attributes
    ----------
    debugLogOutput : boolean
        Reference to the default logging.
    forceTcp : boolean
        Reference to the default security.
    kdcRetries : string
        Reference to the default Key Distribution Center Retries.
    kdcTimeout : string
        Reference to the default Key Distribution Center Timeout (in seconds).

    """

    def __init__(self, kdcRetries:str, kdcTimeout:str, debugLogOutput:bool=None, forceTcp:bool=None) -> None:
        self.debugLogOutput = debugLogOutput
        self.forceTcp = forceTcp
        self.kdcRetries = kdcRetries
        self.kdcTimeout = kdcTimeout

    def _validate(self) -> bool:
        return any(x for x in ["kdcRetries", "kdcTimeout"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, KerberosRealmsSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.debugLogOutput, self.forceTcp, self.kdcRetries, self.kdcTimeout))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["debugLogOutput", "forceTcp", "kdcRetries", "kdcTimeout"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__