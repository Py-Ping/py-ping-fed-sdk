class ApplicationSessionPolicy():
    """Session controls for user facing PingFederate application endpoints, such as the profile management endpoint.

    Attributes
    ----------
    idleTimeoutMins : integer
 The idle timeout period, in minutes. If set to -1, the idle timeout will be set to the maximum timeout. The default is 60.
    maxTimeoutMins : integer
 The maximum timeout period, in minutes. If set to -1, sessions do not expire. The default is 480.

    """

    def __init__(self, idleTimeoutMins:int=None, maxTimeoutMins:int=None) -> None:
        self.idleTimeoutMins = idleTimeoutMins
        self.maxTimeoutMins = maxTimeoutMins

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ApplicationSessionPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.idleTimeoutMins, self.maxTimeoutMins))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["idleTimeoutMins", "maxTimeoutMins"]}

        return cls(**valid_data)