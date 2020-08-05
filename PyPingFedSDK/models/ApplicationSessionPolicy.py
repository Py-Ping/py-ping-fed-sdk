class ApplicationSessionPolicy():
    """ Session controls for user facing PingFederate application endpoints, such as the profile management endpoint.

    Attributes
    ----------
    idleTimeoutMins : integer
        The idle timeout period, in minutes. If set to -1, the idle timeout will be set to the maximum timeout. The default is 60.
    maxTimeoutMins : integer
        The maximum timeout period, in minutes. If set to -1, sessions do not expire. The default is 480.

    """

    __slots__ = ["idleTimeoutMins", "maxTimeoutMins"]
    def __init__(self, idleTimeoutMins=None, maxTimeoutMins=None):
            self.idleTimeoutMins = idleTimeoutMins
            self.maxTimeoutMins = maxTimeoutMins
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ApplicationSessionPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((idleTimeoutMins, maxTimeoutMins))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
