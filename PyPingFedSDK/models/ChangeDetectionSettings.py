class ChangeDetectionSettings():
    """Setting to detect changes to a user or a group.

    Attributes
    ----------
    changedUsersAlgorithm : str
 The changed user algorithm. ACTIVE_DIRECTORY_USN - For Active Directory only, this algorithm queries for update sequence numbers on user records that are larger than the last time records were checked. TIMESTAMP - Queries for timestamps on user records that are not older than the last time records were checked. This check is more efficient from the point of view of the PingFederate provisioner but can be more time consuming on the LDAP side, particularly with the Oracle Directory Server. TIMESTAMP_NO_NEGATION - Queries for timestamps on user records that are newer than the last time records were checked. This algorithm is recommended for the Oracle Directory Server.
    groupObjectClass : string
 The group object class.
    timeStampAttributeName : string
 The timestamp attribute name.
    userObjectClass : string
 The user object class.
    usnAttributeName : string
 The USN attribute name.

    """

    def __init__(self, userObjectClass:str, groupObjectClass:str, changedUsersAlgorithm, timeStampAttributeName:str, usnAttributeName:str=None) -> None:
        self.changedUsersAlgorithm = changedUsersAlgorithm
        self.groupObjectClass = groupObjectClass
        self.timeStampAttributeName = timeStampAttributeName
        self.userObjectClass = userObjectClass
        self.usnAttributeName = usnAttributeName

    def _validate(self) -> bool:
        return any(x for x in ["userObjectClass", "groupObjectClass", "changedUsersAlgorithm", "timeStampAttributeName"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ChangeDetectionSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.changedUsersAlgorithm, self.groupObjectClass, self.timeStampAttributeName, self.userObjectClass, self.usnAttributeName))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["changedUsersAlgorithm", "groupObjectClass", "timeStampAttributeName", "userObjectClass", "usnAttributeName"]}

        return cls(**valid_data)