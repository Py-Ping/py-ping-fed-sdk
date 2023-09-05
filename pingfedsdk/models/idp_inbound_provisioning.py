from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.users import Users
from pingfedsdk.models.inbound_provisioning_user_repository import InboundProvisioningUserRepository
from pingfedsdk.models.groups import Groups
from pingfedsdk.models.schema import Schema
from pingfedsdk.enums import ActionOnDelete


class IdpInboundProvisioning(Model):
    """SCIM Inbound Provisioning specifies how and when to provision user accounts and groups.

    Attributes
    ----------
    groupSupport: bool
        Specify support for provisioning of groups.

    userRepository: InboundProvisioningUserRepository
        The local repository for user accounts and groups requiring provisioning.

    customSchema: Schema
        The Custom SCIM Attributes configuration.

    users: Users
        User creation and read configuration.

    groups: Groups
        Group creation and read configuration.

    actionOnDelete: ActionOnDelete
        Specify behavior of how SCIM DELETE requests are handled.

    """

    def __init__(self, customSchema: Schema, groupSupport: bool, groups: Groups, userRepository: InboundProvisioningUserRepository, users: Users, actionOnDelete: ActionOnDelete = None) -> None:
        self.groupSupport = groupSupport
        self.userRepository = userRepository
        self.customSchema = customSchema
        self.users = users
        self.groups = groups
        self.actionOnDelete = actionOnDelete

    def _validate(self) -> bool:
        return any(x for x in ["customSchema", "groupSupport", "groups", "userRepository", "users"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpInboundProvisioning):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.groupSupport, self.userRepository, self.customSchema, self.users, self.groups, self.actionOnDelete]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["groupSupport", "userRepository", "customSchema", "users", "groups", "actionOnDelete"] and v is not None:
                if k == "groupSupport":
                    valid_data[k] = bool(v)
                if k == "userRepository":
                    valid_data[k] = InboundProvisioningUserRepository(**v)
                if k == "customSchema":
                    valid_data[k] = Schema(**v)
                if k == "users":
                    valid_data[k] = Users(**v)
                if k == "groups":
                    valid_data[k] = Groups(**v)
                if k == "actionOnDelete":
                    valid_data[k] = ActionOnDelete[v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["groupSupport", "userRepository", "customSchema", "users", "groups", "actionOnDelete"]:
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
