from enum import Enum

from pingfedsdk.model import Model


class GroupMembershipDetection(Model):
    """Settings to detect group memberships.

    Attributes
    ----------
    memberOfGroupAttributeName: str
        The name of the attribute that indicates the entity is a member of a group, also known as member of attribute.

    groupMemberAttributeName: str
        The name of the attribute that represents group members in a group, also known as group member attribute.

    """
    def __init__(self, groupMemberAttributeName: str, memberOfGroupAttributeName: str = None) -> None:
        self.memberOfGroupAttributeName = memberOfGroupAttributeName
        self.groupMemberAttributeName = groupMemberAttributeName

    def _validate(self) -> bool:
        return any(x for x in ["groupMemberAttributeName"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, GroupMembershipDetection):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.memberOfGroupAttributeName, self.groupMemberAttributeName]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["memberOfGroupAttributeName", "groupMemberAttributeName"] and v is not None:
                if k == "memberOfGroupAttributeName":
                    valid_data[k] = str(v)
                if k == "groupMemberAttributeName":
                    valid_data[k] = str(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["memberOfGroupAttributeName", "groupMemberAttributeName"]:
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