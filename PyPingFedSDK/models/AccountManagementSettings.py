class AccountManagementSettings():
    """Account management settings.

    Attributes
    ----------
    accountStatusAlgorithm : str
 The account status algorithm name. ACCOUNT_STATUS_ALGORITHM_AD -  Algorithm name for Active Directory, which uses a bitmap for each user entry. ACCOUNT_STATUS_ALGORITHM_FLAG - Algorithm name for Oracle Directory Server and other LDAP directories that use a separate attribute to store the user's status. When this option is selected, the Flag Comparison Value and Flag Comparison Status fields should be used.
    accountStatusAttributeName : string
 The account status attribute name.
    defaultStatus : boolean
 The default status of the account.
    flagComparisonStatus : boolean
 The flag that represents comparison status.
    flagComparisonValue : string
 The flag that represents comparison value.

    """

    def __init__(self, accountStatusAttributeName:str, accountStatusAlgorithm, defaultStatus:bool=None, flagComparisonStatus:bool=None, flagComparisonValue:str=None) -> None:
        self.accountStatusAlgorithm = accountStatusAlgorithm
        self.accountStatusAttributeName = accountStatusAttributeName
        self.defaultStatus = defaultStatus
        self.flagComparisonStatus = flagComparisonStatus
        self.flagComparisonValue = flagComparisonValue

    def _validate(self) -> bool:
        return any(x for x in ["accountStatusAttributeName", "accountStatusAlgorithm"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AccountManagementSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.accountStatusAlgorithm, self.accountStatusAttributeName, self.defaultStatus, self.flagComparisonStatus, self.flagComparisonValue))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["accountStatusAlgorithm", "accountStatusAttributeName", "defaultStatus", "flagComparisonStatus", "flagComparisonValue"]}

        return cls(**valid_data)