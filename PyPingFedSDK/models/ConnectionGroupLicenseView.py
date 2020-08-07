class ConnectionGroupLicenseView():
    """Connection group license information.

    Attributes
    ----------
    connectionCount : integer
        Maximum number of connections permitted under the group.    endDate : string
        End date for the group.    name : string
        Group name from the license file.    startDate : string
        Start date for the group.
    """

    __slots__ = ["connectionCount", "endDate", "name", "startDate"]

    def __init__(self, connectionCount=None, endDate=None, name=None, startDate=None):
        self.connectionCount: str = connectionCount
        self.endDate: str = endDate
        self.name: str = name
        self.startDate: str = startDate

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ConnectionGroupLicenseView):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.connectionCount, self.endDate, self.name, self.startDate))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["connectionCount", "endDate", "name", "startDate"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__