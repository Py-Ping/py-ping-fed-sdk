class GroupMembershipDetection():
    """Settings to detect group memberships.

    Attributes
    ----------
    groupMemberAttributeName : string
        The name of the attribute that represents group members in a group, also known as group member attribute.
    memberOfGroupAttributeName : string
        The name of the attribute that indicates the entity is a member of a group, also known as member of attribute.

    """

    def __init__(self, groupMemberAttributeName:str, memberOfGroupAttributeName:str=None) -> None:
        self.groupMemberAttributeName = groupMemberAttributeName
        self.memberOfGroupAttributeName = memberOfGroupAttributeName

    def _validate(self) -> bool:
        return any(x for x in ["groupMemberAttributeName"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, GroupMembershipDetection):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.groupMemberAttributeName, self.memberOfGroupAttributeName]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["groupMemberAttributeName", "memberOfGroupAttributeName"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__