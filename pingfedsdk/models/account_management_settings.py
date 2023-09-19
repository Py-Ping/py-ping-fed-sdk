from enum import Enum

from pingfedsdk.enums import AccountStatusAlgorithm
from pingfedsdk.model import Model


class AccountManagementSettings(Model):
    """Account management settings.

    Attributes
    ----------
    accountStatusAttributeName: str
        The account status attribute name.

    accountStatusAlgorithm: AccountStatusAlgorithm
        The account status algorithm name. ACCOUNT_STATUS_ALGORITHM_AD -  Algorithm name for Active Directory, which uses a bitmap for each user entry. ACCOUNT_STATUS_ALGORITHM_FLAG - Algorithm name for Oracle Directory Server and other LDAP directories that use a separate attribute to store the user's status. When this option is selected, the Flag Comparison Value and Flag Comparison Status fields should be used.

    flagComparisonValue: str
        The flag that represents comparison value.

    flagComparisonStatus: bool
        The flag that represents comparison status.

    defaultStatus: bool
        The default status of the account.

    """
    def __init__(self, accountStatusAttributeName: str, accountStatusAlgorithm: AccountStatusAlgorithm, flagComparisonValue: str = None, flagComparisonStatus: bool = None, defaultStatus: bool = None) -> None:
        self.accountStatusAttributeName = accountStatusAttributeName
        self.accountStatusAlgorithm = accountStatusAlgorithm
        self.flagComparisonValue = flagComparisonValue
        self.flagComparisonStatus = flagComparisonStatus
        self.defaultStatus = defaultStatus

    def _validate(self) -> bool:
        return any(x for x in ["accountStatusAlgorithm", "accountStatusAttributeName"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AccountManagementSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.accountStatusAttributeName, self.accountStatusAlgorithm, self.flagComparisonValue, self.flagComparisonStatus, self.defaultStatus]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["accountStatusAttributeName", "accountStatusAlgorithm", "flagComparisonValue", "flagComparisonStatus", "defaultStatus"] and v is not None:
                if k == "accountStatusAttributeName":
                    valid_data[k] = str(v)
                if k == "accountStatusAlgorithm":
                    valid_data[k] = AccountStatusAlgorithm[v]
                if k == "flagComparisonValue":
                    valid_data[k] = str(v)
                if k == "flagComparisonStatus":
                    valid_data[k] = bool(v)
                if k == "defaultStatus":
                    valid_data[k] = bool(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["accountStatusAttributeName", "accountStatusAlgorithm", "flagComparisonValue", "flagComparisonStatus", "defaultStatus"]:
                if isinstance(v, Model):
                    body[k] = v.to_dict(remove_nonetypes)
                elif isinstance(v, list):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, dict):
                    vals = {}
                    for x, y in v.items():
                        if isinstance(y, Model):
                            vals[x] = y.to_dict(remove_nonetypes)
                        elif not remove_nonetypes or (remove_nonetypes and y is not None):
                            vals[x] = y
                    body[k] = vals
                elif isinstance(v, set):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, Enum):
                    body[k] = str(v).split('.')[-1]
                elif not remove_nonetypes or (remove_nonetypes and v is not None):
                    body[k] = v
        return body
