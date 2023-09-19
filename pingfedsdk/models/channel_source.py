from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.account_management_settings import AccountManagementSettings
from pingfedsdk.models.change_detection_settings import ChangeDetectionSettings
from pingfedsdk.models.channel_source_location import ChannelSourceLocation
from pingfedsdk.models.group_membership_detection import GroupMembershipDetection
from pingfedsdk.models.resource_link import ResourceLink


class ChannelSource(Model):
    """The source data source and LDAP settings.

    Attributes
    ----------
    dataSource: ResourceLink
        Reference to an LDAP datastore.

    guidAttributeName: str
        the GUID attribute name.

    guidBinary: bool
        Indicates whether the GUID is stored in binary format.

    changeDetectionSettings: ChangeDetectionSettings
        Settings to detect a during provisioning.

    groupMembershipDetection: GroupMembershipDetection
        Settings to detect group memberships.

    accountManagementSettings: AccountManagementSettings
        Account management settings that includes the status and algorithms.

    baseDn: str
        The base DN where the user records are located.

    userSourceLocation: ChannelSourceLocation
        The user provisioning source location settings.

    groupSourceLocation: ChannelSourceLocation
        The group provisioning source location settings.

    """
    def __init__(self, dataSource: ResourceLink, guidAttributeName: str, guidBinary: bool, changeDetectionSettings: ChangeDetectionSettings, groupMembershipDetection: GroupMembershipDetection, accountManagementSettings: AccountManagementSettings, baseDn: str, userSourceLocation: ChannelSourceLocation, groupSourceLocation: ChannelSourceLocation = None) -> None:
        self.dataSource = dataSource
        self.guidAttributeName = guidAttributeName
        self.guidBinary = guidBinary
        self.changeDetectionSettings = changeDetectionSettings
        self.groupMembershipDetection = groupMembershipDetection
        self.accountManagementSettings = accountManagementSettings
        self.baseDn = baseDn
        self.userSourceLocation = userSourceLocation
        self.groupSourceLocation = groupSourceLocation

    def _validate(self) -> bool:
        return any(x for x in ["accountManagementSettings", "baseDn", "changeDetectionSettings", "dataSource", "groupMembershipDetection", "guidAttributeName", "guidBinary", "userSourceLocation"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ChannelSource):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.dataSource, self.guidAttributeName, self.guidBinary, self.changeDetectionSettings, self.groupMembershipDetection, self.accountManagementSettings, self.baseDn, self.userSourceLocation, self.groupSourceLocation]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["dataSource", "guidAttributeName", "guidBinary", "changeDetectionSettings", "groupMembershipDetection", "accountManagementSettings", "baseDn", "userSourceLocation", "groupSourceLocation"] and v is not None:
                if k == "dataSource":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "guidAttributeName":
                    valid_data[k] = str(v)
                if k == "guidBinary":
                    valid_data[k] = bool(v)
                if k == "changeDetectionSettings":
                    valid_data[k] = ChangeDetectionSettings.from_dict(v)
                if k == "groupMembershipDetection":
                    valid_data[k] = GroupMembershipDetection.from_dict(v)
                if k == "accountManagementSettings":
                    valid_data[k] = AccountManagementSettings.from_dict(v)
                if k == "baseDn":
                    valid_data[k] = str(v)
                if k == "userSourceLocation":
                    valid_data[k] = ChannelSourceLocation.from_dict(v)
                if k == "groupSourceLocation":
                    valid_data[k] = ChannelSourceLocation.from_dict(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["dataSource", "guidAttributeName", "guidBinary", "changeDetectionSettings", "groupMembershipDetection", "accountManagementSettings", "baseDn", "userSourceLocation", "groupSourceLocation"]:
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
